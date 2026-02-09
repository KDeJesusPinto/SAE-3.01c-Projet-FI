INSERT INTO ENTREPRISE (
        id_entreprise,
        nom_entreprise,
        secteur,
        ville,
        adresse,
        code_postal,
        typeE,
        tel_entreprise,
        email_entreprise
    )
VALUES (
        1,
        'TechSolutions',
        'Informatique',
        'Paris',
        '10 rue du Code',
        '75001',
        'SARL',
        '0145678913',
        'contact@techsolutions.fr'
    ),
    (
        2,
        'DataCorp',
        'Analyse de données',
        'Lyon',
        '25 avenue des Sciences',
        '69002',
        'SAS',
        '0478912346',
        'info@datacorp.fr'
    ),
    (
        3,
        'WebInnovate',
        'Développement Web',
        'Marseille',
        '8 rue du Port',
        '13002',
        'SARL',
        '0491234568',
        'contact@webinnovate.fr'
    ),
    (
        4,
        'AI Systems',
        'Intelligence Artificielle',
        'Toulouse',
        '42 allée des Startups',
        '31000',
        'SA',
        '0562347890',
        'contact@aisystems.fr'
    );

INSERT INTO ETUDIANT (
        id_etudiant,
        nom_etudiant,
        prenom_etudiant,
        date_naissance,
        civilite_etudiant,
        telephone_etudiant,
        email_etudiant,
        login_etudiant,
        pwd_etudiant
    )
VALUES (
        1,
        'Doe',
        'John',
        '2003-05-14',
        'M.',
        '0601020304',
        'john.doe@gmail.com',
        'johndoe',
        'pass1'
    ),
    (
        2,
        'Smith',
        'Jane',
        '2002-11-22',
        'Mme',
        '0605060708',
        'jane.smith@gmail.com',
        'janesmith',
        'pass2'
    ),
    (
        3,
        'Brown',
        'Alice',
        '2003-02-10',
        'Mme',
        '0608091011',
        'alice.brown@gmail.com',
        'alicebrown',
        'pass3'
    ),
    (
        4,
        'Martin',
        'Lucas',
        '2004-03-05',
        'M.',
        '0612131415',
        'lucas.martin@gmail.com',
        'lucasmartin',
        'pass4'
    ),
    (
        5,
        'Wilson',
        'Emma',
        '2002-07-19',
        'Mme',
        '0616171819',
        'emma.wilson@gmail.com',
        'emmawilson',
        'pass5'
    ),
    (
        6,
        'Taylor',
        'Olivia',
        '2003-12-30',
        'Mme',
        '0620212223',
        'olivia.taylor@gmail.com',
        'oliviataylor',
        'pass6'
    ),
    (
        7,
        'Anderson',
        'Liam',
        '2004-09-25',
        'M.',
        '0624252627',
        'liam.anderson@gmail.com',
        'liamanderson',
        'pass7'
    ),
    (
        8,
        'Thomas',
        'Sophia',
        '2002-04-18',
        'Mme',
        '0628293031',
        'sophia.thomas@gmail.com',
        'sophiathomas',
        'pass8'
    ),
    (
        9,
        'Jackson',
        'Mia',
        '2003-08-09',
        'Mme',
        '0632333435',
        'mia.jackson@gmail.com',
        'miamjackson',
        'pass9'
    ),
    (
        10,
        'White',
        'Noah',
        '2004-01-12',
        'M.',
        '0636373839',
        'noah.white@gmail.com',
        'noahwhite',
        'pass10'
    );

INSERT INTO ENSEIGNANT (
        id_enseignant,
        nom_enseignant,
        prenom_enseignant,
        civilite_enseignant,
        email_enseignant,
        login_enseignant,
        pwd_enseignant
    )
VALUES (
        1,
        'Dubois',
        'Jean',
        'M.',
        'jean.dubois@univ.fr',
        'jdubois',
        'prof1'
    ),
    (
        2,
        'Martin',
        'Sophie',
        'Mme',
        'sophie.martin@univ.fr',
        'smartin',
        'prof2'
    ),
    (
        3,
        'Lefebvre',
        'Pierre',
        'M.',
        'pierre.lefebvre@univ.fr',
        'plefebvre',
        'prof3'
    ),
    (
        4,
        'Durand',
        'Camille',
        'Mme',
        'camille.durand@univ.fr',
        'cdurand',
        'prof4'
    ),
    (
        5,
        'Moreau',
        'Luc',
        'M.',
        'luc.moreau@univ.fr',
        'lmoreau',
        'prof5'
    ),
    (
        6,
        'Girard',
        'Isabelle',
        'Mme',
        'isabelle.girard@univ.fr',
        'igirard',
        'prof6'
    ),
    (
        7,
        'Roux',
        'Antoine',
        'M.',
        'antoine.roux@univ.fr',
        'aroux',
        'prof7'
    ),
    (
        8,
        'Fontaine',
        'Elise',
        'Mme',
        'elise.fontaine@univ.fr',
        'efontaine',
        'prof8'
    ),
    (
        9,
        'Blanc',
        'Marc',
        'M.',
        'marc.blanc@univ.fr',
        'mblanc',
        'prof9'
    ),
    (
        10,
        'Garnier',
        'Nathalie',
        'Mme',
        'nathalie.garnier@univ.fr',
        'ngarnier',
        'prof10'
    );

