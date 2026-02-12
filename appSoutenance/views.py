from collections import defaultdict
from .app import app, db
from flask import jsonify, render_template, request, url_for, redirect, flash
from appSoutenance.models import db,  Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer, MaitreStage, Entreprise, Admini, Jury
from sqlalchemy import desc, asc, distinct, func
from .importer_csv import importer_etudiants_stages, importer_entreprises
from flask_login import login_user, logout_user, login_required, current_user
from appSoutenance.forms import *
from sqlalchemy import extract,desc, distinct, or_
from flask import request, render_template, redirect, url_for
from datetime import datetime, timedelta
from .models import db




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
@login_required
def demarches():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
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
@login_required
def info_stage():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/info_stage_valide.html", accueil="accueil_etudiant", personne=etudiant, title="Mon stage")


@app.route('/etudiant/demarches/new1/')
@login_required
def nouvelle_demarche1():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche1.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")


@app.route('/etudiant/demarches/new2/')
@login_required
def nouvelle_demarche2():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche2.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")


@app.route('/etudiant/demarches/new3/')
@login_required
def nouvelle_demarche3():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche3.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")


@app.route('/etudiant/demarches/resume/')
@login_required
def resume_demarche_etudiant():
    etudiant = current_user
    if not isinstance(etudiant, Etudiant):
        flash("Accès réservé aux étudiants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/resume_demarche.html", accueil="accueil_etudiant", personne=etudiant, title="Résumé de la démarche")


########################## POUR LES ENSEIGNANTS ##########################




@app.route('/enseignant/')
@login_required
def accueil_enseignant():
    enseignant=current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))

    num_personne=current_user.id_enseignant
    queryListeTutore=Etudiant.query.join(Tutorer,Etudiant.id_etudiant==Tutorer.id_etudiant).filter(Tutorer.id_enseignant==num_personne)
    query_soutenance_prevue=Soutenance.query.distinct(Soutenance.id_soutenance).join(Composer,Composer.id_soutenance==Soutenance.id_soutenance).filter(Composer.id_enseignant==num_personne)

    res_tutore = []
    res_soutenance=[]

    for etudiant in queryListeTutore:
        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant).order_by(desc(Demarche.date_envoi)).first()
        soutenance_prevue_tutore=Soutenance.query.join(Stage,Stage.id_stage==Soutenance.id_stage).join(Demarche,Demarche.id_demarche==Stage.id_demarche).join(Etudiant,Etudiant.id_etudiant==Demarche.id_etudiant).filter(Etudiant.id_etudiant==etudiant.id_etudiant).first()
        res_tutore.append({'etudiant':etudiant,'etat':derniere_demarche.situation if derniere_demarche else "Aucune",'soutenance_tutore':soutenance_prevue_tutore})
        
    for soutenance in query_soutenance_prevue.distinct():
        print(soutenance)
        res_soutenance.append({'soutenance':soutenance,'date':soutenance.dateS,'heure':soutenance.h_debut,'salle':soutenance.salle})
    date_soute=query_soutenance_prevue.distinct(Soutenance.dateS)
    res_date=[]
    for date in date_soute:
        if date.dateS not in res_date:
            res_date.append(date.dateS)
    print(res_date)
    enseignant = current_user
    nb_soutenance_place=query_soutenance_prevue.count()
    nb_soutenance_place_tutore=queryListeTutore.count()
    


    return render_template("enseignant/accueil_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Accueil",liste_tutore=res_tutore,liste_soutenance=res_soutenance,date_soute=res_date,nb_sout_place=nb_soutenance_place)


@app.route('/enseignant/planning/')
@login_required
def planning_enseignant():
    enseignant=current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))
    
    return render_template("enseignant/planning_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Planning enseignant")


MOIS = {
    1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 5: 'Mai', 6: 'Juin',
    7: 'Juil', 8: 'Août', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
}


