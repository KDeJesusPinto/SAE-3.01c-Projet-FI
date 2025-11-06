INSERT INTO ENTREPRISE (id_entreprise, nom_entreprise, secteur, ville, adresse, code_postal, typeE, tel_entreprise, email_entreprise) VALUES
(1, 'TechSolutions', 'Informatique', 'Paris', '10 rue du Code', '75001', 'SARL', '0145678913', 'contact@techsolutions.fr'),
(2, 'DataCorp', 'Analyse de données', 'Lyon', '25 avenue des Sciences', '69002', 'SAS', '0478912346', 'info@datacorp.fr'),
(3, 'WebInnovate', 'Développement Web', 'Marseille', '8 rue du Port', '13002', 'SARL', '0491234568', 'contact@webinnovate.fr'),
(4, 'AI Systems', 'Intelligence Artificielle', 'Toulouse', '42 allée des Startups', '31000', 'SA', '0562347890', 'contact@aisystems.fr');


INSERT INTO ETUDIANT (id_etudiant, nom_etudiant, prenom_etudiant, date_naissance, civilite_etudiant, telephone_etudiant, email_etudiant) VALUES
(1, 'Doe', 'John', '2003-05-14', 'M.', '0601020304', 'john.doe@gmail.com'),
(2, 'Smith', 'Jane', '2002-11-22', 'Mme', '0605060708', 'jane.smith@gmail.com'),
(3, 'Brown', 'Alice', '2003-02-10', 'Mme', '0608091011', 'alice.brown@gmail.com'),
(4, 'Martin', 'Lucas', '2004-03-05', 'M.', '0612131415', 'lucas.martin@gmail.com');


INSERT INTO ENSEIGNANT (id_enseignant, nom_enseignant, prenom_enseignant, civilite_enseignant, email_enseignant) VALUES
(1, 'Dubois', 'Jean', 'M.', 'jean.dubois@univ.fr'),
(2, 'Martin', 'Sophie', 'Mme', 'sophie.martin@univ.fr'),
(3, 'Lefebvre', 'Pierre', 'M.', 'pierre.lefebvre@univ.fr'),
(4, 'Durand', 'Camille', 'Mme', 'camille.durand@univ.fr');


INSERT INTO PROMO (nom_promo, annee_promo, formation_promo, id_enseignant) VALUES
('BUT2', 2024, 'BUT Informatique', 1),
('BUT3', 2025, 'BUT Informatique', 2),
('BUT1', 2023, 'BUT Informatique', 3),
('BUT2', 2025, 'BUT Informatique', 4);


INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant) VALUES
(1, 'BUT2', 2024, 'Formation initiale'),
(2, 'BUT2', 2024, 'Formation initiale'),
(3, 'BUT1', 2023, 'Formation initiale'),
(4, 'BUT3', 2025, 'Formation apprentissage');


INSERT INTO TUTORER (id_enseignant, id_etudiant, annee) VALUES
(1, 1, 2024),
(2, 2, 2024),
(3, 3, 2023),
(4, 4, 2025);


INSERT INTO MAITRE_STAGE (id_maitre, nom_maitre, prenom_maitre, civilite_maitre, tel_maitre, email_maitre, id_entreprise) VALUES
(1, 'Dumas', 'Philippe', 'M.', '0145678913', 'philippe.dumas@techsolutions.fr', 1),
(2, 'Lambert', 'Sylvie', 'Mme', '0478912346', 'sylvie.lambert@datacorp.fr', 2),
(3, 'Carpentier', 'Michel', 'M.', '0491234568', 'michel.carpentier@webinnovate.fr', 3),
(4, 'Faure', 'Julie', 'Mme', '0562347890', 'julie.faure@aisystems.fr', 4);


INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(1, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2024-09-15', NULL, 'Stage obtenu', NULL, 'cv_doe.pdf', 'lm_doe.pdf', 1, 1),
(2, 'LinkedIn', 'Réponse à offre', 'Refusée', '2024-09-10', '2024-09-25', 'Refusé', 'Profil junior', 'cv_doe.pdf', 'lm_doe2.pdf', 2, 1),
(3, 'Salon', 'Contact direct', 'En attente', '2024-09-20', NULL, NULL, NULL, 'cv_smith.pdf', 'lm_smith.pdf', 3, 2),
(4, 'Indeed', 'Réponse à offre', 'Acceptée', '2024-09-12', NULL, 'Stage obtenu', NULL, 'cv_brown.pdf', 'lm_brown.pdf', 4, 3);


INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(1, 'Stage de fin études', '2024-10-01', '2025-03-31', 6, 'mois', 'Développer une application web de gestion', 'Développement Full-Stack', 1, 1),
(2, 'Stage de deuxième année', '2024-10-15', '2025-04-15', 6, 'mois', 'Analyse de données massives pour la prédiction', 'Big Data et Machine Learning', 2, 4),
(3, 'Stage initiation', '2023-05-01', '2023-07-31', 3, 'mois', 'Découverte du développement front-end', 'Web & UX', 3, 2),
(4, 'Stage d\'approfondissement', '2025-01-10', '2025-06-30', 6, 'mois', 'Conception d\'un agent conversationnel', 'IA & NLP', 4, 3);