INSERT INTO PROMO (
        nom_promo,
        annee_promo,
        formation_promo,
        id_enseignant
    )
VALUES ('BUT2', 2025, 'BUT Informatique', 1),
    ('BUT3', 2025, 'BUT Informatique', 2),
    ('BUT2', 2025, 'BUT GEA', 3);

INSERT INTO APPARTENIR (
        id_etudiant,
        nom_promo,
        annee_promo,
        regime_etudiant
    )
VALUES (1, 'BUT2', 2025, 'Formation initiale'),
    (2, 'BUT2', 2025, 'Formation initiale'),
    (3, 'BUT2', 2025, 'Formation initiale'),
    (4, 'BUT3', 2025, 'Formation apprentissage'),
    (10, 'BUT2', 2025, 'Formation initiale'),
    (5, 'BUT3', 2025, 'Formation apprentissage'),
    (6, 'BUT2', 2025, 'Formation initiale'),
    (7, 'BUT2', 2025, 'Formation initiale'),
    (8, 'BUT3', 2025, 'Formation apprentissage'),
    (9, 'BUT2', 2025, 'Formation initiale');

INSERT INTO TUTORER (id_enseignant, id_etudiant, annee)
VALUES (1, 1, 2025),
    (2, 2, 2025),
    (3, 3, 2025),
    (4, 4, 2025),
    (5, 5, 2025),
    (6, 6, 2025),
    (7, 10, 2025),
    (8, 4, 2025);

INSERT INTO MAITRE_STAGE (
        id_maitre,
        nom_maitre,
        prenom_maitre,
        civilite_maitre,
        tel_maitre,
        email_maitre,
        id_entreprise
    )
VALUES (
        1,
        'Dumas',
        'Philippe',
        'M.',
        '0145678913',
        'philippe.dumas@techsolutions.fr',
        1
    ),
    (
        2,
        'Lambert',
        'Sylvie',
        'Mme',
        '0478912346',
        'sylvie.lambert@datacorp.fr',
        2
    ),
    (
        3,
        'Carpentier',
        'Michel',
        'M.',
        '0491234568',
        'michel.carpentier@webinnovate.fr',
        3
    ),
    (
        4,
        'Faure',
        'Julie',
        'Mme',
        '0562347890',
        'julie.faure@aisystems.fr',
        4
    );

INSERT INTO DEMARCHE (
        id_demarche,
        source,
        typeD,
        situation,
        date_envoi,
        date_relance,
        resultat,
        raison_refus,
        cv,
        lettre_motiv,
        id_entreprise,
        id_etudiant
    )
VALUES (
        1,
        'Site entreprise',
        'Candidature spontanée',
        'Acceptée',
        '2025-09-15',
        NULL,
        'Stage obtenu',
        NULL,
        'cv_doe.pdf',
        'lm_doe.pdf',
        1,
        1
    ),
    (
        2,
        'LinkedIn',
        'Réponse à offre',
        'Refusée',
        '2025-09-10',
        '2025-09-25',
        'Refusé',
        'Profil junior',
        'cv_doe.pdf',
        'lm_doe2.pdf',
        2,
        5
    ),
    (
        3,
        'Salon',
        'Contact direct',
        'En cours',
        '2025-09-20',
        NULL,
        NULL,
        NULL,
        'cv_smith.pdf',
        'lm_smith.pdf',
        3,
        2
    ),
    (
        4,
        'Indeed',
        'Réponse à offre',
        'Acceptée',
        '2025-09-12',
        NULL,
        'Stage obtenu',
        NULL,
        'cv_brown.pdf',
        'lm_brown.pdf',
        4,
        3
    ),
    (
        5,
        'Entreprise',
        'Candidature spontanée',
        'Acceptée',
        '2025-09-01',
        NULL,
        'Stage obtenu',
        NULL,
        'cv_unknown.pdf',
        'lm_unknown.pdf',
        1,
        7
    ),
    (6,
    'LinkedIn',
    'Réponse à offre',
    'Acceptée',
    '2025-11-01',
    NULL,
    'Stage obtenu',
    NULL,
    'cv_unknown.pdf',
    'lm_unknown.pdf',
    1,
    10),
    (
        7,
        'Import',
        'Création manuelle',
        'Acceptée',
        '2025-12-01',
        NULL,
        'Stage obtenu',
        NULL,
        'cv_martin.pdf',
        'lm_martin.pdf',
        1,
        4
    ),
    (
        8,
        'Import',
        'Création manuelle',
        'Acceptée',
        '2025-12-01',
        NULL,
        'Stage obtenu',
        NULL,
        'cv_wilson.pdf',
        'lm_wilson.pdf',
        1,
        5
    );

