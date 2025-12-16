from .app import app
from flask import render_template, request, url_for, redirect, flash
from appSoutenance.models import Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer, Admini
from sqlalchemy import desc
from flask_login import login_user, logout_user, login_required, current_user
from appSoutenance.forms import LoginForm


@app.route('/')
@app.route('/connexion/')
def index():
    form = LoginForm()
    return render_template("index.html",
                           title="Soutenance - Connexion",
                           accueil="index",
                           form =form)


@app.route('/login/', methods=('GET', 'POST', ))
def login():
    """Redirection vers la page de connexion du site"""
    form = LoginForm()
    if not form.is_submitted():
        form.next.data = request.args.get('next')
    elif form.validate_on_submit():
        etudiant = form.get_authenticated_etudiant()
        enseignant = form.get_authenticated_enseignant()
        admin = form.get_authenticated_admin()

        if etudiant is not None:
            login_user(etudiant)
            return redirect(url_for("accueil_etudiant"))
        
        elif enseignant is not None:
            login_user(enseignant)
            return redirect(url_for("accueil_enseignant"))
        
        elif admin is not None:
            login_user(admin)
            return redirect(url_for("accueil_admin"))
        
        else:
            flash("Login ou mot de passe incorrect", "warning")

    return render_template("index.html", form=form)

########################## POUR LES ÉTUDIANTS ##########################

def sort_id(demarche):
    return demarche.id_demarche

@app.route('/etudiant/')
@login_required
def accueil_etudiant():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    lst_demarches = sorted(list(etudiant.demarches), key=sort_id)[:2]
    return render_template("etudiant/accueil_etu.html", accueil="accueil_etudiant", personne=etudiant, title="Accueil", liste_dem=lst_demarches)

@app.route('/etudiant/demarches/')
def demarches():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.get(num_personne)
    #lst_demarches = sorted(list(etudiant.demarches), key=sort_id)
    lst_demarches = {
        15: ["Google", 2, 'refusé'],
        1: ["Microsoft", 8, 'validé'],
        2: ["Ubisoft", 9, 'en attente de validation'],
        11: ["Apple", 10, 'convention signée'],
        12: ["IUT'O", 256, 'validé'],
        9: ["Cognosphère", 10, 'convention signée']
    }
    return render_template("etudiant/demarches.html", accueil="accueil_etudiant", personne=etudiant, title="Mes démarches", liste_dem=lst_demarches)

@app.route('/etudiant/stage/')
def info_stage():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/info_stage_valide.html", accueil="accueil_etudiant", personne=etudiant, title="Mon stage")

@app.route('/etudiant/demarches/new1/')
def nouvelle_demarche1():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche1.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/new2/')
def nouvelle_demarche2():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche2.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/new3/')
def nouvelle_demarche3():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche3.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/resume/')
def resume_demarche_etudiant():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/resume_demarche.html", accueil="accueil_etudiant", personne=etudiant, title="Résumé de la démarche")

########################## POUR LES ENSEIGNANTS ##########################


@app.route('/enseignant/')
@login_required
def accueil_enseignant():
    enseignant = current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))
    return render_template("enseignant/accueil_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Accueil")

@app.route('/enseignant/planning/')
def planning_enseignant():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    return render_template("enseignant/planning_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Planning enseignant")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    lesEtudiants = Etudiant.query.all()
    res = []

    for etudiant in lesEtudiants:
        appartenance = Appartenir.query.filter_by(
            id_etudiant=etudiant.id_etudiant).first()
        promo = Promo.query.filter_by(nom_promo=appartenance.nom_promo,
                                      annee_promo=appartenance.annee_promo
                                     ).first() if appartenance else None

        nb_demarches = Demarche.query.filter_by(
            id_etudiant=etudiant.id_etudiant).count()

        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant)\
            .order_by(desc(Demarche.date_envoi)).first()

        res.append({
            'etudiant':
                etudiant,
            'formation':
                promo.formation_promo if promo else "None",
            'annee':
                promo.annee_promo if promo else "None",
            'promo':
                promo.nom_promo if promo else "None",
            'nb_demarches':
                nb_demarches,
            'situation':
                derniere_demarche.situation if derniere_demarche else "Aucune"
        })
    return render_template("enseignant/lst_etudiants_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Liste des étudiants",resultats=res)

