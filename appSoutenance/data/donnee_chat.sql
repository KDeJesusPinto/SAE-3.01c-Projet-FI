-- Script d'insertion de données pour la base appsoutenance
USE appsoutenance;

-- ============================
-- INSERTION DES ENSEIGNANTS (10)
-- ============================
INSERT INTO ENSEIGNANT (id_enseignant, nom_enseignant, prenom_enseignant, civilite_enseignant, email_enseignant) VALUES
(1, 'Dubois', 'Jean', 'M.', 'jean.dubois@univ.fr'),
(2, 'Martin', 'Sophie', 'Mme', 'sophie.martin@univ.fr'),
(3, 'Lefebvre', 'Pierre', 'M.', 'pierre.lefebvre@univ.fr'),
(4, 'Rousseau', 'Marie', 'Mme', 'marie.rousseau@univ.fr'),
(5, 'Bernard', 'Luc', 'M.', 'luc.bernard@univ.fr'),
(6, 'Thomas', 'Claire', 'Mme', 'claire.thomas@univ.fr'),
(7, 'Petit', 'François', 'M.', 'francois.petit@univ.fr'),
(8, 'Robert', 'Anne', 'Mme', 'anne.robert@univ.fr'),
(9, 'Richard', 'Marc', 'M.', 'marc.richard@univ.fr'),
(10, 'Durand', 'Isabelle', 'Mme', 'isabelle.durand@univ.fr');

-- ============================
-- INSERTION DES PROMOTIONS
-- ============================
INSERT INTO PROMO (nom_promo, annee_promo, formation_promo, id_enseignant) VALUES
('BUT2', 2024, 'BUT Informatique', 1),
('BUT2', 2025, 'BUT Informatique', 2),
('BUT3', 2025, 'BUT Informatique', 1);

-- ============================
-- INSERTION DES ÉTUDIANTS (24 au total)
-- ============================

-- 8 étudiants BUT3 2025 (qui étaient en BUT2 2024)
INSERT INTO ETUDIANT (id_etudiant, nom_etudiant, prenom_etudiant, date_naissance, civilite_etudiant, telephone_etudiant, email_etudiant) VALUES
(1, 'Dupont', 'Alexandre', '2003-05-12', 'M.', '0612345678', 'alexandre.dupont@edu.fr'),
(2, 'Moreau', 'Camille', '2003-08-24', 'Mme', '0623456789', 'camille.moreau@edu.fr'),
(3, 'Laurent', 'Thomas', '2002-11-03', 'M.', '0634567812', 'thomas.laurent@edu.fr'),
(4, 'Simon', 'Julie', '2003-02-17', 'Mme', '0645678923', 'julie.simon@edu.fr'),
(5, 'Michel', 'Lucas', '2003-07-09', 'M.', '0656789134', 'lucas.michel@edu.fr'),
(6, 'Leroy', 'Emma', '2002-12-21', 'Mme', '0667891245', 'emma.leroy@edu.fr'),
(7, 'Fournier', 'Hugo', '2003-04-15', 'M.', '0678912356', 'hugo.fournier@edu.fr'),
(8, 'Girard', 'Léa', '2003-09-28', 'Mme', '0689123467', 'lea.girard@edu.fr'),

-- 8 étudiants BUT2 2025
(9, 'Bonnet', 'Antoine', '2004-03-14', 'M.', '0691234578', 'antoine.bonnet@edu.fr'),
(10, 'Blanc', 'Sarah', '2004-06-22', 'Mme', '0612345987', 'sarah.blanc@edu.fr'),
(11, 'Garnier', 'Maxime', '2004-01-08', 'M.', '0623456198', 'maxime.garnier@edu.fr'),
(12, 'Faure', 'Chloé', '2004-10-19', 'Mme', '0634567219', 'chloe.faure@edu.fr'),
(13, 'Roussel', 'Nathan', '2004-05-30', 'M.', '0645678321', 'nathan.roussel@edu.fr'),
(14, 'Vincent', 'Manon', '2004-08-11', 'Mme', '0656789432', 'manon.vincent@edu.fr'),
(15, 'Muller', 'Arthur', '2004-02-25', 'M.', '0667891543', 'arthur.muller@edu.fr'),
(16, 'Lefevre', 'Jade', '2004-07-07', 'Mme', '0678912654', 'jade.lefevre@edu.fr'),

