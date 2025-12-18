from collections import defaultdict
from .app import app, db
from flask import render_template, request, url_for, redirect, flash
from appSoutenance.models import db,  Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer, MaitreStage, Entreprise, Admini
from sqlalchemy import desc, asc, distinct, func
from .importer_csv import importer_etudiants_stages, importer_entreprises
from flask_login import login_user, logout_user, login_required, current_user
from appSoutenance.forms import *




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
                promo.formatio if promo else "None",
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




@app.route('/admin/', methods=['GET', 'POST'])
@login_required
def accueil_admin():
    unForm = ImportForm()
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    if unForm.validate_on_submit():
        print("c'est bon")
        file_storage = unForm.ficCSV.data
        type_import = unForm.type_import.data

        success = False
        message = ""
    
        if type_import == 'etudiants_stages':
            success, message = importer_etudiants_stages(file_storage)
        elif type_import == 'entreprises':
            success, message = importer_entreprises(file_storage)

        if success:
            flash(f"Importation réussie : {message}", 'success')
        else:
            flash(f"Échec de l'importation : {message}", 'danger')

        return redirect(url_for('accueil_admin'))

    # Filtres
    annee_filter = request.args.get('annee')
    formation_filter = request.args.get('formation')

    requete_les_etudiants = Etudiant.query.join(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant).join(Promo, (Appartenir.nom_promo == Promo.nom_promo) & (Appartenir.annee_promo == Promo.annee_promo))

    if annee_filter == "2A":
        requete_les_etudiants = requete_les_etudiants.filter((Promo.nom_promo.like("%BUT2%")) | (Promo.nom_promo.like("%BUT 2%")))
    if annee_filter == "3A":
        requete_les_etudiants = requete_les_etudiants.filter((Promo.nom_promo.like("%BUT3%")) | (Promo.nom_promo.like("%BUT 3%")))

    if formation_filter:
        terme = "Informatique" if formation_filter == "Info" else formation_filter
        requete_les_etudiants = requete_les_etudiants.filter(Promo.formation_promo.like(f"%{terme}%"))

    # Nombre total d'étudiants
    nb_etudiants = requete_les_etudiants.distinct().count()

    # Nombre de stages trouvés
    requete_nb_stages_trouves = requete_les_etudiants.join(Demarche, Etudiant.id_etudiant == Demarche.id_etudiant)\
                                                .join(Stage, Demarche.id_demarche == Stage.id_demarche)\
                                                .filter(Demarche.situation == 'Acceptée')
    nb_stages_trouves = requete_nb_stages_trouves.with_entities(Stage.id_stage).distinct().count()

    # Nombre d'étudiants alternants
    requete_nb_etudiants_alternants = requete_les_etudiants.filter(Appartenir.regime_etudiant == 'Formation apprentissage')
    nb_etudiants_alternants = requete_nb_etudiants_alternants.distinct().count()

    # Nombre de soutenances d'alternants prévues
    requete_nb_soutenances_alternants = requete_nb_etudiants_alternants.join(Demarche, Etudiant.id_etudiant == Demarche.id_etudiant)\
                                                                    .join(Stage, Demarche.id_demarche == Stage.id_demarche)\
                                                                    .join(Soutenance, Stage.id_stage == Soutenance.id_stage)
    nb_soutenances_alternants = requete_nb_soutenances_alternants.with_entities(Soutenance.id_soutenance).distinct().count()

    # Nombre de soutenances posées par tuteur
    requete_soutenances = requete_les_etudiants.join(Demarche, Etudiant.id_etudiant == Demarche.id_etudiant)\
                                                     .join(Stage, Demarche.id_demarche == Stage.id_demarche)\
                                                     .join(Soutenance, Stage.id_stage == Soutenance.id_stage)
    nb_soutenances_posees = requete_soutenances.with_entities(Soutenance.id_soutenance).distinct().count()

    # Nombre de soutenances en attente de candide
    requete_ids_soutenances_pertinentes = requete_soutenances.with_entities(Soutenance.id_soutenance).distinct()
    soutenances_jury_complet_ids = db.session.query(Composer.id_soutenance).group_by(Composer.id_soutenance).having(func.count(Composer.id_enseignant) >= 2)
    nb_soutenances_attente_candide = requete_ids_soutenances_pertinentes.filter(Soutenance.id_soutenance.notin_(soutenances_jury_complet_ids)).count()


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
        nb_soutenances_attente_candide=nb_soutenances_attente_candide,
        createForm = unForm)