@app.route('/enseignant/liste+etu/etudiant/')
def detail_etudiant_ens():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    return render_template("admin/detail_etudiant_ens.html", accueil="accueil_enseignant", personne=enseignant, title="Detail de l'etudiant")

########################## POUR LES ADMINISTRATEURS ##########################


@app.route('/admin/')
@login_required
def accueil_admin():
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    nb_etudiants = Etudiant.query.count()
    nb_stages_trouves = Stage.query.count()
    nb_etudiants_alternants = Appartenir.query.filter_by(
        regime_etudiant='Alternance').count()
    nb_soutenances_alternants = 0
    nb_soutenances_posees = Soutenance.query.count()
    nb_soutenances_attente_candide = 0
    return render_template(
        "admin/accueil_admin.html",
        accueil="accueil_admin",
        title="Accueil",
        personne=admin,
        nb_stages_trouves=nb_stages_trouves,
        nb_etudiants=nb_etudiants,
        nb_etudiants_alternants=nb_etudiants_alternants,
        nb_soutenances_alternants=nb_soutenances_alternants,
        nb_soutenances_posees=nb_soutenances_posees,
        nb_soutenances_attente_candide=nb_soutenances_attente_candide)


@app.route('/admin/planning/')
def planning_admin():
    return render_template("admin/planning_admin.html",
                           accueil="accueil_admin",
                           title="Planning")


@app.route('/admin/liste+enseignants/<int:id>/')
@login_required
def detail_enseignant(id):
    enseignant = Enseignant.query.get(id)
    etudiants_suivis = Tutorer.query.filter_by(id_enseignant=enseignant.id_enseignant)
    liste_etudiants_suivis = []
    for etudiant in etudiants_suivis:
        liste_etudiants_suivis.append(Etudiant.query.get(etudiant.id_etudiant))
    enseignant_promo = Promo.query.filter_by(id_enseignant=enseignant.id_enseignant).first()
    jury_soutenances = Soutenance.query.join(Composer, Soutenance.id_soutenance == Composer.id_soutenance)\
                        .filter(Composer.id_enseignant == enseignant.id_enseignant).all()
    jury_soutenances = ', '.join([f"Soutenance ID {s.id_soutenance}" for s in jury_soutenances])

    return render_template("admin/detail_enseignant.html",
                           accueil="accueil_admin",
                           title="Detail de l'enseignant",
                           enseignant=enseignant,
                           etudiants_suivis=liste_etudiants_suivis,
                           enseignant_promo=enseignant_promo)


@app.route('/admin/liste+etudiants/<int:id>/')
@login_required
def detail_etudiant_admin(id):
    etudiant = Etudiant.query.get(id)
    return render_template("admin/detail_etudiant_admin.html",
                           accueil="accueil_admin",
                           title="Detail de l'etudiant",
                           etudiant=etudiant)