-- 8 étudiants BUT2 2024 (mêmes que BUT3 2025 mais dans leur ancienne promo)
(17, 'Mercier', 'Paul', '2004-11-16', 'M.', '0689123765', 'paul.mercier@edu.fr'),
(18, 'Lemoine', 'Louise', '2004-04-02', 'Mme', '0691234876', 'louise.lemoine@edu.fr'),
(19, 'Andre', 'Theo', '2004-09-13', 'M.', '0612348765', 'theo.andre@edu.fr'),
(20, 'Roux', 'Clara', '2004-12-28', 'Mme', '0623459876', 'clara.roux@edu.fr'),
(21, 'David', 'Victor', '2005-03-05', 'M.', '0634561987', 'victor.david@edu.fr'),
(22, 'Bertrand', 'Zoé', '2005-06-18', 'Mme', '0645672198', 'zoe.bertrand@edu.fr'),
(23, 'Morel', 'Gabriel', '2005-01-21', 'M.', '0656783219', 'gabriel.morel@edu.fr'),
(24, 'Fontaine', 'Alice', '2005-08-09', 'Mme', '0667894321', 'alice.fontaine@edu.fr');

-- ============================
-- APPARTENANCE AUX PROMOTIONS
-- ============================

-- Étudiants 1-8 : BUT2 2024 puis BUT3 2025
INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant) VALUES
(1, 'BUT2', 2024, 'Formation initiale'),
(2, 'BUT2', 2024, 'Formation initiale'),
(3, 'BUT2', 2024, 'Alternance'),
(4, 'BUT2', 2024, 'Formation initiale'),
(5, 'BUT2', 2024, 'Formation initiale'),
(6, 'BUT2', 2024, 'Alternance'),
(7, 'BUT2', 2024, 'Formation initiale'),
(8, 'BUT2', 2024, 'Formation initiale'),

(1, 'BUT3', 2025, 'Formation initiale'),
(2, 'BUT3', 2025, 'Formation initiale'),
(3, 'BUT3', 2025, 'Alternance'),
(4, 'BUT3', 2025, 'Formation initiale'),
(5, 'BUT3', 2025, 'Formation initiale'),
(6, 'BUT3', 2025, 'Alternance'),
(7, 'BUT3', 2025, 'Formation initiale'),
(8, 'BUT3', 2025, 'Formation initiale'),

-- Étudiants 9-16 : BUT2 2025
(9, 'BUT2', 2025, 'Formation initiale'),
(10, 'BUT2', 2025, 'Formation initiale'),
(11, 'BUT2', 2025, 'Alternance'),
(12, 'BUT2', 2025, 'Formation initiale'),
(13, 'BUT2', 2025, 'Formation initiale'),
(14, 'BUT2', 2025, 'Alternance'),
(15, 'BUT2', 2025, 'Formation initiale'),
(16, 'BUT2', 2025, 'Formation initiale'),

-- Étudiants 17-24 : BUT2 2024 (autres étudiants)
(17, 'BUT2', 2024, 'Formation initiale'),
(18, 'BUT2', 2024, 'Formation initiale'),
(19, 'BUT2', 2024, 'Alternance'),
(20, 'BUT2', 2024, 'Formation initiale'),
(21, 'BUT2', 2024, 'Formation initiale'),
(22, 'BUT2', 2024, 'Alternance'),
(23, 'BUT2', 2024, 'Formation initiale'),
(24, 'BUT2', 2024, 'Formation initiale');

-- ============================
-- TUTEURS (24 tuteurs, 1 par étudiant)
-- ============================
INSERT INTO TUTORER (id_enseignant, id_etudiant, annee) VALUES
(1, 1, 2025), (2, 2, 2025), (3, 3, 2025), (4, 4, 2025),
(5, 5, 2025), (6, 6, 2025), (7, 7, 2025), (8, 8, 2025),
(9, 9, 2025), (10, 10, 2025), (1, 11, 2025), (2, 12, 2025),
(3, 13, 2025), (4, 14, 2025), (5, 15, 2025), (6, 16, 2025),
(7, 17, 2024), (8, 18, 2024), (9, 19, 2024), (10, 20, 2024),
(1, 21, 2024), (2, 22, 2024), (3, 23, 2024), (4, 24, 2024);