INSERT INTO STAGE (
        id_stage,
        typeS,
        date_debut,
        date_fin,
        duree_stage,
        unite_duree,
        titre_stage,
        theme_stage,
        id_maitre,
        id_demarche
    )
VALUES (
        1,
        'Stage de fin études',
        '2025-10-01',
        '2025-03-31',
        6,
        'mois',
        'Développer une application web de gestion',
        'Développement Full-Stack',
        1,
        1
    ),
    (
        2,
        'Stage de deuxième année',
        '2025-10-15',
        '2025-04-15',
        6,
        'mois',
        'Analyse de données massives pour la prédiction',
        'Big Data et Machine Learning',
        2,
        4
    ),
    (
        3,
        'Stage initiation',
        '2025-05-01',
        '2025-07-31',
        3,
        'mois',
        'Découverte du développement front-end',
        'Web & UX',
        3,
        2
    ),
    (
        4,
        'Stage approfondissement',
        '2025-01-10',
        '2025-06-30',
        6,
        'mois',
        'Conception d''un agent conversationnel',
        'IA & NLP',
        4,
        3
    ),
    (
        5,
        'Stage professionnel',
        '2025-04-01',
        '2025-06-30',
        3,
        'mois',
        'Projet spécial',
        'Développement',
        1,
        5
    ),
    (6,
    'Stage BUT2',
    '2025-12-01',
    '2026-02-01',
    2,
    'mois',
    'Sujet Noah',
    'Dev',
    1,
    6),
    (
        7,
        'Stage professionnel',
        '2025-12-01',
        '2026-02-01',
        2,
        'mois',
        'Stage auto Lucas Martin',
        'Général',
        NULL,
        7
    ),
    (
        8,
        'Stage professionnel',
        '2025-12-01',
        '2026-02-01',
        2,
        'mois',
        'Stage auto Emma Wilson',
        'Général',
        NULL,
        8
    );

INSERT INTO SOUTENANCE (
        id_soutenance,
        salle,
        nom_bat,
        dateS,
        h_debut,
        h_fin,
        id_stage
    )
VALUES (
        1,
        101,
        'Bâtiment A',
        '2025-03-25',
        '09:00',
        '09:45',
        1
    ),
    (
        2,
        101,
        'Bâtiment A',
        '2025-03-25',
        '09:00',
        '09:45',
        2
    ),
    (
        3,
        101,
        'Bâtiment A',
        '2025-03-25',
        '09:00',
        '09:45',
        3
    ),
    (
        4,
        104,
        'Bâtiment C',
        '2025-06-20',
        '11:00',
        '11:45',
        4
    ),
    (
        5,
        102,
        'Bâtiment B',
        '2025-03-25',
        '08:00',
        '09:45',
        5
    );

INSERT INTO JURY (
        id_jury,
        date_jury,
        h_jury,
        duree_jury,
        id_soutenance
    )
VALUES (1, '2025-03-25', '09:00', 45, 1),
    (2, '2025-03-25', '09:00', 45, 2),
    (3, '2025-03-25', '09:00', 45, 3),
    (4, '2025-06-20', '11:00', 45, 4),
    (5, '2025-03-25', '09:00', 45, 5);

INSERT INTO COMPOSER (id_enseignant, id_soutenance)
VALUES -- Jury (profs 1,2,3) assigned to soutenances 1,2,3 (same jury for these sessions)
    (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (1, 3),
    (2, 3),
    (3, 3),
    -- jury for soutenance 4 (single prof)
    (4, 4),
    -- jury for soutenance 5 (different jury, same day/time as 1-3)
    (4, 5),
    (5, 5);

INSERT INTO ADMINI (
        id_admin,
        nom_admin,
        prenom_admin,
        login_admin,
        pwd_admin
    )
VALUES (
        'A001',
        'Biscuit',
        'Nathalie',
        'nbiscuit',
        'nbiscuitpass'
    ),
    (
        'A002',
        'Soler',
        'Alvaro',
        'aSoler',
        'aSolerpass'
    );

INSERT INTO ASSEMBLER (id_jury, id_admin)
VALUES (1, 'A001'),
    (2, 'A002'),
    (3, 'A001'),
    (4, 'A002');