@app.route('/enseignant/soutenances/')
@login_required
def soutenance_enseignant():
    enseignant=current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))

    ##Filtre:
    args = request.args
    annee_promo = args.get('annee_promo', '')
    formation_promo = args.get('formation_promo', '')
    date_soutenance = args.get('date_soutenance', '')
    heure_soutenance = args.get('heure_soutenance', '')
    jury_enseignant_id = args.get('jury_enseignant_id', '')

    num_personne = request.args.get('num_personne')
    enseignant = current_user

    query = Soutenance.query.order_by(Soutenance.dateS, Soutenance.h_debut)
    dates_disponibles_dt = db.session.query(distinct(Soutenance.dateS)).order_by(Soutenance.dateS).all()
    # Conversion au format string lisible (ex: 25 Mar)
    dates_disponibles = [f"{d[0].day} {MOIS[d[0].month]}" for d in dates_disponibles_dt]


    heures_disponibles = db.session.query(distinct(Soutenance.h_debut)).order_by(Soutenance.h_debut).all()
    heures_disponibles = [h[0] for h in heures_disponibles]


    # 1. Filtrer par Jour (date)
    if date_soutenance:
        pass
    if heure_soutenance:
        query = query.filter(Soutenance.h_debut == heure_soutenance)
    if jury_enseignant_id:
        query = query.join(Composer, Soutenance.id_soutenance == Composer.id_soutenance) \
                     .filter(Composer.id_enseignant == jury_enseignant_id)
       
    if annee_promo or formation_promo:
 
        subquery_stages = db.session.query(Stage.id_stage) \
                              .join(Demarche, Stage.id_demarche == Demarche.id_demarche) \
                              .join(Etudiant, Demarche.id_etudiant == Etudiant.id_etudiant) \
                              .join(Entreprise,Entreprise.id_entreprise==Demarche.id_entreprise) \
                              .join(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant)
        if annee_promo:
            subquery_stages = subquery_stages.filter(Appartenir.nom_promo == annee_promo)
        if formation_promo:
            subquery_stages = subquery_stages.filter(Appartenir.formation_promo == formation_promo)


        query = query.filter(Soutenance.id_stage.in_(subquery_stages))

    lesSoutenances = query.all()
    regroupement = {}

    for soutenance in lesSoutenances:
        stage = Stage.query.get(soutenance.id_stage)

        entreprise_stage = None

        etudiant_lie = None
        if stage and stage.demarche:
            etudiant_lie = stage.demarche.etudiant
       
        enseignants_jury = db.session.query(Enseignant).join(Composer).filter(Composer.id_soutenance == soutenance.id_soutenance).all()
        membres_jury_noms =', '.join( [f"{e.nom_enseignant} {e.prenom_enseignant}" for e in enseignants_jury])


        if not membres_jury_noms:
            membres_jury_noms = "Jury non assigné"


        if etudiant_lie:
            jour_mois = soutenance.dateS.day
            mois_francais = MOIS[soutenance.dateS.month]
            date_formatee = f"{jour_mois} {mois_francais}"

            

            cle_regroupement = f"{soutenance.dateS.strftime('%Y-%m-%d')}-{soutenance.h_debut}-{soutenance.salle}-{membres_jury_noms}"
           
            if cle_regroupement not in regroupement:
                # Si la clé n'existe pas, créer une nouvelle entrée (le "bloc")
                regroupement[cle_regroupement] = {
                    'dateS': date_formatee,
                    'h_debut': soutenance.h_debut,
                    'salle': soutenance.salle,
                    'jury_noms': membres_jury_noms,
                    'stages': []  # Initialiser la liste des stages/étudiants
                }

            if stage and stage.demarche:
                entreprise_stage=stage.demarche.entreprise


            # Ajouter l'étudiant/stage à la liste 'stages' de ce bloc
            regroupement[cle_regroupement]['stages'].append({
                'nom_etudiant': etudiant_lie.nom_etudiant,
                'prenom_etudiant': etudiant_lie.prenom_etudiant,
                'titre_stage': stage.titre_stage if stage else "Titre de stage non trouvé",
                'nom_entreprise': entreprise_stage.nom_entreprise if entreprise_stage else "entreprise non trouvé"
            })      

    resultats_regroupes = list(regroupement.values())
    return render_template("enseignant/soutenance_enseignant.html",
                           accueil="accueil_enseignant",personne=enseignant,
                           heures_disponibles = heures_disponibles,
                           title="soutenance", resultats = resultats_regroupes)





@app.route('/enseignant/liste+etu/')
@login_required
def liste_etu_enseignant():

    num_personne = request.args.get('num_personne')
    enseignant=current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))
    
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
    return render_template("enseignant/lst_etudiants_enseignant.html", accueil="accueil_enseignant", title="Liste des étudiants",resultats=res, personne=enseignant)



@app.route('/enseignant/liste+etu/etudiant/')
@login_required
def detail_etudiant_ens():
    enseignant=current_user
    if not isinstance(enseignant, Enseignant):
        flash("Accès réservé aux enseignants.", "warning")
        return redirect(url_for("login"))
    
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    return render_template("admin/detail_etudiant_ens.html", accueil="accueil_enseignant", personne=enseignant, title="Detail de l'etudiant")


########################## POUR LES ADMINISTRATEURS ##########################