MOIS = {
    1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 5: 'Mai', 6: 'Juin',
    7: 'Juil', 8: 'Août', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
}


@app.route('/admin/planning/')
@login_required
def planning_admin():
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    args = request.args
    nom_promo = args.get('nom_promo')
    regime = args.get('regime')
    formation_promo = args.get('formation_promo')
    date_soutenance = args.get('date_soutenance')
    heure_soutenance = args.get('heure_soutenance')
    jury_enseignant_id = args.get('jury_enseignant_id')
    tri = args.get('trier')


    dates_disponibles_dt = db.session.query(distinct(Soutenance.dateS)).order_by(Soutenance.dateS).all()
    dates_disponibles = [(d[0].strftime('%Y-%m-%d'), f"{d[0].day} {MOIS[d[0].month]}") for d in dates_disponibles_dt]


    heures_disponibles = db.session.query(distinct(Soutenance.h_debut)).order_by(Soutenance.h_debut).all()
    heures_disponibles = [h[0] for h in heures_disponibles]


    # Enseignants (Jury)
    enseignants_disponibles = Enseignant.query.order_by(Enseignant.nom_enseignant).all()


    query = Soutenance.query.join(Stage).join(Demarche).join(Etudiant).join(Appartenir).join(Promo)

    # Filtres
    if nom_promo == "2A":
        query = query.filter((Promo.nom_promo.like("%BUT2%")) | (Promo.nom_promo.like("%BUT 2%")))
    if nom_promo == "3A":
        query = query.filter((Promo.nom_promo.like("%BUT3%")) | (Promo.nom_promo.like("%BUT 3%")))

    if formation_promo:
        terme = "Informatique" if formation_promo == "Info" else formation_promo
        query = query.filter(Promo.formation_promo.like(f"%{terme}%"))

    if regime:
        regime_val = "Formation initiale" if regime == "Initial" else "Formation apprentissage"
        query = query.filter(Appartenir.regime_etudiant == regime_val)

    if date_soutenance:
        query = query.filter(Soutenance.dateS == date_soutenance)

    if heure_soutenance:
        query = query.filter(Soutenance.h_debut == heure_soutenance)

    if jury_enseignant_id:
        query = query.join(Composer, Soutenance.id_soutenance == Composer.id_soutenance) \
                     .filter(Composer.id_enseignant == jury_enseignant_id)

    # Tri
    if tri == "Nom":
        query = query.order_by(Etudiant.nom_etudiant, Etudiant.prenom_etudiant)
    else:
        query = query.order_by(asc(Soutenance.dateS), asc(Soutenance.h_debut))

    lesSoutenances = query.distinct().all()
    regroupement = {}

    for soutenance in lesSoutenances:
        stage = Stage.query.get(soutenance.id_stage)

        
        etudiant_lie = None
        if stage and stage.demarche:
            etudiant_lie = stage.demarche.etudiant
       
        enseignants_jury = db.session.query(Enseignant).join(Composer).filter(Composer.id_soutenance == soutenance.id_soutenance).all()
        membres_jury_noms =', '.join( [f"{e.nom_enseignant} {e.prenom_enseignant}" for e in enseignants_jury])

        promo_etudiant = "N/C"
        if etudiant_lie:
            appartenance = Appartenir.query.filter_by(id_etudiant=etudiant_lie.id_etudiant).first()
            if appartenance:
                promo_etudiant = appartenance.nom_promo

        if not membres_jury_noms:
            membres_jury_noms = "Jury non assigné"


        if etudiant_lie:
            jour_mois = soutenance.dateS.day
            mois_francais = MOIS[soutenance.dateS.month]
            date_formatee = f"{jour_mois} {mois_francais} {soutenance.dateS.year}"


            cle_regroupement = f"{soutenance.dateS.strftime('%Y-%m-%d')}-{soutenance.h_debut}-{soutenance.salle}-{membres_jury_noms}"
           
            if cle_regroupement not in regroupement:
                regroupement[cle_regroupement] = {
                    'dateS': date_formatee,
                    'h_debut': soutenance.h_debut,
                    'salle': soutenance.salle,
                    'jury_noms': membres_jury_noms,
                    'nom_promo': promo_etudiant,
                    'stages': []
                }
            regroupement[cle_regroupement]['stages'].append({
                'nom_etudiant': etudiant_lie.nom_etudiant,
                'prenom_etudiant': etudiant_lie.prenom_etudiant,
                'titre_stage': stage.titre_stage if stage else "Titre de stage non trouvé"
            })

    resultats_regroupes = list(regroupement.values())
    return render_template("admin/planning_admin.html",
                           accueil="accueil_admin",
                           title="Planning", resultats = resultats_regroupes,
                           heures_disponibles = heures_disponibles,
                           enseignants_disponibles = enseignants_disponibles,
                           dates_disponibles = dates_disponibles)


