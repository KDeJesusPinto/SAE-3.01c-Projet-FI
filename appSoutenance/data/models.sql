DROP TABLE IF EXISTS TUTORER;

DROP TABLE IF EXISTS COMPOSER;

DROP TABLE IF EXISTS ASSEMBLER;

DROP TABLE IF EXISTS JURY;

DROP TABLE IF EXISTS SOUTENANCE;

DROP TABLE IF EXISTS APPARTENIR;

DROP TABLE IF EXISTS STAGE;

DROP TABLE IF EXISTS MAITRE_STAGE;

DROP TABLE IF EXISTS DEMARCHE;

DROP TABLE IF EXISTS PROMO;

DROP TABLE IF EXISTS ETUDIANT;

DROP TABLE IF EXISTS ENSEIGNANT;

DROP TABLE IF EXISTS ENTREPRISE;

DROP TABLE IF EXISTS ADMINI;

CREATE TABLE ENTREPRISE (
  PRIMARY KEY (id_entreprise),
  id_entreprise INT NOT NULL,
  nom_entreprise VARCHAR(200),
  secteur VARCHAR(200),
  ville VARCHAR(100),
  adresse VARCHAR(200),
  code_postal VARCHAR(5),
  typeE VARCHAR(100),
  tel_entreprise VARCHAR(15),
  email_entreprise VARCHAR(200)
);

CREATE TABLE ETUDIANT(
  id_etudiant INT PRIMARY KEY,
  nom_etudiant VARCHAR(100) NOT NULL,
  prenom_etudiant VARCHAR(100) NOT NULL,
  date_naissance DATE NOT NULL,
  civilite_etudiant VARCHAR(10),
  telephone_etudiant VARCHAR(15),
  email_etudiant VARCHAR(200),
  login_etudiant VARCHAR(100),
  pwd_etudiant VARCHAR(100)
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
  id_entreprise INT NOT NULL,
  id_etudiant INT NOT NULL
);

CREATE TABLE MAITRE_STAGE (
  PRIMARY KEY (id_maitre),
  id_maitre INT NOT NULL,
  nom_maitre VARCHAR(100),
  prenom_maitre VARCHAR(100),
  civilite_maitre VARCHAR(10),
  tel_maitre VARCHAR(15),
  email_maitre VARCHAR(200),
  id_entreprise INT NOT NULL
);

CREATE TABLE ENSEIGNANT (
  PRIMARY KEY (id_enseignant),
  id_enseignant INT NOT NULL,
  nom_enseignant VARCHAR(100),
  prenom_enseignant VARCHAR(100),
  civilite_enseignant VARCHAR(10),
  email_enseignant VARCHAR(200),
  login_enseignant VARCHAR(100),
  pwd_enseignant VARCHAR(100)
);

CREATE TABLE STAGE (
  PRIMARY KEY (id_stage),
  id_stage INT NOT NULL,
  typeS VARCHAR(100),
  date_debut DATE NOT NULL,
  date_fin DATE NOT NULL,
  duree_stage INT,
  unite_duree VARCHAR(50),
  titre_stage VARCHAR(2000),
  theme_stage VARCHAR(2000),
  id_maitre INT NULL,
  id_demarche INT NOT NULL,
  UNIQUE (id_demarche)
);

CREATE TABLE PROMO (
  PRIMARY KEY (nom_promo, annee_promo, formation_promo),
  nom_promo VARCHAR(100) NOT NULL,
  annee_promo INT(4) NOT NULL,
  formation_promo VARCHAR(100),
  id_enseignant INT NULL -- Directeur d'études
);

CREATE TABLE JURY (
  PRIMARY KEY (id_jury),
  id_jury INT NOT NULL,
  date_jury DATE NOT NULL,
  h_jury VARCHAR(5),
  duree INT,
  id_soutenance INT NULL,
  UNIQUE (id_soutenance)
);

CREATE TABLE SOUTENANCE (
  PRIMARY KEY (id_soutenance),
  id_soutenance INT NOT NULL,
  salle INT,
  nom_bat VARCHAR(50) NULL,
  dateS DATE,
  h_debut VARCHAR(5),
  h_fin VARCHAR(5) NULL,
  id_stage INT NOT NULL,
  UNIQUE (id_stage)
);

CREATE TABLE TUTORER (
  PRIMARY KEY (id_enseignant, id_etudiant),
  id_enseignant INT NOT NULL,
  id_etudiant INT NOT NULL,
  annee INT(4)
);

CREATE TABLE COMPOSER (
  PRIMARY KEY (id_enseignant, id_soutenance),
  id_enseignant INT NOT NULL,
  id_soutenance INT NOT NULL
);

CREATE TABLE APPARTENIR (
  PRIMARY KEY (id_etudiant, nom_promo, annee_promo),
  id_etudiant INT NOT NULL,
  nom_promo VARCHAR(100) NOT NULL,
  annee_promo INT(4) NOT NULL,
  regime_etudiant VARCHAR(100)
);

CREATE TABLE ADMINI (
  PRIMARY KEY (id_admin),
  id_admin VARCHAR(42) NOT NULL,
  nom_admin VARCHAR(100),
  prenom_admin VARCHAR(100),
  login_admin VARCHAR(100),
  pwd_admin VARCHAR(100)
);

CREATE TABLE ASSEMBLER (
  PRIMARY KEY (id_jury, id_admin),
  id_jury VARCHAR(42) NOT NULL,
  id_admin VARCHAR(42) NOT NULL
);

ALTER TABLE APPARTENIR
ADD FOREIGN KEY (nom_promo, annee_promo) REFERENCES PROMO (nom_promo, annee_promo);

ALTER TABLE APPARTENIR
ADD FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT (id_etudiant);

ALTER TABLE ASSEMBLER
ADD FOREIGN KEY (id_admin) REFERENCES ADMINI (id_admin);

ALTER TABLE ASSEMBLER
ADD FOREIGN KEY (id_jury) REFERENCES JURY (id_jury);

ALTER TABLE COMPOSER
ADD FOREIGN KEY (id_soutenance) REFERENCES SOUTENANCE (id_soutenance);

ALTER TABLE COMPOSER
ADD FOREIGN KEY (id_enseignant) REFERENCES ENSEIGNANT (id_enseignant);

ALTER TABLE DEMARCHE
ADD FOREIGN KEY (id_entreprise) REFERENCES ENTREPRISE (id_entreprise);

ALTER TABLE DEMARCHE
ADD FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT (id_etudiant);

ALTER TABLE JURY
ADD FOREIGN KEY (id_soutenance) REFERENCES SOUTENANCE (id_soutenance);

ALTER TABLE MAITRE_STAGE
ADD FOREIGN KEY (id_entreprise) REFERENCES ENTREPRISE (id_entreprise);

ALTER TABLE PROMO
ADD FOREIGN KEY (id_enseignant) REFERENCES ENSEIGNANT (id_enseignant);

ALTER TABLE SOUTENANCE
ADD FOREIGN KEY (id_stage) REFERENCES STAGE (id_stage);

ALTER TABLE STAGE
ADD FOREIGN KEY (id_demarche) REFERENCES DEMARCHE (id_demarche);

ALTER TABLE STAGE
ADD FOREIGN KEY (id_maitre) REFERENCES MAITRE_STAGE (id_maitre);

ALTER TABLE TUTORER
ADD FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT (id_etudiant);

ALTER TABLE TUTORER
ADD FOREIGN KEY (id_enseignant) REFERENCES ENSEIGNANT (id_enseignant);