@app.route('/admin/', methods=['GET', 'POST'])
@login_required
def accueil_admin():
    """Page d'accueil pour les administrateurs"""

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
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

    requete_les_etudiants = Etudiant.query.outerjoin(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant).outerjoin(Promo, (Appartenir.nom_promo == Promo.nom_promo) & (Appartenir.annee_promo == Promo.annee_promo))

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
                                                     .join(Soutenance, Stage.id_stage == Soutenance.id_stage)\
                                                     .join(Tutorer, Etudiant.id_etudiant == Tutorer.id_etudiant)
    nb_soutenances_posees = requete_soutenances.with_entities(Soutenance.id_soutenance).distinct().count()
    nb_tuteurs = db.session.query(Tutorer.id_enseignant).distinct().count()

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
        nb_tuteurs=nb_tuteurs,
        createForm = unForm)


MOIS = {
    1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 5: 'Mai', 6: 'Juin',
    7: 'Juil', 8: 'Août', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
}


@app.route('/admin/planning/')
@login_required
def planning_admini():
    """Page de planning pour les administrateurs"""

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
    elif tri == "DateDesc":
        query = query.order_by(desc(Soutenance.dateS), desc(Soutenance.h_debut))
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


            cle_regroupement = f"{soutenance.dateS.strftime('%Y-%m-%d')}-{soutenance.h_debut}-{soutenance.h_fin}-{soutenance.salle}-{membres_jury_noms}"
           
            if cle_regroupement not in regroupement:
                regroupement[cle_regroupement] = {
                    'id_soutenance': soutenance.id_soutenance,
                    'dateS': date_formatee,
                    'h_debut': soutenance.h_debut,
                    'h_fin': soutenance.h_fin,
                    'salle': soutenance.salle,
                    'jury_noms': membres_jury_noms,
                    'nom_promo': promo_etudiant,
                    'stages': []
                }
            regroupement[cle_regroupement]['stages'].append({
                'nom_etudiant': etudiant_lie.nom_etudiant,
                'prenom_etudiant': etudiant_lie.prenom_etudiant,
                'titre_stage': stage.titre_stage if stage else "Titre de stage non trouvé",
                'nom_entreprise': stage.demarche.entreprise.nom_entreprise if stage else "Entreprise non trouvée",
                'nom_maitre': stage.maitre_stage.prenom_maitre + " " + stage.maitre_stage.nom_maitre if stage and stage.maitre_stage else "Maître de stage non trouvé   "
            })

    resultats_regroupes = list(regroupement.values())
    return render_template("admin/planning_admin.html",
                           accueil="accueil_admin",
                           title="Planning", resultats = resultats_regroupes,
                           heures_disponibles = heures_disponibles,
                           enseignants_disponibles = enseignants_disponibles,
                           dates_disponibles = dates_disponibles,
                           soutenance = regroupement)


HEURE= {
    1: '08:00', 2: '09:00', 3: '10:00', 4: '11:00', 5: '12:00', 6: '13:00',
    7: '14:00'
}




@app.route('/admin/planning/<int:id>/')
@login_required
def detail_soutenance_admin(id):
    """Page de détail d'une soutenance pour les administrateurs


    Args:
        id (int): l'identifiant de la soutenance
    """


    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
   
    soutenance = Soutenance.query.get(id)
    if not soutenance:
        flash("Soutenance introuvable.", "danger")
        return redirect(url_for('planning_admini'))
   
    soutenances_groupe = Soutenance.query.filter_by(
        dateS=soutenance.dateS,
        h_debut=soutenance.h_debut,
        salle=soutenance.salle
    ).all()

    enseignants_jury = db.session.query(Enseignant)\
            .join(Composer)\
            .filter(Composer.id_soutenance == id)\
            .all()

    deleteForm = FormSoutenance()

    return render_template("/admin/detail_soutenance_admin.html",
                           accueil="accueil_admin",
                           title="Détail de la soutenance",
                           soutenance = soutenance,
                           soutenances_groupe = soutenances_groupe,
                           enseignants_jury = enseignants_jury,
                           deleteForm = deleteForm)


@app.route('/admin/planning/<int:id>/update')
@login_required
def modifier_soutenance_admin(id):
    uneSoutenance = Soutenance.query.get(id)
    compose = Composer.query.filter_by(id_soutenance=id).all()
    jury_actuel_id = [int(c.id_enseignant) for c in compose]
    
    etu_actuels_id = []
    for s in Soutenance.query.filter_by(
            dateS=uneSoutenance.dateS,
            h_debut=uneSoutenance.h_debut,
            salle=uneSoutenance.salle
        ).all():
        if s.stage and s.stage.demarche and s.stage.demarche.etudiant:
            etu_actuels_id.append(s.stage.demarche.etudiant.id_etudiant)

    return render_template(
        "admin/update_soutenance.html",
        uneSoutenance=uneSoutenance,
        jury_actuel_id=jury_actuel_id,
        etu_actuels_id=etu_actuels_id
    )




