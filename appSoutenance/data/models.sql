DROP TABLE IF EXISTS STAGE;
DROP TABLE IF EXISTS DEMARCHE;
DROP TABLE IF EXISTS ENTREPRISE;
DROP TABLE IF EXISTS ETUDIANT;
DROP TABLE IF EXISTS PROMO;

CREATE TABLE ENTREPRISE (
    id_entreprise INT PRIMARY KEY,
    nom_entreprise VARCHAR(200) NOT NULL,
    secteur VARCHAR(200) NOT NULL,
    adresse VARCHAR(300) NOT NULL,
    typeE VARCHAR(100) NOT NULL,
    tel_entreprise VARCHAR(20),
    email_entreprise VARCHAR(200)
);

CREATE TABLE DEMARCHE (
    id_demarche INT PRIMARY KEY,
    source VARCHAR(300) NOT NULL,
    typeD VARCHAR(100) NOT NULL,
    situation VARCHAR(300) NOT NULL,
    date_envoi DATE NOT NULL,
    date_relance DATE,
    resultat VARCHAR(300),
    raison_refus VARCHAR(300),
    cv VARCHAR(200),
    lettre_motiv VARCHAR(200),
    id_entreprise INT
    -- id_etudiant INT
);

CREATE TABLE STAGE (
    id_stage INT PRIMARY KEY,
    typeS VARCHAR(100) NOT NULL,
    duree INT NOT NULL,
    date_debut DATE NOT NULL,
    sujet VARCHAR(300) NOT NULL,
    descriptionS VARCHAR(500),
    competence VARCHAR(200),
    revenu DECIMAL(10,2),
    id_demarche INT
);

CREATE TABLE ETUDIANT(
    id_etudiant INT PRIMARY KEY,
    nom_etudiant VARCHAR(20) NOT NULL,
    prenom_etudiant VARCHAR(20) NOT NULL,
    date_naissance VARCHAR(20) NOT NULL,
    telephone_etudiant VARCHAR(10),
    email_etudiant VARCHAR(100) 
);

CREATE TABLE PROMO(
    nom_promo VARCHAR(50) PRIMARY KEY,
    annee_promo VARCHAR(20) PRIMARY KEY,
    formation_promo VARCHAR(20)
);


ALTER TABLE DEMARCHE ADD FOREIGN KEY (id_entreprise) REFERENCES ENTREPRISE(id_entreprise);
-- ALTER TABLE DEMARCHE ADD FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT(id_etudiant);
ALTER TABLE STAGE ADD FOREIGN KEY (id_demarche) REFERENCES DEMARCHE(id_demarche);