@app.route('/admin/planning/creation_soutenance/', methods =["GET", "POST"])
@login_required
def creation_soutenance():
    unForm= FormSoutenance()
    return render_template("admin/creation_soutenance.html", createForm=unForm)



@app.route('/admin/liste+enseignants/<int:id>/')
@login_required
def detail_enseignant(id):
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    enseignant = Enseignant.query.get(id)
    etudiant_suivi = Tutorer.query.filter_by(id_enseignant=enseignant.id_enseignant)
    etudiant_suivi = Etudiant.query.get(etudiant_suivi.first().id_etudiant)
    # liste_etudiants_suivis = []
    # for etudiant in etudiants_suivis:
    #     liste_etudiants_suivis.append(Etudiant.query.get(etudiant.id_etudiant))
    enseignant_promo = Promo.query.filter_by(id_enseignant=enseignant.id_enseignant).first()
    jury_soutenances = Soutenance.query.join(Composer, Soutenance.id_soutenance == Composer.id_soutenance)\
                        .filter(Composer.id_enseignant == enseignant.id_enseignant).all()
    jury_soutenances = ', '.join([f"Soutenance n°{s.id_soutenance} ({Stage.query.get(s.id_stage).titre_stage}). "
                                  for s in jury_soutenances])

    return render_template("admin/detail_enseignant.html",
                           accueil="accueil_admin",
                           title="Detail de l'enseignant",
                           enseignant=enseignant,
                           etudiant_suivi=etudiant_suivi,
                           enseignant_promo=enseignant_promo,
                           jury_soutenances=jury_soutenances)




@app.route('/admin/liste+etudiants/<int:id>/')
@login_required
def detail_etudiant_admin(id):
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    etudiant = Etudiant.query.get(id)
    etudiant_promo = Appartenir.query.filter_by(id_etudiant=etudiant.id_etudiant).first()
    demarches = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant).all()
    
    tuteur = Tutorer.query.filter_by(id_etudiant=etudiant.id_etudiant).first()
    if tuteur:
        tuteur = Enseignant.query.get(tuteur.id_enseignant)
    else:
        tuteur = None
    stage_etudiant = Stage.query.join(Demarche, Stage.id_demarche == Demarche.id_demarche)\
                        .filter(Demarche.id_etudiant == etudiant.id_etudiant).first()

    maitre_stage = MaitreStage.query.get(stage_etudiant.id_maitre) if stage_etudiant else None
    entreprise = Entreprise.query.get(maitre_stage.id_entreprise) if maitre_stage else None

    return render_template("admin/detail_etudiant_admin.html",
                           accueil="accueil_admin",
                           title="Detail de l'etudiant",
                           etudiant=etudiant,
                           etudiant_promo=etudiant_promo,
                           demarches=demarches,
                           tuteur=tuteur,
                           stage_etudiant=stage_etudiant,
                           maitre_stage=maitre_stage,
                           entreprise=entreprise)


