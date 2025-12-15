from .app import app
from flask import Flask, flash
from flask import render_template, request, url_for, redirect
from appSoutenance.models import Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer, Admini, Compose
from sqlalchemy import desc
from flask_wtf import FlaskForm
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

# @app.route("/login", methods=["GET","POST"])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = Etudiant.query.filter_by(login_etudiant=form.Login.data).first()

#         if user and user.pwd_etudiant == form.Password.data:
#             login_user(user)
#             if user.metier.lower() == "chercheur":
#                 return redirect(url_for("accueil_cher"))
#             elif user.metier.lower() == "administrateur":
#                 return redirect(url_for("accueil_admin"))
#             elif user.metier.lower() == "technicien":
#                 return redirect(url_for("accueil_tech"))

#         return("Login ou mot de passe incorrect")

#     return render_template("index.html", form=form, error="Login ou mot de passe incorrect")

# @app.route('/login/', methods=('GET', 'POST', ))
# def login():
#     """Redirection vers la page de connexion du site"""
#     form = LoginForm()
#     if not form.is_submitted():
#         form.next.data = request.args.get('next')
#     elif form.validate_on_submit():
#         etudiant = form.get_authenticated_etudiant()
#         enseignant = form.get_authenticated_enseignant()
#         admin = form.get_authenticated_admin()

#         if etudiant is not None:
#             login_user(etudiant)
#             return redirect(url_for("accueil_etudiant"))
        
#         elif enseignant is not None:
#             login_user(enseignant)
#             return redirect(url_for("accueil_enseignant"))
        
#         elif admin is not None:
#             login_user(admin)
#             return redirect(url_for("accueil_admin"))
        
#         else:
#             flash("Login ou mot de passe incorrect", "warning")

#     return render_template("index.html", form=form)

@app.route('/login/', methods=('GET', 'POST', ))
def login():
    """Redirection vers la page de connexion du site"""
    form = LoginForm()
    
    # 1. GESTION DU GET OU DU NEXT
    if not form.is_submitted():
        form.next.data = request.args.get('next')
        
    # 2. GESTION DU POST ET DE L'AUTHENTIFICATION
    elif form.validate_on_submit(): # <-- Cette ligne doit retourner True
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

    # 3. GESTION DE L'ÉCHEC (y compris l'échec de la validation)
    
    # Si validate_on_submit() a échoué, vérifions les erreurs :
    if form.errors:
        print("--- ERREURS DE FORMULAIRE ---")
        print(form.errors)
        print("----------------------------")
        # Flasher un message d'erreur si la validation WTForms échoue
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Erreur de validation sur le champ {field} : {error}", "error")

    # On retourne la page de connexion après échec ou si c'est un GET initial
    return render_template("index.html", form=form)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("index"))


########################## POUR LES ÉTUDIANTS ##########################

def sort_id(demarche):
    return demarche.id_demarche

@app.route('/etudiant/')
@login_required
def accueil_etudiant():
    etudiant = current_user
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
def detail_enseignant(id):
    enseignant = Enseignant.query.get(id)
    return render_template("admin/detail_enseignant.html",
                           accueil="accueil_admin",
                           title="Detail de l'enseignant",
                           enseignant=enseignant)


@app.route('/admin/liste+etudiants/<int:id>/')
def detail_etudiant_admin(id):
    etudiant = Etudiant.query.get(id)
    return render_template("admin/detail_etudiant_admin.html",
                           accueil="accueil_admin",
                           title="Detail de l'etudiant",
                           etudiant=etudiant)


@app.route('/admin/liste+enseignants/')
def liste_ens_admin():
    lesEnseignants = Enseignant.query.all()
    res = []

    for enseignant in lesEnseignants:
        nb_tutore = Tutorer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()
        nb_soutenances = Composer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()

        res.append({
            "enseignant": enseignant,
            "nb_tutores": nb_tutore,
            "nb_soutenances": nb_soutenances,
        })

    return render_template("admin/lst_enseignants.html",
                           accueil="accueil_admin",
                           title="Liste enseignants",
                           resultats=res)


@app.route('/admin/liste+etudiants/')
def liste_etu_admin():
    lesEtudiants = Etudiant.query.all()

    tri = request.args.get("trier", "Nom")

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
                promo.formation_promo,
            'annee':
                promo.annee_promo,
            'promo':
                promo.nom_promo,
            'nb_demarches':
                nb_demarches,
            'situation':
                derniere_demarche.situation if derniere_demarche else "Aucune"
        })

    if tri == "Nom":
        res = sorted(res, key=lambda x: x["etudiant"].nom_etudiant)
    elif tri == "Annee":
        res = sorted(res, key=lambda x: (x["annee"] is None, x["annee"]))
    elif tri == "NbDemarches":
        res = sorted(res, key=lambda x: x["nb_demarches"], reverse=True)

    return render_template("admin/lst_etudiants_admin.html",
                           accueil="accueil_admin",
                           title="Liste etudiants",
                           resultats=res)


if __name__ == "__main__":
    app.run()
