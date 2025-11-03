DROP TABLE IF EXISTS STAGE;
DROP TABLE IF EXISTs DEMARCHE;
DROP TABLE IF EXISTS ENTREPRISE;

CREATE TABLE ENTREPRISE (
    id_entreprise PRIMARY KEY,
    nom_entreprise VARCHAR(200) NOT NULL,
    secteur VARCHAR(200) NOT NULL,
    adresse VARCHAR(300) NOT NULL,
    type VARCHAR(100) NOT NULL,
    tel_entreprise VARCHAR(20),
    email_entreprise VARCHAR(200)
);

CREATE TABLE DEMARCHE (
    id_demarche PRIMARY KEY,
    source VARCHAR(300) NOT NULL,
    type VARCHAR(100) NOT NULL,
    situation VARCHAR(300) NOT NULL,
    date_envoi DATE NOT NULL,
    date_relance DATE,
    resultat VARCHAR(300),
    raison_refus VARCHAR(300),
    cv VARCHAR(200),
    lettre_motiv VARCHAR(200),
    id_entreprise INTEGER,
    id_etudiant INTEGER,
);

CREATE TABLE STAGE (
    id_stage INTEGER PRIMARY KEY,
    typeS VARCHAR(100) NOT NULL,
    duree INTEGER NOT NULL,
    date_debut DATE NOT NULL,
    sujet VARCHAR(300) NOT NULL,
    descriptionS VARCHAR(500),
    competence VARCHAR(200),
    revenu DECIMAL(10,2),
    id_demarche INTEGER,
);



ALTER TABLE DEMARCHE ADD FOREIGN KEY (id_entreprise) REFERENCES ENTREPRISE(id_entreprise);
ALTER TABLE DEMARCHE ADD FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT(id_etudiant);
ALTER TABLE STAGE ADD FOREIGN KEY (id_demarche) REFERENCES DEMARCHE(id_demarche);