@app.route('/admin/liste+enseignants/')
@login_required
def liste_ens_admin():
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    # Récupération des filtres
    soutenance = request.args.get('soutenance')
    situation = request.args.get('situation')
    candide = request.args.get('candide')

    lesEnseignants = Enseignant.query
    if soutenance:
        lesEnseignants = lesEnseignants.join(Tutorer, Tutorer.id_enseignant == Enseignant.id_enseignant).join(Etudiant, Tutorer.id_etudiant == Etudiant.id_etudiant).join(Promo, Etudiant.promos)

        if soutenance == "Soutenance":
            lesEnseignants = lesEnseignants.join(Composer, Composer.id_enseignant == Enseignant.id_enseignant).join(Soutenance, Soutenance.id_soutenance == Composer.id_soutenance)
        elif soutenance == "NonSoutenance":
            lesEnseignants = lesEnseignants.outerjoin(Composer, Composer.id_enseignant == Enseignant.id_enseignant).outerjoin(Soutenance, Soutenance.id_soutenance == Composer.id_soutenance)
            lesEnseignants = lesEnseignants.filter(Soutenance.id_soutenance.is_(None))

    # Réccupérer soutenances avec jury non complet : Composer -> Soutenance -> Stage -> Demarche -> Etudiant -> Tutorer -> Enseignant
    # id de l'étudiant =! de l'id de l'étudiant dont l'enseignant est tuteur
    if candide == 'NonCandide':
        sq = db.session.query(Enseignant.id_enseignant)\
            .join(Composer, Composer.id_enseignant == Enseignant.id_enseignant)\
            .join(Soutenance, Soutenance.id_soutenance == Composer.id_soutenance)\
            .join(Stage, Stage.id_stage == Soutenance.id_stage)\
            .join(Demarche, Demarche.id_demarche == Stage.id_demarche)\
            .join(Etudiant, Etudiant.id_etudiant == Demarche.id_etudiant)\
            .outerjoin(Tutorer, (Tutorer.id_enseignant == Enseignant.id_enseignant) & (Tutorer.id_etudiant == Etudiant.id_etudiant))\
            .filter(Tutorer.id_enseignant.is_(None))
        lesEnseignants = lesEnseignants.filter(Enseignant.id_enseignant.notin_(sq))


    lesEnseignants = lesEnseignants.all()
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
@login_required
def liste_etu_admin():
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    annee_filter = request.args.get('annee')
    formation_filter = request.args.get('formation')
    situation_filter = request.args.get('situation')
    regime_filter = request.args.get('regime')
    tri = request.args.get("trier", "Nom") # Par défaut, trié par nom

    requete_les_etudiants = Etudiant.query.join(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant).join(Promo, (Appartenir.nom_promo == Promo.nom_promo) & (Appartenir.annee_promo == Promo.annee_promo))

    # Les filtres
    if annee_filter == "2A":
        requete_les_etudiants = requete_les_etudiants.filter((Promo.nom_promo.like("%BUT2%")) | (Promo.nom_promo.like("%BUT 2%")))
    if annee_filter == "3A":
        requete_les_etudiants = requete_les_etudiants.filter((Promo.nom_promo.like("%BUT3%")) | (Promo.nom_promo.like("%BUT 3%")))

    if formation_filter:
        terme = "Informatique" if formation_filter == "Info" else formation_filter
        requete_les_etudiants = requete_les_etudiants.filter(Promo.formation_promo.like(f"%{terme}%"))

    if regime_filter:
        regime = "Formation initiale" if regime_filter == "Formation Initiale" else "Formation apprentissage"
        requete_les_etudiants = requete_les_etudiants.filter(Appartenir.regime_etudiant == regime)

    lesEtudiants = requete_les_etudiants.distinct().all()

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
            elif situation_filter == 'En cours' and current_situation != 'En cours':
                continue

        res.append({
            'etudiant': etudiant,
            'formation': promo.formation_promo if promo else "Aucune trouvée",
            'regime': "FI" if appartenance.regime_etudiant == "Formation initiale" else "Apprenti",
            'annee': promo.annee_promo if promo else "Aucune trouvée",
            'promo': promo.nom_promo if promo else "Aucune trouvée",
            'nb_demarches': nb_demarches,
            'situation': current_situation
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


@app.route('/admin/liste+soutenances+candides/')
@login_required
def liste_soutenances_candides_admin():
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    # IDs des soutenances qui ont un jury complet (>= 2 membres)
    soutenances_jury_complet_ids = db.session.query(Composer.id_soutenance)\
        .group_by(Composer.id_soutenance)\
        .having(func.count(Composer.id_enseignant) >= 2)

    # n récupère toutes les soutenances dont l'ID n'est pas dans la liste des complets
    requete_soutenances_sans_candide = db.session.query(Soutenance, Etudiant, Enseignant, Stage)\
        .join(Stage, Soutenance.id_stage == Stage.id_stage)\
        .join(Demarche, Stage.id_demarche == Demarche.id_demarche)\
        .join(Etudiant, Demarche.id_etudiant == Etudiant.id_etudiant)\
        .outerjoin(Tutorer, Etudiant.id_etudiant == Tutorer.id_etudiant)\
        .outerjoin(Enseignant, Tutorer.id_enseignant == Enseignant.id_enseignant)\
        .filter(Soutenance.id_soutenance.notin_(soutenances_jury_complet_ids))\
        .all()
    
    resultats = []
    for soutenance, etudiant, tuteur, stage in requete_soutenances_sans_candide:
        resultats.append({
            'soutenance': soutenance,
            'etudiant': etudiant,
            'tuteur': tuteur,
            'stage': stage
        })

    return render_template("admin/lst_soutenances_candides_admin.html",
                           accueil="accueil_admin",
                           title="Liste soutenances sans candide",
                           personne=admin,
                           resultats=resultats)


if __name__ == "__main__":
    app.run()