-- ============================
-- INSERTION DES ENTREPRISES
-- ============================
INSERT INTO ENTREPRISE (id_entreprise, nom_entreprise, secteur, ville, adresse, code_postal, typeE, tel_entreprise, email_entreprise) VALUES
(1, 'TechSolutions', 'Informatique', 'Paris', '15 rue de la Technologie', '75001', 'PME', '0145678912', 'contact@techsolutions.fr'),
(2, 'DataCorp', 'Big Data', 'Lyon', '23 avenue des Données', '69001', 'Grande entreprise', '0478912345', 'rh@datacorp.fr'),
(3, 'WebInnovate', 'Développement Web', 'Marseille', '8 boulevard du Numérique', '13001', 'Startup', '0491234567', 'info@webinnovate.fr'),
(4, 'SecureIT', 'Cybersécurité', 'Toulouse', '42 rue de la Sécurité', '31000', 'PME', '0561234789', 'contact@secureit.fr'),
(5, 'CloudServices', 'Cloud Computing', 'Nantes', '17 place du Cloud', '44000', 'Grande entreprise', '0240567891', 'recrutement@cloudservices.fr'),
(6, 'AppDev', 'Applications mobiles', 'Lille', '31 rue des Applications', '59000', 'Startup', '0320456789', 'jobs@appdev.fr'),
(7, 'SoftwareGroup', 'Logiciels', 'Bordeaux', '9 cours des Logiciels', '33000', 'Grande entreprise', '0556789123', 'contact@softwaregroup.fr'),
(8, 'DigitalFactory', 'Transformation digitale', 'Nice', '12 promenade du Digital', '06000', 'PME', '0493567812', 'info@digitalfactory.fr');

-- ============================
-- INSERTION DES MAÎTRES DE STAGE
-- ============================
INSERT INTO MAITRE_STAGE (id_maitre, nom_maitre, prenom_maitre, civilite_maitre, tel_maitre, email_maitre, id_entreprise) VALUES
(1, 'Dumas', 'Philippe', 'M.', '0145678913', 'philippe.dumas@techsolutions.fr', 1),
(2, 'Lambert', 'Sylvie', 'Mme', '0478912346', 'sylvie.lambert@datacorp.fr', 2),
(3, 'Carpentier', 'Michel', 'M.', '0491234568', 'michel.carpentier@webinnovate.fr', 3),
(4, 'Masson', 'Catherine', 'Mme', '0561234791', 'catherine.masson@secureit.fr', 4),
(5, 'Blanc', 'Olivier', 'M.', '0240567892', 'olivier.blanc@cloudservices.fr', 5),
(6, 'Garnier', 'Nathalie', 'Mme', '0320456791', 'nathalie.garnier@appdev.fr', 6),
(7, 'Faure', 'Alain', 'M.', '0556789124', 'alain.faure@softwaregroup.fr', 7),
(8, 'Roussel', 'Sandrine', 'Mme', '0493567813', 'sandrine.roussel@digitalfactory.fr', 8),
(9, 'Vincent', 'David', 'M.', '0145678914', 'david.vincent@techsolutions.fr', 1),
(10, 'Muller', 'Brigitte', 'Mme', '0478912347', 'brigitte.muller@datacorp.fr', 2);

-- ============================
-- DÉMARCHES (6 étudiants avec max 3 démarches chacun)
-- ============================