@app.route('/admin/planning/<int:id>/update/save', methods=("POST",))
@login_required
def save_soutenance_admin(id):
    soutenance = Soutenance.query.get(id)
    if not soutenance:
        flash("Soutenance introuvable.", "danger")
        return redirect(url_for('planning_admini'))

    date_str = request.form.get('dateS')
    heure_str = request.form.get('h_debut')
    salle = request.form.get('salle')

    # strptime pour convertir la date (string) au format date
    if date_str:
        soutenance.dateS = datetime.strptime(date_str, "%Y-%m-%d").date()

    if heure_str:
        soutenance.h_debut = heure_str
    
    soutenance.salle =salle

    Composer.query.filter_by(id_soutenance=id).delete()

    for i in range(1, 4):
        id_ens = request.form.get(f'ens{i}')
        if id_ens and id_ens.strip():
            try:
                comp = Composer(id_enseignant=int(id_ens), id_soutenance=soutenance.id_soutenance)
                db.session.add(comp)
            except ValueError:
                pass

    try:
        db.session.commit()
        flash("Soutenance mise à jour avec succès !", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la mise à jour : {e}", "danger")

    return redirect(url_for('planning_admini'))


@app.route('/api/enseignants_disponibles/<int:id_soutenance>')
@login_required
def api_enseignants_disponibles(id_soutenance):
    date_s = request.args.get('date')
    heure_s = request.args.get('heure')
    

    occupes = db.session.query(Composer.id_enseignant).join(Soutenance).filter(
            Soutenance.dateS == date_s,
            Soutenance.h_debut == heure_s,
            Soutenance.id_soutenance != id_soutenance
        ).all()

    ids_occupes = [o[0] for o in occupes]
    jury_actuel = db.session.query(Composer.id_enseignant).filter(Composer.id_soutenance == id_soutenance).all()
    ids_jury_actuel = [j[0] for j in jury_actuel]
    ids_a_exclure = [id_ens for id_ens in ids_occupes if id_ens not in ids_jury_actuel]
    dispos = Enseignant.query.filter(~Enseignant.id_enseignant.in_(ids_a_exclure)).all()

    return jsonify([
        {
            'id': int(e.id_enseignant),
            'nom': e.nom_enseignant,
            'prenom': e.prenom_enseignant
        }
        for e in dispos
    ])


@app.route('/api/etudiants_par_tuteur/<int:id_enseignant>/<int:id_soutenance>')
@login_required
def api_etudiants_par_tuteur(id_enseignant, id_soutenance):
    query = db.session.query(Etudiant).join(Tutorer).filter(Tutorer.id_enseignant == id_enseignant)
    query = query.join(Demarche).filter(Demarche.situation == 'Acceptée').join(Stage, Demarche.id_demarche == Stage.id_demarche).outerjoin(Soutenance, Stage.id_stage == Soutenance.id_stage)
    #query = query.filter(or_(Soutenance.id_soutenance == None, Soutenance.id_soutenance == id_soutenance)).distinct()  
    query = query.filter((Soutenance.id_soutenance == None) | (Soutenance.id_soutenance == id_soutenance)).distinct()  
    etudiants = query.all()

    return jsonify([
        {'id': int(etu.id_etudiant), 'nom': etu.nom_etudiant, 'prenom': etu.prenom_etudiant} 
        for etu in etudiants
    ])


@app.route('/api/salle_disponible/')
@login_required
def api_salle_disponible(id_soutenance):
    date_s = request.args.get('date')
    heure_s = request.args.get('heure')
    salle_s = request.args.get('salle')
    if not date_s or not heure_s or not salle_s:
        return jsonify({'disponible': True})



@app.route('/admin/planning/<int:id>/delete')
@login_required
def suppression_soutenance_admin(id):
    uneSoutenance = Soutenance.query.get(id)
    soutenances_groupe = Soutenance.query.filter_by(
        dateS=uneSoutenance.dateS,
        h_debut=uneSoutenance.h_debut,
        salle=uneSoutenance.salle
    ).all()

    compose = Composer.query.filter_by(id_soutenance=id).all()
    unForm = FormSoutenance(id_soutenance = uneSoutenance.id_soutenance, id_stage =uneSoutenance.id_stage,
                            h_debut=uneSoutenance.h_debut, dateS=uneSoutenance.dateS, salle=uneSoutenance.salle,
                            nom_enseignant1 = compose[0].enseignant if len(compose) > 0 else None,
                            nom_enseignant2 = compose[1].enseignant if len(compose) > 1 else None,
                            nom_enseignant3 = compose[2].enseignant if len(compose) > 2 else None)
    return render_template("admin/supprimer_soutenance_admin.html", accueil="accueil_admin", title="Supprimer la soutenance", deleteForm=unForm, uneSoutenance=uneSoutenance, soutenances_groupe=soutenances_groupe)

@app.route('/admin/planning/<int:id>/erase', methods=("POST",))
@login_required
def erase_soutenance_admin(id):
    soutenance = Soutenance.query.get(id)
    if not soutenance:
        flash("Soutenance introuvable.", "danger")
        return redirect(url_for('planning_admini'))

    try:
        soutenances_to_delete = Soutenance.query.filter_by(
            dateS=soutenance.dateS,
            h_debut=soutenance.h_debut,
            salle=soutenance.salle
        ).all()

        for s in soutenances_to_delete:
            Jury.query.filter_by(id_soutenance=s.id_soutenance).delete()
            Composer.query.filter_by(id_soutenance=s.id_soutenance).delete()
            db.session.delete(s)
            
        db.session.commit()
        flash("Soutenances supprimées avec succès !", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la suppression : {e}", "danger")
    return redirect(url_for('planning_admini'))


@app.route('/admin/planning/creation_soutenance/', methods =["GET", "POST"])
@login_required
def creation_soutenance():
    """Page de création de soutenance pour les administrateurs"""

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    createForm = FormSoutenance()

    date_sel = request.args.get('dateS')
    heure_sel = request.args.get('h_debut')
    salle_sel = request.args.get('salle', '')

    ens_ids = [request.args.get(f'ens{i}','') for i in range(1, 4)]
    etu_ids = [request.args.get(f'etu{i}','') for i in range(1, 4)]

    etudiants_par_tuteur = [[] for _ in range(3)]
    ens_sel = [None] * 3
    etu_sel = [None] * 3

    if date_sel:
        try:
            createForm.dateS.data = datetime.strptime(date_sel, '%Y-%m-%d').date()
            
            #ids_exclus = [r[0] for r in deja_planifies]
            
            for i in range(3):
                if ens_ids[i] and ens_ids[i].strip():
                    ens_sel[i] = Enseignant.query.get(int(ens_ids[i]))
                    
                    query = db.session.query(Etudiant).join(Tutorer).filter(
                        Tutorer.id_enseignant == int(ens_ids[i])
                    )
                    # query = query.join(Demarche).filter(Demarche.situation == 'Acceptée').distinct()
                    # if ids_exclus:
                    #     query = query.filter(~Etudiant.id_etudiant.in_(ids_exclus))
                    query = query.join(Demarche).filter(Demarche.situation == 'Acceptée')\
                                 .join(Stage, Demarche.id_demarche == Stage.id_demarche)\
                                 .outerjoin(Soutenance, Stage.id_stage == Soutenance.id_stage)\
                                 .filter(Soutenance.id_soutenance == None)\
                                 .distinct()
                    etudiants_par_tuteur[i] = query.all()

                if etu_ids[i] and etu_ids[i].strip():
                    etu_sel[i] = Etudiant.query.get(int(etu_ids[i]))
                    
        except Exception as e:
            print(f"Erreur de traitement : {e}")    

    query_enseignants = Enseignant.query
    if date_sel and heure_sel:
        enseignants_occupes = db.session.query(Composer.id_enseignant)\
            .join(Soutenance, Composer.id_soutenance == Soutenance.id_soutenance)\
            .filter(Soutenance.dateS == date_sel, Soutenance.h_debut == heure_sel)
        query_enseignants = query_enseignants.filter(Enseignant.id_enseignant.notin_(enseignants_occupes))

    tous_les_enseignants = query_enseignants.all()

    return render_template(
        'admin/creation_soutenance.html',
        createForm=createForm,
        heure=HEURE.values(),
        enseignants_dispos=tous_les_enseignants,
        etudiants_par_tuteur=etudiants_par_tuteur,
        dateS=date_sel,
        h_debut=heure_sel,
        salle=salle_sel,
        date_sel=date_sel,
        heure_sel=heure_sel,
        ens_ids=ens_ids,
        etu_ids=etu_ids,
        ens_sel=ens_sel,
        etu_sel=etu_sel
    )

@app.route('/soutenance/valider', methods=['POST'])
@login_required
def valider_jury():
    """Valider le jury d'une soutenance et l'insérer en base de données"""
    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    print("--- TENTATIVE D'INSERTION ---")
    print(f"Formulaire reçu : {request.form}")

    dateS = request.form.get('dateS')
    heure_sel = request.form.get('h_debut')
    salle_sel = request.form.get('salle')

    if not salle_sel or not salle_sel.strip():
        flash("Veuillez renseigner une salle.", "danger")
        ens1 = request.form.get('ens1', '')
        ens2 = request.form.get('ens2', '')
        ens3 = request.form.get('ens3', '')
        etu1 = request.form.get('etu1', '')
        etu2 = request.form.get('etu2', '')
        etu3 = request.form.get('etu3', '')
        return redirect(url_for('creation_soutenance', dateS=dateS, h_debut=heure_sel, salle=salle_sel, ens1=ens1, ens2=ens2, ens3=ens3, etu1=etu1, etu2=etu2, etu3=etu3))

    created = 0
    errors = []
    # Utiliser un set pour ne traiter chaque étudiant qu'une seule fois et éviter les doublons
    unique_etu_ids = set()
    for i in range(1, 4):
        id_etu = request.form.get(f'etu{i}')
        if id_etu and id_etu.strip():
            try:
                unique_etu_ids.add(int(id_etu))
            except ValueError:
                errors.append(f"Identifiant étudiant invalide pour le champ etu{i}: {id_etu}")

    if not unique_etu_ids:
        flash("Veuillez sélectionner au moins un étudiant pour créer une soutenance.", "danger")
        ens1 = request.form.get('ens1', '')
        ens2 = request.form.get('ens2', '')
        ens3 = request.form.get('ens3', '')
        return redirect(url_for('creation_soutenance', dateS=dateS, h_debut=heure_sel, salle=salle_sel, ens1=ens1, ens2=ens2, ens3=ens3))

    try:
        date_obj = datetime.strptime(dateS, '%Y-%m-%d').date()
    except Exception:
        flash("Date invalide.", "danger")
        return redirect(url_for('creation_soutenance', dateS=dateS, h_debut=heure_sel, salle=salle_sel))

    if Soutenance.query.filter(Soutenance.dateS == date_obj, Soutenance.h_debut == heure_sel, Soutenance.salle == salle_sel).first():
        flash(f"La salle {salle_sel} est déjà occupée à cette date et heure.", "danger")
        ens1 = request.form.get('ens1', '')
        ens2 = request.form.get('ens2', '')
        ens3 = request.form.get('ens3', '')
        etu1 = request.form.get('etu1', '')
        etu2 = request.form.get('etu2', '')
        etu3 = request.form.get('etu3', '')
        return redirect(url_for('creation_soutenance', dateS=dateS, h_debut=heure_sel, salle=salle_sel, ens1=ens1, ens2=ens2, ens3=ens3, etu1=etu1, etu2=etu2, etu3=etu3))

    for id_etu_int in unique_etu_ids:
        stage = Stage.query.join(Demarche).filter(
            Demarche.id_etudiant == id_etu_int,
            Demarche.situation == 'Acceptée'
        ).first()

        if not stage:
            etudiant = Etudiant.query.get(id_etu_int)
            errors.append(f"Aucun stage validé trouvé pour {etudiant.prenom_etudiant} {etudiant.nom_etudiant}.")
            continue

        # Vérifier si une soutenance existe déjà pour ce stage
        if Soutenance.query.filter_by(id_stage=stage.id_stage).first():
            etudiant = Etudiant.query.get(id_etu_int)
            errors.append(f"Une soutenance existe déjà pour {etudiant.prenom_etudiant} {etudiant.nom_etudiant}.")
            continue

        # Créer une soutenance liée au stage
        nouvelle_sout = Soutenance(
            salle=salle_sel,
            dateS=date_obj,
            h_debut=heure_sel,
            h_fin=(datetime.strptime(heure_sel, '%H:%M') + timedelta(minutes=45)).strftime('%H:%M'),
            id_stage=stage.id_stage,
            nom_bat=""
        )
        db.session.add(nouvelle_sout)
        db.session.flush()

        for j in range(1, 4):
            id_ens = request.form.get(f'ens{j}')
            if id_ens and id_ens.strip():
                try:
                    comp = Composer(id_enseignant=int(id_ens), id_soutenance=nouvelle_sout.id_soutenance)
                    db.session.add(comp)
                except ValueError:
                    pass
        created += 1

    if created == 0:
        db.session.rollback()
        for e in errors:
            flash(e, "warning")
        flash("Aucune soutenance n'a été créée. Veuillez vérifier que les étudiants ont un stage validé.", "danger")
        ens1 = request.form.get('ens1', '')
        ens2 = request.form.get('ens2', '')
        ens3 = request.form.get('ens3', '')
        etu1 = request.form.get('etu1', '')
        etu2 = request.form.get('etu2', '')
        etu3 = request.form.get('etu3', '')
        return redirect(url_for('creation_soutenance', dateS=dateS, h_debut=heure_sel, salle=salle_sel, ens1=ens1, ens2=ens2, ens3=ens3, etu1=etu1, etu2=etu2, etu3=etu3))

    try:
        db.session.commit()
        for e in errors:
            flash(e, "warning")
        flash(f"{created} soutenance(s) ajoutée(s) avec succès !", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de l'insertion : {e}", "danger")

    return redirect(url_for('planning_admini'))

@app.route('/admin/liste+enseignants/<int:id>/')
@login_required
def detail_enseignant(id):
    """Page de détail d'un enseignant pour les administrateurs

    Args:
        id (int): l'identifiant de l'enseignant
    """

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    enseignant = Enseignant.query.get(id)
    tutorats = Tutorer.query.filter_by(id_enseignant=enseignant.id_enseignant).all()
    etudiants_suivis = [t.etudiant for t in tutorats]
    enseignant_promo = Promo.query.filter_by(id_enseignant=enseignant.id_enseignant).first()
    soutenances_jury = Soutenance.query.outerjoin(Composer)\
                        .outerjoin(Stage)\
                        .outerjoin(Demarche)\
                        .outerjoin(Etudiant)\
                        .outerjoin(Tutorer)\
                        .filter((Composer.id_enseignant == enseignant.id_enseignant) | (Tutorer.id_enseignant == enseignant.id_enseignant)).distinct().all()

    liste_soutenances = []
    for s in soutenances_jury:
        etudiant = s.stage.demarche.etudiant
        est_tuteur = Tutorer.query.filter_by(id_enseignant=enseignant.id_enseignant, id_etudiant=etudiant.id_etudiant).first() is not None
        role = "Tuteur" if est_tuteur else "Candide"
        liste_soutenances.append({
            'id': s.id_soutenance,
            'titre': s.stage.titre_stage,
            'role': role
        })

    return render_template("admin/detail_enseignant.html",
                           accueil="accueil_admin",
                           title="Detail de l'enseignant",
                           enseignant=enseignant,
                           etudiants_suivis=etudiants_suivis,
                           enseignant_promo=enseignant_promo,
                           soutenances=liste_soutenances)



@app.route('/admin/liste+etudiants/<int:id>/')
@login_required
def detail_etudiant_admin(id):
    """Page de détail d'un étudiant pour les administrateurs

    Args:
        id (int): l'identifiant de l'étudiant
    """

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

    soutenance = stage_etudiant.soutenance if stage_etudiant else None

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
                           etudiant_soutenance=soutenance,
                           maitre_stage=maitre_stage,
                           entreprise=entreprise)


@app.route('/admin/liste+enseignants/')
@login_required
def liste_ens_admin():
    """Liste des enseignants pour les administrateurs"""
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
        if soutenance == "Soutenance":
            lesEnseignants = lesEnseignants.join(Tutorer)\
                                           .join(Etudiant)\
                                           .join(Demarche)\
                                           .join(Stage)\
                                           .join(Soutenance, Stage.id_stage == Soutenance.id_stage)\
                                           .distinct()
        elif soutenance == "NonSoutenance":
            sq_soutenance = db.session.query(Tutorer.id_enseignant)\
                                      .join(Etudiant)\
                                      .join(Demarche)\
                                      .join(Stage)\
                                      .join(Soutenance, Stage.id_stage == Soutenance.id_stage)
            lesEnseignants = lesEnseignants.join(Tutorer).filter(Enseignant.id_enseignant.notin_(sq_soutenance)).distinct()

    # Récupérer soutenances avec jury non complet : Composer -> Soutenance -> Stage -> 
    # Demarche -> Etudiant -> Tutorer -> Enseignant
    # id de l'étudiant =! de l'id de l'étudiant dont l'enseignant est tuteur
    if candide == 'NonCandide':
        sq = db.session.query(Enseignant.id_enseignant)\
            .join(Composer, Composer.id_enseignant == Enseignant.id_enseignant)\
            .join(Soutenance, Soutenance.id_soutenance == Composer.id_soutenance)\
            .join(Stage, Stage.id_stage == Soutenance.id_stage)\
            .join(Demarche, Demarche.id_demarche == Stage.id_demarche)\
            .join(Etudiant, Etudiant.id_etudiant == Demarche.id_etudiant)\
            .outerjoin(Tutorer, (Tutorer.id_enseignant == Enseignant.id_enseignant)\
                 & (Tutorer.id_etudiant == Etudiant.id_etudiant))\
            .filter(Tutorer.id_enseignant.is_(None))
        lesEnseignants = lesEnseignants.filter(Enseignant.id_enseignant.notin_(sq))


    lesEnseignants = lesEnseignants.all()
    res = []


    for enseignant in lesEnseignants:
        nb_tutore = Tutorer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()

        nb_soutenances = Composer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()
        
        nb_soutenances_en_tuteur = Soutenance.query.join(Stage, Soutenance.id_stage == Stage.id_stage) \
            .join(Demarche, Stage.id_demarche == Demarche.id_demarche) \
            .join(Etudiant, Demarche.id_etudiant == Etudiant.id_etudiant) \
            .join(Tutorer, (Etudiant.id_etudiant == Tutorer.id_etudiant) & (Tutorer.id_enseignant == enseignant.id_enseignant)) \
            .count()

        nb_candide = db.session.query(Soutenance).join(Composer, Soutenance.id_soutenance == Composer.id_soutenance)\
                                                .join(Stage, Soutenance.id_stage == Stage.id_stage)\
                                                .join(Demarche, Stage.id_demarche == Demarche.id_demarche)\
                                                .join(Etudiant, Demarche.id_etudiant == Etudiant.id_etudiant)\
                                                .filter(Composer.id_enseignant == enseignant.id_enseignant, ~Etudiant.tutorats.any(Tutorer.id_enseignant == enseignant.id_enseignant)).count()

        res.append({
            "enseignant": enseignant,
            "nb_tutores": nb_tutore,
            "nb_soutenances": nb_soutenances,
            "nb_soutenances_en_tuteur": nb_soutenances_en_tuteur,
            "nb_candide": nb_candide
        })


    return render_template("admin/lst_enseignants.html",
                           accueil="accueil_admin",
                           title="Liste enseignants",
                           resultats=res)




@app.route('/admin/liste+etudiants/')
@login_required
def liste_etu_admin():
    """Liste des étudiants pour les administrateurs"""

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    annee_filter = request.args.get('annee')
    formation_filter = request.args.get('formation')
    situation_filter = request.args.get('situation')
    regime_filter = request.args.get('regime')
    tri = request.args.get("trier", "Nom") # Par défaut, trié par nom

    requete_les_etudiants = Etudiant.query.outerjoin(Appartenir, Etudiant.id_etudiant == Appartenir.id_etudiant).outerjoin(Promo, (Appartenir.nom_promo == Promo.nom_promo) & (Appartenir.annee_promo == Promo.annee_promo))

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
            'regime': "FI" if appartenance and appartenance.regime_etudiant == "Formation initiale" else ("Apprenti" if appartenance else "N/C"),
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
@app.route('/admin/liste+soutenances+candides/<int:id>/')
@login_required
def liste_soutenances_candides_admin(id=None):
    """Liste des soutenances sans candide pour les administrateurs
    
    Args:
        id (int|None): l'identifiant de l'enseignant
    """

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))

    # IDs des soutenances qui ont un jury complet
    soutenances_jury_complet_ids = db.session.query(Composer.id_soutenance)\
        .group_by(Composer.id_soutenance)\
        .having(func.count(Composer.id_enseignant) >= 2)

    # On récupère toutes les soutenances dont l'ID n'est pas dans la liste des complets
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
                           resultats=resultats,
                           id_enseignant=id)

@app.route('/admin/ajouter_candide/<int:id_ens>/<int:id_sout>/')
@login_required
def ajouter_candide_admin(id_ens, id_sout):
    """Ajouter un enseignant en tant que candide d'une soutenance

    Args:
        id_ens (int): l'identifiant de l'enseignant
        id_sout (int): l'identifiant de la soutenance
    """

    admin = current_user
    if not isinstance(admin, Admini):
        flash("Accès réservé aux administrateurs.", "warning")
        return redirect(url_for("login"))
    
    existe = Composer.query.filter_by(id_enseignant=id_ens, id_soutenance=id_sout).first()
    
    if not existe:
        try:
            nouveau_candide = Composer(id_enseignant=id_ens, id_soutenance=id_sout)
            db.session.add(nouveau_candide)
            db.session.commit()
            flash("Enseignant ajouté au jury avec succès", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de l'ajout : {e}", "danger")
    else:
        flash("Cet enseignant fait déjà partie du jury", "info")
    
    return redirect(url_for('liste_ens_admin'))


if __name__ == "__main__":
    app.run()