@app.route('/admin/liste+enseignants/')
@login_required
def liste_ens_admin():
    # Récupération des filtres
    annee = request.args.get('annee')
    formation = request.args.get('formation')
    situation = request.args.get('situation')

    lesEnseignants = Enseignant.query

    if annee or formation:
        # On récupère les enseignants qui sont tuteurs d'au moins un étudiant correspondant aux filtres
        lesEnseignants = lesEnseignants.join(Tutorer).join(Etudiant).join(Promo, Etudiant.promos)

        if annee:
            niveau = "BUT2" if annee == '2A' else "BUT3"
            lesEnseignants = lesEnseignants.filter(Promo.nom_promo.like(f"%{niveau}%"))
        if formation:
            terme = "Informatique" if formation == "Info" else formation
            lesEnseignants = lesEnseignants.filter(Promo.formation_promo.like(f"%{terme}%"))

        lesEnseignants = lesEnseignants.distinct()

    lesEnseignants = lesEnseignants.all()
    res = []

    for enseignant in lesEnseignants:
        nb_tutore = Tutorer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()
        nb_soutenances_total = Composer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()
        nb_soutenances_posees = Composer.query.join(Soutenance, Composer.id_soutenance == Soutenance.id_soutenance)
        nb_soutenances_posees = nb_soutenances_posees.filter(Composer.id_enseignant == enseignant.id_enseignant)

        if situation == 'Trouvé' and nb_soutenances_posees.count() == 0:
            continue
        if situation == 'En cours' and nb_soutenances_posees.count() > 0:
            continue
        nb_soutenances_posees = nb_soutenances_posees.count()

        res.append({
            "enseignant": enseignant,
            "nb_tutores": nb_tutore,
            "nb_soutenances": nb_soutenances_total,
            "nb_soutenances_posees": nb_soutenances_posees,
        })

    return render_template("admin/lst_enseignants.html",
                           accueil="accueil_admin",
                           title="Liste enseignants",
                           resultats=res)


@app.route('/admin/liste+etudiants/')
@login_required
def liste_etu_admin():
    annee_filter = request.args.get('annee')
    formation_filter = request.args.get('formation')
    situation_filter = request.args.get('situation')
    tri = request.args.get("trier", "Nom") # Par défaut, trié par nom

    lesEtudiants_query = Etudiant.query.join(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant).join(Promo, (Appartenir.nom_promo == Promo.nom_promo) & (Appartenir.annee_promo == Promo.annee_promo))

    # Les filtres
    if annee_filter:
        niveau = "BUT2" if annee_filter == '2A' else "BUT3"
        lesEtudiants_query = lesEtudiants_query.filter(Promo.nom_promo.like(f"%{niveau}%"))
    if formation_filter:
        terme = "Informatique" if formation_filter == "Info" else formation_filter
        lesEtudiants_query = lesEtudiants_query.filter(Promo.formation_promo.like(f"%{terme}%"))

    lesEtudiants = lesEtudiants_query.distinct().all()

    res = []

    for etudiant in lesEtudiants:
        appartenance = Appartenir.query.filter_by(
            id_etudiant=etudiant.id_etudiant).first()
        
        promo = Promo.query.filter_by(nom_promo=appartenance.nom_promo,
                                      annee_promo=appartenance.annee_promo
                                     ).first() if appartenance else None
        
        nb_demarches = Demarche.query.filter_by(
            id_etudiant=etudiant.id_etudiant).count()

        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant)\
                                  .order_by(desc(Demarche.date_envoi)).first()

        current_situation = derniere_demarche.situation if derniere_demarche else "Aucune"

        if situation_filter:
            if situation_filter == 'Trouvé' and current_situation != 'Acceptée':
                continue
            elif situation_filter == 'En cours' and current_situation != 'En attente':
                continue

        res.append({
            'etudiant': etudiant,
            'formation': promo.formation_promo if promo else "Aucune trouvée",
            'annee': promo.annee_promo if promo else "Aucune trouvée",
            'promo': promo.nom_promo if promo else "Aucune trouvée",
            'nb_demarches': nb_demarches,
            'situation': current_situation
        })

    # Le tri
    if tri == "Nom":
        res = sorted(res, key=lambda x: x["etudiant"].nom_etudiant.lower())
    elif tri == "Annee":
        res = sorted(res, key=lambda x: (x["annee"] == "N/A", x["annee"]))
    elif tri == "NbDemarches":
        res = sorted(res, key=lambda x: x["nb_demarches"], reverse=True)

    return render_template("admin/lst_etudiants_admin.html",
                           accueil="accueil_admin",
                           title="Liste etudiants",
                           resultats=res)


if __name__ == "__main__":
    app.run()