-- Étudiant 1 : 3 démarches
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(1, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2024-09-15', NULL, 'Stage obtenu', NULL, 'cv_dupont.pdf', 'lm_dupont.pdf', 1, 1),
(2, 'LinkedIn', 'Réponse à offre', 'Refusée', '2024-09-10', '2024-09-25', 'Refusé', 'Profil junior', 'cv_dupont.pdf', 'lm_dupont2.pdf', 2, 1),
(3, 'Salon', 'Contact direct', 'En attente', '2024-09-20', NULL, NULL, NULL, 'cv_dupont.pdf', 'lm_dupont3.pdf', 3, 1);

-- Étudiant 2 : 2 démarches
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(4, 'Indeed', 'Réponse à offre', 'Acceptée', '2024-09-12', NULL, 'Stage obtenu', NULL, 'cv_moreau.pdf', 'lm_moreau.pdf', 2, 2),
(5, 'Site entreprise', 'Candidature spontanée', 'Refusée', '2024-09-08', '2024-09-22', 'Refusé', 'Pas de place', 'cv_moreau.pdf', 'lm_moreau2.pdf', 4, 2);

-- Étudiant 3 : 3 démarches
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(6, 'Réseau personnel', 'Recommandation', 'Acceptée', '2024-09-18', NULL, 'Stage obtenu', NULL, 'cv_laurent.pdf', 'lm_laurent.pdf', 3, 3),
(7, 'Indeed', 'Réponse à offre', 'Refusée', '2024-09-05', NULL, 'Refusé', 'Niveau insuffisant', 'cv_laurent.pdf', 'lm_laurent2.pdf', 5, 3),
(8, 'LinkedIn', 'Réponse à offre', 'En attente', '2024-09-25', NULL, NULL, NULL, 'cv_laurent.pdf', 'lm_laurent3.pdf', 6, 3);

-- Étudiant 9 : 2 démarches
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(9, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2024-09-14', NULL, 'Stage obtenu', NULL, 'cv_bonnet.pdf', 'lm_bonnet.pdf', 4, 9),
(10, 'Salon', 'Contact direct', 'Refusée', '2024-09-11', NULL, 'Refusé', 'Budget limité', 'cv_bonnet.pdf', 'lm_bonnet2.pdf', 7, 9);

-- Étudiant 10 : 3 démarches
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(11, 'Indeed', 'Réponse à offre', 'Acceptée', '2024-09-16', NULL, 'Stage obtenu', NULL, 'cv_blanc.pdf', 'lm_blanc.pdf', 5, 10),
(12, 'LinkedIn', 'Réponse à offre', 'En attente', '2024-09-22', NULL, NULL, NULL, 'cv_blanc.pdf', 'lm_blanc2.pdf', 8, 10),
(13, 'Site entreprise', 'Candidature spontanée', 'Refusée', '2024-09-07', '2024-09-21', 'Refusé', 'Profil inadapté', 'cv_blanc.pdf', 'lm_blanc3.pdf', 1, 10);

-- Étudiant 11 : 1 démarche
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(14, 'Réseau personnel', 'Recommandation', 'Acceptée', '2024-09-19', NULL, 'Stage obtenu', NULL, 'cv_garnier.pdf', 'lm_garnier.pdf', 6, 11);

-- ============================
-- STAGES (19 étudiants avec stage, 5 sans)
-- Étudiants SANS stage : 4, 5, 7, 8, 17
-- ============================

-- Stages des étudiants BUT3 2025 (qui ont fait des démarches)
INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(1, 'Stage de fin d\'études', '2024-10-01', '2025-03-31', 6, 'mois', 'Développement d\'une application web de gestion', 'Développement Full-Stack', 1, 1),
(2, 'Stage de fin d\'études', '2024-10-15', '2025-04-15', 6, 'mois', 'Analyse de données massives pour la prédiction', 'Big Data et Machine Learning', 2, 4),
(3, 'Stage de fin d\'études', '2024-10-01', '2025-03-31', 6, 'mois', 'Création d\'un site e-commerce responsive', 'Développement Web', 3, 6);

-- Stage étudiant 6 (BUT3 2025, sans démarche enregistrée mais avec stage)
INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(4, 'Stage de fin d\'études', '2024-10-15', '2025-04-15', 6, 'mois', 'Développement d\'applications mobiles iOS/Android', 'Mobile Development', 6, NULL);

-- Stages des étudiants BUT2 2025 (qui ont fait des démarches)
INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(5, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Mise en place d\'une infrastructure sécurisée', 'Cybersécurité et Réseaux', 4, 9),
(6, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Migration vers le Cloud AWS', 'Cloud Computing', 5, 11),
(7, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Développement d\'une application mobile de fitness', 'Applications mobiles', 6, 14);

-- Stages des autres étudiants BUT2 2025 (sans démarches enregistrées)
INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(8, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d\'un ERP sur mesure', 'Développement logiciel', 7, NULL),
(9, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Transformation digitale des processus internes', 'Digital & Innovation', 8, NULL),
(10, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d\'une plateforme web collaborative', 'Développement Web', 9, NULL),
(11, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Optimisation des performances d\'applications', 'Performance & Big Data', 10, NULL);

-- Stages des étudiants BUT2 2024 (étudiants 18-24, sauf 17)
INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(12, 'Stage professionnel', '2024-04-01', '2024-06-30', 3, 'mois', 'Création d\'interfaces utilisateur modernes', 'UX/UI Design', 1, NULL),
(13, 'Stage professionnel', '2024-04-15', '2024-07-15', 3, 'mois', 'Analyse de données clients pour le marketing', 'Data Analytics', 2, NULL),
(14, 'Stage professionnel', '2024-04-01', '2024-06-30', 3, 'mois', 'Développement d\'API REST pour microservices', 'Architecture logicielle', 3, NULL),
(15, 'Stage professionnel', '2024-04-15', '2024-07-15', 3, 'mois', 'Mise en place d\'une solution IoT', 'Internet des Objets', 4, NULL),
(16, 'Stage professionnel', '2024-04-01', '2024-06-30', 3, 'mois', 'Développement d\'un chatbot intelligent', 'Intelligence Artificielle', 5, NULL),
(17, 'Stage professionnel', '2024-04-15', '2024-07-15', 3, 'mois', 'Automatisation des tests logiciels', 'QA & Testing', 6, NULL),
(18, 'Stage professionnel', '2024-04-01', '2024-06-30', 3, 'mois', 'Développement d\'un système de monitoring', 'DevOps', 7, NULL),
(19, 'Stage professionnel', '2024-04-15', '2024-07-15', 3, 'mois', 'Création d\'un CMS personnalisé', 'Développement Web', 8, NULL);

-- Correction des id_stage pour les stages avec démarche NULL
UPDATE STAGE SET id_demarche = 1 WHERE id_stage = 4;
UPDATE STAGE SET id_demarche = 2 WHERE id_stage = 8;
UPDATE STAGE SET id_demarche = 3 WHERE id_stage = 9;
UPDATE STAGE SET id_demarche = 4 WHERE id_stage = 10;
UPDATE STAGE SET id_demarche = 5 WHERE id_stage = 11;
UPDATE STAGE SET id_demarche = 6 WHERE id_stage = 12;
UPDATE STAGE SET id_demarche = 7 WHERE id_stage = 13;
UPDATE STAGE SET id_demarche = 8 WHERE id_stage = 14;
UPDATE STAGE SET id_demarche = 9 WHERE id_stage = 15;
UPDATE STAGE SET id_demarche = 10 WHERE id_stage = 16;
UPDATE STAGE SET id_demarche = 11 WHERE id_stage = 17;
UPDATE STAGE SET id_demarche = 12 WHERE id_stage = 18;
UPDATE STAGE SET id_demarche = 13 WHERE id_stage = 19;

-- Création de démarches fictives pour les stages sans démarche
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(15, 'Réseau école', 'Partenariat', 'Acceptée', '2024-09-01', NULL, 'Stage obtenu', NULL, 'cv_leroy.pdf', 'lm_leroy.pdf', 6, 6),
(16, 'Réseau école', 'Partenariat', 'Acceptée', '2025-02-01', NULL, 'Stage obtenu', NULL, 'cv_faure.pdf', 'lm_faure.pdf', 7, 12),
(17, 'Réseau école', 'Partenariat', 'Acceptée', '2025-02-15', NULL, 'Stage obtenu', NULL, 'cv_roussel.pdf', 'lm_roussel.pdf', 8, 13),
(18, 'Réseau école', 'Partenariat', 'Acceptée', '2025-02-01', NULL, 'Stage obtenu', NULL, 'cv_vincent.pdf', 'lm_vincent.pdf', 1, 14),
(19, 'Réseau école', 'Partenariat', 'Acceptée', '2025-02-15', NULL, 'Stage obtenu', NULL, 'cv_muller.pdf', 'lm_muller.pdf', 2, 15),
(20, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-01', NULL, 'Stage obtenu', NULL, 'cv_lemoine.pdf', 'lm_lemoine.pdf', 1, 18),
(21, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-15', NULL, 'Stage obtenu', NULL, 'cv_andre.pdf', 'lm_andre.pdf', 2, 19),
(22, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-01', NULL, 'Stage obtenu', NULL, 'cv_roux.pdf', 'lm_roux.pdf', 3, 20),
(23, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-15', NULL, 'Stage obtenu', NULL, 'cv_david.pdf', 'lm_david.pdf', 4, 21),
(24, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-01', NULL, 'Stage obtenu', NULL, 'cv_bertrand.pdf', 'lm_bertrand.pdf', 5, 22),
(25, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-15', NULL, 'Stage obtenu', NULL, 'cv_morel.pdf', 'lm_morel.pdf', 6, 23),
(26, 'Réseau école', 'Partenariat', 'Acceptée', '2024-02-01', NULL, 'Stage obtenu', NULL, 'cv_fontaine.pdf', 'lm_fontaine.pdf', 7, 24);

-- Mise à jour des stages avec les bonnes démarches
UPDATE STAGE SET id_demarche = 15 WHERE id_stage = 4;
UPDATE STAGE SET id_demarche = 16 WHERE id_stage = 8;
UPDATE STAGE SET id_demarche = 17 WHERE id_stage = 9;
UPDATE STAGE SET id_demarche = 18 WHERE id_stage = 10;
UPDATE STAGE SET id_demarche = 19 WHERE id_stage = 11;
UPDATE STAGE SET id_demarche = 20 WHERE id_stage = 12;
UPDATE STAGE SET id_demarche = 21 WHERE id_stage = 13;
UPDATE STAGE SET id_demarche = 22 WHERE id_stage = 14;
UPDATE STAGE SET id_demarche = 23 WHERE id_stage = 15;
UPDATE STAGE SET id_demarche = 24 WHERE id_stage = 16;
UPDATE STAGE SET id_demarche = 25 WHERE id_stage = 17;
UPDATE STAGE SET id_demarche = 26 WHERE id_stage = 18;
UPDATE STAGE SET id_demarche = 1 WHERE id_stage = 19;

-- ============================
-- SOUTENANCES (pour les étudiants BUT3 2025 et certains BUT2 2024)
-- Seulement 12 soutenances sur 19 stages
-- ============================

-- Soutenances pour BUT3 2025 (3 étudiants avec stage : 1, 2, 3, 6)
INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
(1, 101, 'Bâtiment A', '2025-04-15', '09:00', '10:30', 1),
(2, 102, 'Bâtiment A', '2025-04-15', '14:00', '15:30', 2),
(3, 103, 'Bâtiment B', '2025-04-16', '09:00', '10:30', 3),
(4, 104, 'Bâtiment B', '2025-04-16', '14:00', '15:30', 4);

-- Soutenances pour BUT2 2024 (certains étudiants : 18, 19, 20, 21, 22, 23, 24, 16)
INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
(5, 201, 'Bâtiment C', '2024-07-01', '09:00', '10:00', 12),
(6, 202, 'Bâtiment C', '2024-07-01', '10:30', '11:30', 13),
(7, 203, 'Bâtiment C', '2024-07-01', '14:00', '15:00', 14),
(8, 204, 'Bâtiment C', '2024-07-02', '09:00', '10:00', 15),
(9, 201, 'Bâtiment C', '2024-07-02', '10:30', '11:30', 16),
(10, 202, 'Bâtiment C', '2024-07-02', '14:00', '15:00', 17),
(11, 203, 'Bâtiment C', '2024-07-03', '09:00', '10:00', 18),
(12, 204, 'Bâtiment C', '2024-07-03', '10:30', '11:30', 19);

-- ============================
-- JURYS (un jury par soutenance)
-- ============================
INSERT INTO JURY (id_jury, date_jury, h_jury, duree, id_soutenance) VALUES
(1, '2025-04-15', '09:00', 90, 1),
(2, '2025-04-15', '14:00', 90, 2),
(3, '2025-04-16', '09:00', 90, 3),
(4, '2025-04-16', '14:00', 90, 4),
(5, '2024-07-01', '09:00', 60, 5),
(6, '2024-07-01', '10:30', 60, 6),
(7, '2024-07-01', '14:00', 60, 7),
(8, '2024-07-02', '09:00', 60, 8),
(9, '2024-07-02', '10:30', 60, 9),
(10, '2024-07-02', '14:00', 60, 10),
(11, '2024-07-03', '09:00', 60, 11),
(12, '2024-07-03', '10:30', 60, 12);

-- ============================
-- COMPOSER (au moins 2 enseignants par jury)
-- ============================

-- Jury 1 (soutenance 1 - étudiant 1, tuteur enseignant 1)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(1, 1),  -- Tuteur
(3, 1),  -- Autre enseignant
(5, 1);  -- Troisième enseignant

-- Jury 2 (soutenance 2 - étudiant 2, tuteur enseignant 2)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(2, 2),  -- Tuteur
(4, 2),  -- Autre enseignant
(6, 2);  -- Troisième enseignant

-- Jury 3 (soutenance 3 - étudiant 3, tuteur enseignant 3)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(3, 3),  -- Tuteur
(1, 3),  -- Autre enseignant
(7, 3);  -- Troisième enseignant

-- Jury 4 (soutenance 4 - étudiant 6, tuteur enseignant 6)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(6, 4),  -- Tuteur
(2, 4),  -- Autre enseignant
(8, 4);  -- Troisième enseignant

-- Jury 5 (soutenance 5 - étudiant 18, tuteur enseignant 8)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(8, 5),  -- Tuteur
(9, 5);  -- Autre enseignant

-- Jury 6 (soutenance 6 - étudiant 19, tuteur enseignant 9)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(9, 6),  -- Tuteur
(10, 6); -- Autre enseignant

-- Jury 7 (soutenance 7 - étudiant 20, tuteur enseignant 10)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(10, 7), -- Tuteur
(1, 7);  -- Autre enseignant

-- Jury 8 (soutenance 8 - étudiant 21, tuteur enseignant 1)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(1, 8),  -- Tuteur
(2, 8);  -- Autre enseignant

-- Jury 9 (soutenance 9 - étudiant 22, tuteur enseignant 2)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(2, 9),  -- Tuteur
(3, 9);  -- Autre enseignant

-- Jury 10 (soutenance 10 - étudiant 23, tuteur enseignant 3)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(3, 10), -- Tuteur
(4, 10); -- Autre enseignant

-- Jury 11 (soutenance 11 - étudiant 24, tuteur enseignant 4)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(4, 11), -- Tuteur
(5, 11); -- Autre enseignant

-- Jury 12 (soutenance 12 - étudiant 16, tuteur enseignant 6)
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(6, 12), -- Tuteur
(7, 12); -- Autre enseignant

-- ============================
-- FIN DU SCRIPT
-- ============================

-- Récapitulatif :
-- - 10 enseignants
-- - 24 étudiants (8 par promo)
-- - 3 promotions (BUT2 2024, BUT2 2025, BUT3 2025)
-- - Les étudiants 1-8 de BUT3 2025 étaient en BUT2 2024
-- - 24 tuteurs (1 par étudiant, répartis entre les 10 enseignants)
-- - 6 étudiants ont fait des démarches (étudiants 1, 2, 3, 9, 10, 11)
-- - Max 3 démarches par étudiant
-- - 19 étudiants ont un stage (5 sans stage : 4, 5, 7, 8, 17)
-- - 12 soutenances sur les 19 stages
-- - 12 jurys avec au moins 2 enseignants chacun
-- - Tous les stages ont un maître de stage
-- - 8 entreprises
-- - 10 maîtres de stage