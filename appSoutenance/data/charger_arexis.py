import csv
from datetime import datetime
import mariadb

# ----------------------------
# Fonction pour convertir les dates
# ----------------------------
def convert_date(d):
    if d:
        try:
            return datetime.strptime(d, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return None  # ou une date par défaut si nécessaire
    return None

# ----------------------------
# Connexion à MariaDB
# ----------------------------
conn = mariadb.connect(
    user="root",
    password="hachelef",
    host="localhost",
    database="appsoutenance"
)
cur = conn.cursor()

# ----------------------------
# Lecture du CSV
# ----------------------------
with open("arexis_donnees.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            # ----------------------------
            # ENTREPRISE
            # ----------------------------
            nom_entreprise = row["lib_import"].strip()
            cur.execute("SELECT id_entreprise FROM ENTREPRISE WHERE nom_entreprise=%s", (nom_entreprise,))
            res = cur.fetchone()
            if res:
                id_entreprise = res[0]
            else:
                adresse = f"{row['service_adm_adr1_service']} {row['service_adm_adr2_service']}".strip()
                cur.execute("""
                    INSERT INTO ENTREPRISE (nom_entreprise, secteur, adresse, code_postal, ville)
                    VALUES (%s,%s,%s,%s,%s)
                """, (nom_entreprise, row["service_adm_nom_service"], adresse,
                      row["service_adm_cp_service"], row["service_adm_ville_service"]))
                id_entreprise = cur.lastrowid

            # ----------------------------
            # ETUDIANT
            # ----------------------------
            email = row["mail_perso"] or row["mail_etu"]
            cur.execute("SELECT id_etudiant FROM ETUDIANT WHERE email_etudiant=%s", (email,))
            res = cur.fetchone()
            if res:
                id_etudiant = res[0]
            else:
                date_naissance = convert_date("01/01/2000")  # Valeur par défaut
                cur.execute("""
                    INSERT INTO ETUDIANT (civilite_etudiant, nom_etudiant, prenom_etudiant,
                                          telephone_etudiant, email_etudiant, date_naissance)
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    row["civilite_stagiaire"], row["nom_stagiaire"], row["prenom_stagiaire"],
                    row["tel_perso"], email, date_naissance
                ))
                id_etudiant = cur.lastrowid

            # ----------------------------
            # PROMO
            # ----------------------------
            nom_promo = "BUT RT"
            annee_promo = 2025
            cur.execute("SELECT 1 FROM PROMO WHERE nom_promo=%s AND annee_promo=%s", (nom_promo, annee_promo))
            if not cur.fetchone():
                cur.execute("""
                    INSERT INTO PROMO (nom_promo, annee_promo, formation_promo, id_enseignant)
                    VALUES (%s,%s,%s,%s)
                """, (nom_promo, annee_promo, "Réseaux et Télécoms", None))

            # ----------------------------
            # MAITRE_STAGE
            # ----------------------------
            email_maitre = row["mail_employe_tut"]
            cur.execute("SELECT id_maitre FROM MAITRE_STAGE WHERE email_maitre=%s", (email_maitre,))
            res = cur.fetchone()
            if res:
                id_maitre = res[0]
            else:
                tel_maitre = row["tel_employe_tut"] or row["gsm_employe_tut"]
                cur.execute("""
                    INSERT INTO MAITRE_STAGE (civilite_maitre, nom_maitre, prenom_maitre, tel_maitre, email_maitre, id_entreprise)
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (
                    row["civilite_employe_tut"], row["nom_employe_tut"], row["prenom_employe_tut"],
                    tel_maitre, email_maitre, id_entreprise
                ))
                id_maitre = cur.lastrowid

            # ----------------------------
            # DEMARCHE
            # ----------------------------
            cur.execute("""
                INSERT INTO DEMARCHE (source, typeD, situation, date_envoi, id_entreprise, id_etudiant)
                VALUES (%s,%s,%s,CURDATE(),%s,%s)
            """, ("import_csv", "stage", "valide", id_entreprise, id_etudiant))
            id_demarche = cur.lastrowid

            # ----------------------------
            # STAGE
            # ----------------------------
            date_debut = convert_date(row["dtdeb_stage"])
            date_fin = convert_date(row["dtfin_stage"])
            cur.execute("""
                INSERT INTO STAGE (typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                "obligatoire", date_debut, date_fin, row["duree"], row["unite_duree"],
                row["titre_stage"], row["theme_stage"], id_maitre, id_demarche
            ))
            id_stage = cur.lastrowid

            # ----------------------------
            # APPARTENIR
            # ----------------------------
            cur.execute("""
                INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant)
                VALUES (%s,%s,%s,%s)
                ON DUPLICATE KEY UPDATE regime_etudiant=VALUES(regime_etudiant)
            """, (
                id_etudiant, nom_promo, annee_promo, row["intitule_regime_inscription"]
            ))

            # Commit après chaque ligne pour éviter de perdre tout le CSV en cas d’erreur
            conn.commit()

        except Exception as e:
            print("❌ Erreur ligne CSV :", row)
            print(e)
            conn.rollback()

cur.close()
conn.close()
print("✅ Import CSV terminé !")
