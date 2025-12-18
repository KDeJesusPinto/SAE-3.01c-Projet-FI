from collections import defaultdict
from datetime import datetime
from .app import app
from flask import render_template, request, url_for, redirect, flash
from appSoutenance.models import db,  Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer
from sqlalchemy import desc, distinct
from .importer_csv import importer_etudiants_stages, importer_entreprises
from flask_login import login_user, logout_user, login_required, current_user
from appSoutenance.forms import *
from sqlalchemy import extract
from flask import request, render_template, redirect, url_for
from datetime import datetime, timedelta




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




@app.route('/admin/', methods=['GET', 'POST'])
@login_required
def accueil_admin():
    unForm = ImportForm()
    admin = current_user


    if unForm.validate_on_submit():
        file_storage = unForm.ficCSV.data
        type_import = unForm.type_import.data
       
        if type_import == 'etudiants_stages':
            success, message = importer_etudiants_stages(file_storage)
        elif type_import == 'entreprises':
            success, message = importer_entreprises(file_storage)
        else:
            success = False
            message = "Type d'importation inconnu."

        if success:
            flash(f"Importation réussie : {message}", 'success')
        else:
            flash(f"Échec de l'importation : {message}", 'danger')
        return redirect(url_for('accueil_admin'))




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
        nb_soutenances_attente_candide=nb_soutenances_attente_candide,
        createForm = unForm)


MOIS = {
    1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 5: 'Mai', 6: 'Juin',
    7: 'Juil', 8: 'Août', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
}


@app.route('/admin/planning/')
def planning_admin():

    args = request.args
    annee_promo = args.get('annee_promo', '')
    formation_promo = args.get('formation_promo', '')
    date_soutenance = args.get('date_soutenance', '')
    heure_soutenance = args.get('heure_soutenance', '')
    jury_enseignant_id = args.get('jury_enseignant_id', '')

    dates_disponibles_dt = db.session.query(distinct(Soutenance.dateS)).order_by(Soutenance.dateS).all()
    dates_disponibles = [f"{d[0].day} {MOIS[d[0].month]}" for d in dates_disponibles_dt]
    heures_disponibles = db.session.query(distinct(Soutenance.h_debut)).order_by(Soutenance.h_debut).all()
    heures_disponibles = [h[0] for h in heures_disponibles]
    enseignants_disponibles = Enseignant.query.order_by(Enseignant.nom_enseignant).all()
    query = Soutenance.query.order_by(Soutenance.dateS, Soutenance.h_debut)

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
                regroupement[cle_regroupement] = {
                    'dateS': date_formatee,
                    'h_debut': soutenance.h_debut,
                    'salle': soutenance.salle,
                    'jury_noms': membres_jury_noms,
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
                           enseignants_disponibles = enseignants_disponibles)

HEURE= {
    1: '08:00', 2: '09:00', 3: '10:00', 4: '11:00', 5: '12:00', 6: '13:00',
    7: '14:00'
}

@app.route('/admin/planning/creation_soutenance/', methods=['GET'])
def creation_soutenance():

    createForm = FormSoutenance()

    date_sel = request.args.get('dateS')
    heure_sel = request.args.get('h_debut')
    salle_sel = request.args.get('salle')

    ens_ids = [request.args.get(f'ens{i}') for i in range(1, 4)]
    etu_ids = [request.args.get(f'etu{i}') for i in range(1, 4)]

    etudiants_par_tuteur = [[] for _ in range(3)]
    ens_sel = [None] * 3
    etu_sel = [None] * 3 #COMMENT PK ETU_SEL*3

    if date_sel:
        try:
            annee_sout = int(date_sel.split('-')[0])
            deja_planifies = db.session.query(Demarche.id_etudiant).join(
                Stage, Stage.id_demarche == Demarche.id_demarche
            ).join(
                Soutenance, Soutenance.id_stage == Stage.id_stage
            ).filter(extract('year', Soutenance.dateS) == annee_sout).all()
            
            ids_exclus = [r[0] for r in deja_planifies]
            
            for i in range(3):
                if ens_ids[i] and ens_ids[i].strip():
                    ens_sel[i] = Enseignant.query.get(int(ens_ids[i]))
                    
                    query = db.session.query(Etudiant).join(Tutorer).filter(
                        Tutorer.id_enseignant == int(ens_ids[i])
                    )
                    if ids_exclus:
                        query = query.filter(~Etudiant.id_etudiant.in_(ids_exclus))
                    etudiants_par_tuteur[i] = query.all()

                if etu_ids[i] and etu_ids[i].strip():
                    etu_sel[i] = Etudiant.query.get(int(etu_ids[i]))
                    
        except Exception as e:
            print(f"Erreur de traitement : {e}")

    tous_les_enseignants = Enseignant.query.all()


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
def valider_jury():
    dateS = request.form.get('dateS')
    heure_sel = request.form.get('h_debut')
    salle_sel = request.form.get('salle')
    h_fin_calc = ""
    if heure_sel:
        try:
            start_dt = datetime.strptime(heure_sel, '%H:%M')
            h_fin_calc = (start_dt + timedelta(minutes=45)).strftime('%H:%M')
        except:
            h_fin_calc = "12:00"

    try:
        id_etu_principal = None
        for i in range(1, 4):
            val = request.form.get(f'etu{i}')
            if val and val.strip():
                id_etu_principal = val
                break
        
        if id_etu_principal:
            stage = db.session.query(Stage).join(Demarche).filter(
                Demarche.id_etudiant == id_etu_principal
            ).first()
            
            if stage:
                existante = Soutenance.query.filter_by(id_stage=stage.id_stage).first()
                if existante:
                    print(f"Le stage {stage.id_stage} a déjà une soutenance !")
                    return redirect(url_for('planning_admin'))
                
                date_obj = datetime.strptime(dateS, '%Y-%m-%d').date()
                nouvelle_sout = Soutenance(
                    salle=int(salle_sel) if salle_sel else 0, 
                    dateS=date_obj, 
                    h_debut=heure_sel, 
                    h_fin=h_fin_calc, 
                    id_stage=stage.id_stage,
                    nom_bat="" 
                )
                db.session.add(nouvelle_sout)
                db.session.flush()

                for i in range(1, 4):
                    id_ens = request.form.get(f'ens{i}')
                    if id_ens and id_ens.strip():
                        jury = Composer(
                            id_enseignant=int(id_ens), 
                            id_soutenance=nouvelle_sout.id_soutenance
                        )
                        db.session.add(jury)
                
                db.session.commit()
                print("Insertion réussie !")
                
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de la validation : {e}")
    
    return redirect(url_for('planning_admin'))

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


