-- Script d'insertion de données pour la base appsoutenance

-- ============================
-- INSERTION DES ENSEIGNANTS (10)
-- ============================
INSERT INTO ENSEIGNANT (id_enseignant, nom_enseignant, prenom_enseignant, civilite_enseignant, email_enseignant, login_enseignant, pwd_enseignant) VALUES
(1, 'Dubois', 'Jean', 'M.', 'jean.dubois@univ.fr', 'jdubois', 'prof1'),
(2, 'Martin', 'Sophie', 'Mme', 'sophie.martin@univ.fr', 'smartin', 'prof2'),
(3, 'Lefebvre', 'Pierre', 'M.', 'pierre.lefebvre@univ.fr', 'plefebvre', 'prof3'),
(4, 'Rousseau', 'Marie', 'Mme', 'marie.rousseau@univ.fr', 'mrousseau', 'prof4'),
(5, 'Bernard', 'Luc', 'M.', 'luc.bernard@univ.fr', 'lbernard', 'prof5'),
(6, 'Thomas', 'Claire', 'Mme', 'claire.thomas@univ.fr', 'cthomas', 'prof6'),
(7, 'Petit', 'François', 'M.', 'francois.petit@univ.fr', 'fpetit', 'prof7'),
(8, 'Robert', 'Anne', 'Mme', 'anne.robert@univ.fr', 'arobert', 'prof8'),
(9, 'Richard', 'Marc', 'M.', 'marc.richard@univ.fr', 'mrichard', 'prof9'),
(10, 'Durand', 'Isabelle', 'Mme', 'isabelle.durand@univ.fr', 'idurand', 'prof10'),
(11, 'Leroy', 'David', 'M.', 'david.leroy@univ.fr', 'dleroy', 'prof11'),
(12, 'Moreau', 'Céline', 'Mme', 'celine.moreau@univ.fr', 'cmoreau', 'prof12'),
(13, 'Simon', 'Julien', 'M.', 'julien.simon@univ.fr', 'jsimon', 'prof13'),
(14, 'Laurent', 'Audrey', 'Mme', 'audrey.laurent@univ.fr', 'alaurent', 'prof14'),
(15, 'Lefevre', 'Nicolas', 'M.', 'nicolas.lefevre@univ.fr', 'nlefevre', 'prof15'),
(16, 'Michel', 'Sandrine', 'Mme', 'sandrine.michel@univ.fr', 'smichel', 'prof16'),
(17, 'Garcia', 'Luis', 'M.', 'luis.garcia@univ.fr', 'lgarcia', 'prof17'),
(18, 'Martinez', 'Elena', 'Mme', 'elena.martinez@univ.fr', 'emartinez', 'prof18'),
(19, 'Robinson', 'Paul', 'M.', 'paul.robinson@univ.fr', 'probinson', 'prof19'),
(20, 'Clark', 'Sarah', 'Mme', 'sarah.clark@univ.fr', 'sclark', 'prof20');

-- ============================
-- INSERTION DES ADMINS
-- ============================
INSERT INTO ADMINI (id_admin, nom_admin, prenom_admin, login_admin, pwd_admin) VALUES
('A001', 'Biscuit', 'Nathalie', 'nbiscuit', 'nbiscuitpass'),
('A002', 'Soler', 'Alvaro', 'aSoler', 'aSolerpass');

-- ============================
-- INSERTION DES PROMOTIONS
-- ============================
INSERT INTO PROMO (nom_promo, annee_promo, formation_promo, id_enseignant) VALUES
('BUT2', 2025, 'BUT Informatique', 1),
('BUT3', 2025, 'BUT Informatique', 2);

-- ============================
-- INSERTION DES ÉTUDIANTS (24 au total)
-- ============================

-- 8 étudiants BUT3 2025 (qui étaient en BUT2 2025)
INSERT INTO ETUDIANT (id_etudiant, nom_etudiant, prenom_etudiant, date_naissance, civilite_etudiant, telephone_etudiant, email_etudiant, login_etudiant, pwd_etudiant) VALUES
(1, 'Dupont', 'Alexandre', '2003-05-12', 'M.', '0612345678', 'alexandre.dupont@edu.fr', 'adupont', 'pass1'),
(2, 'Moreau', 'Camille', '2003-08-24', 'Mme', '0623456789', 'camille.moreau@edu.fr', 'cmoreau', 'pass2'),
(3, 'Laurent', 'Thomas', '2002-11-03', 'M.', '0634567812', 'thomas.laurent@edu.fr', 'tlaurent', 'pass3'),
(4, 'Simon', 'Julie', '2003-02-17', 'Mme', '0645678923', 'julie.simon@edu.fr', 'jsimon', 'pass4'),
(5, 'Michel', 'Lucas', '2003-07-09', 'M.', '0656789134', 'lucas.michel@edu.fr', 'lmichel', 'pass5'),
(6, 'Leroy', 'Emma', '2002-12-21', 'Mme', '0667891245', 'emma.leroy@edu.fr', 'eleroy', 'pass6'),
(7, 'Fournier', 'Hugo', '2003-04-15', 'M.', '0678912356', 'hugo.fournier@edu.fr', 'hfournier', 'pass7'),
(8, 'Girard', 'Léa', '2003-09-28', 'Mme', '0689123467', 'lea.girard@edu.fr', 'lgirard', 'pass8'),

-- 8 étudiants BUT2 2025
(9, 'Bonnet', 'Antoine', '2004-03-14', 'M.', '0691234578', 'antoine.bonnet@edu.fr', 'abonnet', 'pass9'),
(10, 'Blanc', 'Sarah', '2004-06-22', 'Mme', '0612345987', 'sarah.blanc@edu.fr', 'sblanc', 'pass10'),
(11, 'Garnier', 'Maxime', '2004-01-08', 'M.', '0623456198', 'maxime.garnier@edu.fr', 'mgarnier', 'pass11'),
(12, 'Faure', 'Chloé', '2004-10-19', 'Mme', '0634567219', 'chloe.faure@edu.fr', 'cfaure', 'pass12'),
(13, 'Roussel', 'Nathan', '2004-05-30', 'M.', '0645678321', 'nathan.roussel@edu.fr', 'nroussel', 'pass13'),
(14, 'Vincent', 'Manon', '2004-08-11', 'Mme', '0656789432', 'manon.vincent@edu.fr', 'mvincent', 'pass14'),
(15, 'Muller', 'Arthur', '2004-02-25', 'M.', '0667891543', 'arthur.muller@edu.fr', 'amuller', 'pass15'),
(16, 'Lefevre', 'Jade', '2004-07-07', 'Mme', '0678912654', 'jade.lefevre@edu.fr', 'jlefevre', 'pass16'),

-- 8 étudiants BUT2 2025 (mêmes que BUT3 2025 mais dans leur ancienne promo)
(17, 'Mercier', 'Paul', '2004-11-16', 'M.', '0689123765', 'paul.mercier@edu.fr', 'pmercier', 'pass17'),
(18, 'Lemoine', 'Louise', '2004-04-02', 'Mme', '0691234876', 'louise.lemoine@edu.fr', 'llemoine', 'pass18'),
(19, 'Andre', 'Theo', '2004-09-13', 'M.', '0612348765', 'theo.andre@edu.fr', 'tandre', 'pass19'),
(20, 'Roux', 'Clara', '2004-12-28', 'Mme', '0623459876', 'clara.roux@edu.fr', 'croux', 'pass20'),
(21, 'David', 'Victor', '2005-03-05', 'M.', '0634561987', 'victor.david@edu.fr', 'vdavid', 'pass21'),
(22, 'Bertrand', 'Zoé', '2005-06-18', 'Mme', '0645672198', 'zoe.bertrand@edu.fr', 'zbertrand', 'pass22'),
(23, 'Morel', 'Gabriel', '2005-01-21', 'M.', '0656783219', 'gabriel.morel@edu.fr', 'gmorel', 'pass23'),
(24, 'Fontaine', 'Alice', '2005-08-09', 'Mme', '0667894321', 'alice.fontaine@edu.fr', 'afontaine', 'pass24'),
-- Nouveaux étudiants pour atteindre 120 (70 BUT2 + 50 BUT3)
(25, 'Guerin', 'Lucas', '2005-02-10', 'M.', '0600000025', 'lucas.guerin@edu.fr', 'lguerin', 'pass25'),
(26, 'Rousseau', 'Manon', '2005-03-15', 'Mme', '0600000026', 'manon.rousseau@edu.fr', 'mrousseau', 'pass26'),
(27, 'Blanc', 'Théo', '2005-04-20', 'M.', '0600000027', 'theo.blanc@edu.fr', 'tblanc', 'pass27'),
(28, 'Garnier', 'Léa', '2005-05-25', 'Mme', '0600000028', 'lea.garnier@edu.fr', 'lgarnier', 'pass28'),
(29, 'Chevalier', 'Hugo', '2005-06-30', 'M.', '0600000029', 'hugo.chevalier@edu.fr', 'hchevalier', 'pass29'),
(30, 'Francois', 'Emma', '2005-07-05', 'Mme', '0600000030', 'emma.francois@edu.fr', 'efrancois', 'pass30'),
(31, 'Legrand', 'Enzo', '2005-08-10', 'M.', '0600000031', 'enzo.legrand@edu.fr', 'elegrand', 'pass31'),
(32, 'Gauthier', 'Jade', '2005-09-15', 'Mme', '0600000032', 'jade.gauthier@edu.fr', 'jgauthier', 'pass32'),
(33, 'Perrin', 'Nathan', '2005-10-20', 'M.', '0600000033', 'nathan.perrin@edu.fr', 'nperrin', 'pass33'),
(34, 'Robin', 'Chloé', '2005-11-25', 'Mme', '0600000034', 'chloe.robin@edu.fr', 'crobin', 'pass34'),
(35, 'Clement', 'Arthur', '2005-12-30', 'M.', '0600000035', 'arthur.clement@edu.fr', 'aclement', 'pass35'),
(36, 'Morin', 'Sarah', '2006-01-04', 'Mme', '0600000036', 'sarah.morin@edu.fr', 'smorin', 'pass36'),
(37, 'Nicolas', 'Louis', '2006-02-09', 'M.', '0600000037', 'louis.nicolas@edu.fr', 'lnicolas', 'pass37'),
(38, 'Henry', 'Inès', '2006-03-14', 'Mme', '0600000038', 'ines.henry@edu.fr', 'ihenry', 'pass38'),
(39, 'Roussel', 'Gabriel', '2006-04-19', 'M.', '0600000039', 'gabriel.roussel@edu.fr', 'groussel', 'pass39'),
(40, 'Mathieu', 'Lola', '2006-05-24', 'Mme', '0600000040', 'lola.mathieu@edu.fr', 'lmathieu', 'pass40'),
(41, 'Gautier', 'Jules', '2006-06-29', 'M.', '0600000041', 'jules.gautier@edu.fr', 'jgautier', 'pass41'),
(42, 'Masson', 'Clara', '2006-07-04', 'Mme', '0600000042', 'clara.masson@edu.fr', 'cmasson', 'pass42'),
(43, 'Marchand', 'Paul', '2006-08-09', 'M.', '0600000043', 'paul.marchand@edu.fr', 'pmarchand', 'pass43'),
(44, 'Duval', 'Louise', '2006-09-14', 'Mme', '0600000044', 'louise.duval@edu.fr', 'lduval', 'pass44'),
(45, 'Denis', 'Adam', '2006-10-19', 'M.', '0600000045', 'adam.denis@edu.fr', 'adenis', 'pass45'),
(46, 'Dumont', 'Alice', '2006-11-24', 'Mme', '0600000046', 'alice.dumont@edu.fr', 'adumont', 'pass46'),
(47, 'Marie', 'Mohamed', '2006-12-29', 'M.', '0600000047', 'mohamed.marie@edu.fr', 'mmarie', 'pass47'),
(48, 'Lemaire', 'Lina', '2007-01-03', 'Mme', '0600000048', 'lina.lemaire@edu.fr', 'llemaire', 'pass48'),
(49, 'Noel', 'Tom', '2007-02-08', 'M.', '0600000049', 'tom.noel@edu.fr', 'tnoel', 'pass49'),
(50, 'Meyer', 'Mila', '2007-03-15', 'Mme', '0600000050', 'mila.meyer@edu.fr', 'mmeyer', 'pass50'),
(51, 'Dufour', 'Rayan', '2005-01-01', 'M.', '0600000051', 'rayan.dufour@edu.fr', 'rdufour', 'pass51'),
(52, 'Meunier', 'Anna', '2005-01-02', 'Mme', '0600000052', 'anna.meunier@edu.fr', 'ameunier', 'pass52'),
(53, 'Brun', 'Leo', '2005-01-03', 'M.', '0600000053', 'leo.brun@edu.fr', 'lbrun', 'pass53'),
(54, 'Blanchard', 'Zoe', '2005-01-04', 'Mme', '0600000054', 'zoe.blanchard@edu.fr', 'zblanchard', 'pass54'),
(55, 'Giraud', 'Axel', '2005-01-05', 'M.', '0600000055', 'axel.giraud@edu.fr', 'agiraud', 'pass55'),
(56, 'Joly', 'Julia', '2005-01-06', 'Mme', '0600000056', 'julia.joly@edu.fr', 'jjoly', 'pass56'),
(57, 'Riviere', 'Evan', '2005-01-07', 'M.', '0600000057', 'evan.riviere@edu.fr', 'eriviere', 'pass57'),
(58, 'Lucas', 'Maeva', '2005-01-08', 'Mme', '0600000058', 'maeva.lucas@edu.fr', 'mlucas', 'pass58'),
(59, 'Brunet', 'Noa', '2005-01-09', 'M.', '0600000059', 'noa.brunet@edu.fr', 'nbrunet', 'pass59'),
(60, 'Gaillard', 'Rose', '2005-01-10', 'Mme', '0600000060', 'rose.gaillard@edu.fr', 'rgaillard', 'pass60'),
(61, 'Barbier', 'Sacha', '2005-01-11', 'M.', '0600000061', 'sacha.barbier@edu.fr', 'sbarbier', 'pass61'),
(62, 'Arnaud', 'Nina', '2005-01-12', 'Mme', '0600000062', 'nina.arnaud@edu.fr', 'narnaud', 'pass62'),
(63, 'Martinez', 'Aaron', '2005-01-13', 'M.', '0600000063', 'aaron.martinez@edu.fr', 'amartinez', 'pass63'),
(64, 'Gerard', 'Sara', '2005-01-14', 'Mme', '0600000064', 'sara.gerard@edu.fr', 'sgerard', 'pass64'),
(65, 'Roche', 'Mael', '2005-01-15', 'M.', '0600000065', 'mael.roche@edu.fr', 'mroche', 'pass65'),
(66, 'Renard', 'Lucie', '2005-01-16', 'Mme', '0600000066', 'lucie.renard@edu.fr', 'lrenard', 'pass66'),
(67, 'Schmitt', 'Timéo', '2005-01-17', 'M.', '0600000067', 'timeo.schmitt@edu.fr', 'tschmitt', 'pass67'),
(68, 'Roy', 'Maya', '2005-01-18', 'Mme', '0600000068', 'maya.roy@edu.fr', 'mroy', 'pass68'),
(69, 'Leroux', 'Liam', '2005-01-19', 'M.', '0600000069', 'liam.leroux@edu.fr', 'lleroux', 'pass69'),
(70, 'Jean', 'Iris', '2005-01-20', 'Mme', '0600000070', 'iris.jean@edu.fr', 'ijean', 'pass70'),
(71, 'Muller', 'Kylian', '2004-01-01', 'M.', '0600000071', 'kylian.muller@edu.fr', 'kmuller', 'pass71'),
(72, 'Lefebvre', 'Eva', '2004-01-02', 'Mme', '0600000072', 'eva.lefebvre@edu.fr', 'elefebvre', 'pass72'),
(73, 'Vidal', 'Yanis', '2004-01-03', 'M.', '0600000073', 'yanis.vidal@edu.fr', 'yvidal', 'pass73'),
(74, 'Morel', 'Ambre', '2004-01-04', 'Mme', '0600000074', 'ambre.morel@edu.fr', 'amorel', 'pass74'),
(75, 'Chevalier', 'Mathis', '2004-01-05', 'M.', '0600000075', 'mathis.chevalier@edu.fr', 'mchevalier', 'pass75'),
(76, 'Francois', 'Agathe', '2004-01-06', 'Mme', '0600000076', 'agathe.francois@edu.fr', 'afrancois', 'pass76'),
(77, 'Legrand', 'Nolan', '2004-01-07', 'M.', '0600000077', 'nolan.legrand@edu.fr', 'nlegrand', 'pass77'),
(78, 'Gauthier', 'Elena', '2004-01-08', 'Mme', '0600000078', 'elena.gauthier@edu.fr', 'egauthier', 'pass78'),
(79, 'Perrin', 'Diego', '2004-01-09', 'M.', '0600000079', 'diego.perrin@edu.fr', 'dperrin', 'pass79'),
(80, 'Robin', 'Margaux', '2004-01-10', 'Mme', '0600000080', 'margaux.robin@edu.fr', 'mrobin', 'pass80'),
(81, 'Clement', 'Victor', '2004-01-11', 'M.', '0600000081', 'victor.clement@edu.fr', 'vclement', 'pass81'),
(82, 'Morin', 'Salomé', '2004-01-12', 'Mme', '0600000082', 'salome.morin@edu.fr', 'smorin', 'pass82'),
(83, 'Nicolas', 'Basile', '2004-01-13', 'M.', '0600000083', 'basile.nicolas@edu.fr', 'bnicolas', 'pass83'),
(84, 'Henry', 'Romane', '2004-01-14', 'Mme', '0600000084', 'romane.henry@edu.fr', 'rhenry', 'pass84'),
(85, 'Roussel', 'Marius', '2004-01-15', 'M.', '0600000085', 'marius.roussel@edu.fr', 'mroussel', 'pass85'),
(86, 'Mathieu', 'Camille', '2004-01-16', 'Mme', '0600000086', 'camille.mathieu@edu.fr', 'cmathieu', 'pass86'),
(87, 'Gautier', 'Oscar', '2004-01-17', 'M.', '0600000087', 'oscar.gautier@edu.fr', 'ogautier', 'pass87'),
(88, 'Masson', 'Léonie', '2004-01-18', 'Mme', '0600000088', 'leonie.masson@edu.fr', 'lmasson', 'pass88'),
(89, 'Marchand', 'Gabin', '2004-01-19', 'M.', '0600000089', 'gabin.marchand@edu.fr', 'gmarchand', 'pass89'),
(90, 'Duval', 'Clémence', '2004-01-20', 'Mme', '0600000090', 'clemence.duval@edu.fr', 'cduval', 'pass90'),
(91, 'Denis', 'Simon', '2004-01-21', 'M.', '0600000091', 'simon.denis@edu.fr', 'sdenis', 'pass91'),
(92, 'Dumont', 'Élise', '2004-01-22', 'Mme', '0600000092', 'elise.dumont@edu.fr', 'edumont', 'pass92'),
(93, 'Marie', 'Paul', '2004-01-23', 'M.', '0600000093', 'paul.marie@edu.fr', 'pmarie', 'pass93'),
(94, 'Lemaire', 'Clara', '2004-01-24', 'Mme', '0600000094', 'clara.lemaire@edu.fr', 'clemaire', 'pass94'),
(95, 'Noel', 'Arthur', '2004-01-25', 'M.', '0600000095', 'arthur.noel@edu.fr', 'anoel', 'pass95'),
(96, 'Meyer', 'Manon', '2004-01-26', 'Mme', '0600000096', 'manon.meyer@edu.fr', 'mmeyer', 'pass96'),
(97, 'Dufour', 'Louis', '2004-01-27', 'M.', '0600000097', 'louis.dufour@edu.fr', 'ldufour', 'pass97'),
(98, 'Meunier', 'Chloé', '2004-01-28', 'Mme', '0600000098', 'chloe.meunier@edu.fr', 'cmeunier', 'pass98'),
(99, 'Brun', 'Jules', '2004-01-29', 'M.', '0600000099', 'jules.brun@edu.fr', 'jbrun', 'pass99'),
(100, 'Blanchard', 'Emma', '2004-01-30', 'Mme', '0600000100', 'emma.blanchard@edu.fr', 'eblanchard', 'pass100'),
(101, 'Giraud', 'Hugo', '2004-02-01', 'M.', '0600000101', 'hugo.giraud@edu.fr', 'hgiraud', 'pass101'),
(102, 'Joly', 'Léa', '2004-02-02', 'Mme', '0600000102', 'lea.joly@edu.fr', 'ljoly', 'pass102'),
(103, 'Riviere', 'Nathan', '2004-02-03', 'M.', '0600000103', 'nathan.riviere@edu.fr', 'nriviere', 'pass103'),
(104, 'Lucas', 'Jade', '2004-02-04', 'Mme', '0600000104', 'jade.lucas@edu.fr', 'jlucas', 'pass104'),
(105, 'Brunet', 'Enzo', '2004-02-05', 'M.', '0600000105', 'enzo.brunet@edu.fr', 'ebrunet', 'pass105'),
(106, 'Gaillard', 'Mila', '2004-02-06', 'Mme', '0600000106', 'mila.gaillard@edu.fr', 'mgaillard', 'pass106'),
(107, 'Barbier', 'Théo', '2004-02-07', 'M.', '0600000107', 'theo.barbier@edu.fr', 'tbarbier', 'pass107'),
(108, 'Arnaud', 'Anna', '2004-02-08', 'Mme', '0600000108', 'anna.arnaud@edu.fr', 'aarnaud', 'pass108'),
(109, 'Martinez', 'Rayan', '2004-02-09', 'M.', '0600000109', 'rayan.martinez@edu.fr', 'rmartinez', 'pass109'),
(110, 'Gerard', 'Julia', '2004-02-10', 'Mme', '0600000110', 'julia.gerard@edu.fr', 'jgerard', 'pass110'),
(111, 'Roche', 'Evan', '2004-02-11', 'M.', '0600000111', 'evan.roche@edu.fr', 'eroche', 'pass111'),
(112, 'Renard', 'Maeva', '2004-02-12', 'Mme', '0600000112', 'maeva.renard@edu.fr', 'mrenard', 'pass112'),
(113, 'Schmitt', 'Noa', '2004-02-13', 'M.', '0600000113', 'noa.schmitt@edu.fr', 'nschmitt', 'pass113'),
(114, 'Roy', 'Rose', '2004-02-14', 'Mme', '0600000114', 'rose.roy@edu.fr', 'rroy', 'pass114'),
(115, 'Leroux', 'Sacha', '2004-02-15', 'M.', '0600000115', 'sacha.leroux@edu.fr', 'sleroux', 'pass115'),
(116, 'Jean', 'Nina', '2004-02-16', 'Mme', '0600000116', 'nina.jean@edu.fr', 'njean', 'pass116'),
(117, 'Muller', 'Aaron', '2004-02-17', 'M.', '0600000117', 'aaron.muller@edu.fr', 'amuller', 'pass117'),
(118, 'Lefebvre', 'Sara', '2004-02-18', 'Mme', '0600000118', 'sara.lefebvre@edu.fr', 'slefebvre', 'pass118'),
(119, 'Vidal', 'Mael', '2004-02-19', 'M.', '0600000119', 'mael.vidal@edu.fr', 'mvidal', 'pass119'),
(120, 'Morel', 'Lucie', '2004-02-20', 'Mme', '0600000120', 'lucie.morel@edu.fr', 'lmorel', 'pass120');

-- ============================
-- APPARTENANCE AUX PROMOTIONS
-- ============================

INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant) VALUES
(1, 'BUT2', 2025, 'Formation initiale'),
(2, 'BUT2', 2025, 'Formation initiale'),
(3, 'BUT2', 2025, 'Alternance'),
(4, 'BUT2', 2025, 'Formation initiale'),
(5, 'BUT2', 2025, 'Formation initiale'),
(6, 'BUT2', 2025, 'Alternance'),
(7, 'BUT2', 2025, 'Formation initiale'),
(8, 'BUT2', 2025, 'Formation initiale'),

(9, 'BUT2', 2025, 'Formation initiale'),
(10, 'BUT2', 2025, 'Formation initiale'),
(11, 'BUT2', 2025, 'Alternance'),
(12, 'BUT2', 2025, 'Formation initiale'),
(13, 'BUT2', 2025, 'Formation initiale'),
(14, 'BUT2', 2025, 'Alternance'),
(15, 'BUT2', 2025, 'Formation initiale'),
(16, 'BUT2', 2025, 'Formation initiale'),

(17, 'BUT2', 2025, 'Formation initiale'),
(18, 'BUT2', 2025, 'Formation initiale'),
(19, 'BUT2', 2025, 'Alternance'),
(20, 'BUT2', 2025, 'Formation initiale'),
(21, 'BUT2', 2025, 'Formation initiale'),
(22, 'BUT2', 2025, 'Alternance'),
(23, 'BUT2', 2025, 'Formation initiale'),
(24, 'BUT2', 2025, 'Formation initiale');

INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant) VALUES
(25, 'BUT2', 2025, 'Formation initiale'), (26, 'BUT2', 2025, 'Formation initiale'), (27, 'BUT2', 2025, 'Formation initiale'), (28, 'BUT2', 2025, 'Formation initiale'), (29, 'BUT2', 2025, 'Formation initiale'),
(30, 'BUT2', 2025, 'Formation initiale'), (31, 'BUT2', 2025, 'Formation initiale'), (32, 'BUT2', 2025, 'Formation initiale'), (33, 'BUT2', 2025, 'Formation initiale'), (34, 'BUT2', 2025, 'Formation initiale'),
(35, 'BUT2', 2025, 'Formation initiale'), (36, 'BUT2', 2025, 'Formation initiale'), (37, 'BUT2', 2025, 'Formation initiale'), (38, 'BUT2', 2025, 'Formation initiale'), (39, 'BUT2', 2025, 'Formation initiale'),
(40, 'BUT2', 2025, 'Formation initiale'), (41, 'BUT2', 2025, 'Formation initiale'), (42, 'BUT2', 2025, 'Formation initiale'), (43, 'BUT2', 2025, 'Formation initiale'), (44, 'BUT2', 2025, 'Formation initiale'),
(45, 'BUT2', 2025, 'Formation initiale'), (46, 'BUT2', 2025, 'Formation initiale'), (47, 'BUT2', 2025, 'Formation initiale'), (48, 'BUT2', 2025, 'Formation initiale'), (49, 'BUT2', 2025, 'Formation initiale'),
(50, 'BUT2', 2025, 'Formation initiale'), (51, 'BUT2', 2025, 'Formation initiale'), (52, 'BUT2', 2025, 'Formation initiale'), (53, 'BUT2', 2025, 'Formation initiale'), (54, 'BUT2', 2025, 'Formation initiale'),
(55, 'BUT2', 2025, 'Formation initiale'), (56, 'BUT2', 2025, 'Formation initiale'), (57, 'BUT2', 2025, 'Formation initiale'), (58, 'BUT2', 2025, 'Formation initiale'), (59, 'BUT2', 2025, 'Formation initiale'),
(60, 'BUT2', 2025, 'Formation initiale'), (61, 'BUT2', 2025, 'Formation initiale'), (62, 'BUT2', 2025, 'Formation initiale'), (63, 'BUT2', 2025, 'Formation initiale'), (64, 'BUT2', 2025, 'Formation initiale'),
(65, 'BUT2', 2025, 'Formation initiale'), (66, 'BUT2', 2025, 'Formation initiale'), (67, 'BUT2', 2025, 'Formation initiale'), (68, 'BUT2', 2025, 'Formation initiale'), (69, 'BUT2', 2025, 'Formation initiale'),
(70, 'BUT2', 2025, 'Formation initiale');

INSERT INTO APPARTENIR (id_etudiant, nom_promo, annee_promo, regime_etudiant) VALUES
(71, 'BUT3', 2025, 'Formation initiale'), (72, 'BUT3', 2025, 'Formation initiale'), (73, 'BUT3', 2025, 'Formation initiale'), (74, 'BUT3', 2025, 'Formation initiale'), (75, 'BUT3', 2025, 'Formation initiale'),
(76, 'BUT3', 2025, 'Formation initiale'), (77, 'BUT3', 2025, 'Formation initiale'), (78, 'BUT3', 2025, 'Formation initiale'), (79, 'BUT3', 2025, 'Formation initiale'), (80, 'BUT3', 2025, 'Formation initiale'),
(81, 'BUT3', 2025, 'Formation initiale'), (82, 'BUT3', 2025, 'Formation initiale'), (83, 'BUT3', 2025, 'Formation initiale'), (84, 'BUT3', 2025, 'Formation initiale'), (85, 'BUT3', 2025, 'Formation initiale'),
(86, 'BUT3', 2025, 'Formation initiale'), (87, 'BUT3', 2025, 'Formation initiale'), (88, 'BUT3', 2025, 'Formation initiale'), (89, 'BUT3', 2025, 'Formation initiale'), (90, 'BUT3', 2025, 'Formation initiale'),
(91, 'BUT3', 2025, 'Formation initiale'), (92, 'BUT3', 2025, 'Formation initiale'), (93, 'BUT3', 2025, 'Formation initiale'), (94, 'BUT3', 2025, 'Formation initiale'), (95, 'BUT3', 2025, 'Formation initiale'),
(96, 'BUT3', 2025, 'Formation initiale'), (97, 'BUT3', 2025, 'Formation initiale'), (98, 'BUT3', 2025, 'Formation initiale'), (99, 'BUT3', 2025, 'Formation initiale'), (100, 'BUT3', 2025, 'Formation initiale'),
(101, 'BUT3', 2025, 'Formation initiale'), (102, 'BUT3', 2025, 'Formation initiale'), (103, 'BUT3', 2025, 'Formation initiale'), (104, 'BUT3', 2025, 'Formation initiale'), (105, 'BUT3', 2025, 'Formation initiale'),
(106, 'BUT3', 2025, 'Formation initiale'), (107, 'BUT3', 2025, 'Formation initiale'), (108, 'BUT3', 2025, 'Formation initiale'), (109, 'BUT3', 2025, 'Formation initiale'), (110, 'BUT3', 2025, 'Formation initiale'),
(111, 'BUT3', 2025, 'Formation initiale'), (112, 'BUT3', 2025, 'Formation initiale'), (113, 'BUT3', 2025, 'Formation initiale'), (114, 'BUT3', 2025, 'Formation initiale'), (115, 'BUT3', 2025, 'Formation initiale'),
(116, 'BUT3', 2025, 'Formation initiale'), (117, 'BUT3', 2025, 'Formation initiale'), (118, 'BUT3', 2025, 'Formation initiale'), (119, 'BUT3', 2025, 'Formation initiale'), (120, 'BUT3', 2025, 'Formation initiale');

-- ============================
-- TUTEURS (120 tuteurs, répartis sur 20 enseignants)
-- ============================
INSERT INTO TUTORER (id_enseignant, id_etudiant, annee) VALUES
(1, 1, 2025), (2, 2, 2025), (3, 3, 2025), (4, 4, 2025),
(5, 5, 2025), (6, 6, 2025), (7, 7, 2025), (8, 8, 2025),
(9, 9, 2025), (10, 10, 2025), (1, 11, 2025), (2, 12, 2025),
(3, 13, 2025), (4, 14, 2025), (5, 15, 2025), (6, 16, 2025),
(7, 17, 2025), (8, 18, 2025), (9, 19, 2025), (10, 20, 2025),
(1, 21, 2025), (2, 22, 2025), (3, 23, 2025), (4, 24, 2025),
(5, 25, 2025), (6, 26, 2025), (7, 27, 2025), (8, 28, 2025),
(9, 29, 2025), (10, 30, 2025), (11, 31, 2025), (12, 32, 2025),
(13, 33, 2025), (14, 34, 2025), (15, 35, 2025), (16, 36, 2025),
(17, 37, 2025), (18, 38, 2025), (19, 39, 2025), (20, 40, 2025),
(1, 41, 2025), (2, 42, 2025), (3, 43, 2025), (4, 44, 2025),
(5, 45, 2025), (6, 46, 2025), (7, 47, 2025), (8, 48, 2025),
(9, 49, 2025), (10, 50, 2025), (11, 51, 2025), (12, 52, 2025),
(13, 53, 2025), (14, 54, 2025), (15, 55, 2025), (16, 56, 2025),
(17, 57, 2025), (18, 58, 2025), (19, 59, 2025), (20, 60, 2025),
(1, 61, 2025), (2, 62, 2025), (3, 63, 2025), (4, 64, 2025),
(5, 65, 2025), (6, 66, 2025), (7, 67, 2025), (8, 68, 2025),
(9, 69, 2025), (10, 70, 2025), (11, 71, 2025), (12, 72, 2025),
(13, 73, 2025), (14, 74, 2025), (15, 75, 2025), (16, 76, 2025),
(17, 77, 2025), (18, 78, 2025), (19, 79, 2025), (20, 80, 2025),
(1, 81, 2025), (2, 82, 2025), (3, 83, 2025), (4, 84, 2025),
(5, 85, 2025), (6, 86, 2025), (7, 87, 2025), (8, 88, 2025),
(9, 89, 2025), (10, 90, 2025), (11, 91, 2025), (12, 92, 2025),
(13, 93, 2025), (14, 94, 2025), (15, 95, 2025), (16, 96, 2025),
(17, 97, 2025), (18, 98, 2025), (19, 99, 2025), (20, 100, 2025),
(1, 101, 2025), (2, 102, 2025), (3, 103, 2025), (4, 104, 2025),
(5, 105, 2025), (6, 106, 2025), (7, 107, 2025), (8, 108, 2025),
(9, 109, 2025), (10, 110, 2025), (11, 111, 2025), (12, 112, 2025),
(13, 113, 2025), (14, 114, 2025), (15, 115, 2025), (16, 116, 2025),
(17, 117, 2025), (18, 118, 2025), (19, 119, 2025), (20, 120, 2025);

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


INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(1, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-15', NULL, 'Stage obtenu', NULL, 'cv_dupont.pdf', 'lm_dupont.pdf', 1, 1),
(2, 'LinkedIn', 'Réponse à offre', 'Refusée', '2025-09-10', '2025-09-25', 'Refusé', 'Profil junior', 'cv_dupont.pdf', 'lm_dupont2.pdf', 2, 1),
(3, 'Salon', 'Contact direct', 'En attente', '2025-09-20', NULL, NULL, NULL, 'cv_dupont.pdf', 'lm_dupont3.pdf', 3, 1);


INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(4, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-12', NULL, 'Stage obtenu', NULL, 'cv_moreau.pdf', 'lm_moreau.pdf', 2, 2),
(5, 'Site entreprise', 'Candidature spontanée', 'Refusée', '2025-09-08', '2025-09-22', 'Refusé', 'Pas de place', 'cv_moreau.pdf', 'lm_moreau2.pdf', 4, 2);

INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(6, 'Réseau personnel', 'Recommandation', 'Acceptée', '2025-09-18', NULL, 'Stage obtenu', NULL, 'cv_laurent.pdf', 'lm_laurent.pdf', 3, 3),
(7, 'Indeed', 'Réponse à offre', 'Refusée', '2025-09-05', NULL, 'Refusé', 'Niveau insuffisant', 'cv_laurent.pdf', 'lm_laurent2.pdf', 5, 3),
(8, 'LinkedIn', 'Réponse à offre', 'En attente', '2025-09-25', NULL, NULL, NULL, 'cv_laurent.pdf', 'lm_laurent3.pdf', 6, 3);

INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(9, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-14', NULL, 'Stage obtenu', NULL, 'cv_bonnet.pdf', 'lm_bonnet.pdf', 4, 9),
(10, 'Salon', 'Contact direct', 'Refusée', '2025-09-11', NULL, 'Refusé', 'Budget limité', 'cv_bonnet.pdf', 'lm_bonnet2.pdf', 7, 9);

INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(11, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-16', NULL, 'Stage obtenu', NULL, 'cv_blanc.pdf', 'lm_blanc.pdf', 5, 10),
(12, 'LinkedIn', 'Réponse à offre', 'En attente', '2025-09-22', NULL, NULL, NULL, 'cv_blanc.pdf', 'lm_blanc2.pdf', 8, 10),
(13, 'Site entreprise', 'Candidature spontanée', 'Refusée', '2025-09-07', '2025-09-21', 'Refusé', 'Profil inadapté', 'cv_blanc.pdf', 'lm_blanc3.pdf', 1, 10);

INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre_motiv, id_entreprise, id_etudiant) VALUES
(14, 'Réseau personnel', 'Recommandation', 'Acceptée', '2025-09-19', NULL, 'Stage obtenu', NULL, 'cv_garnier.pdf', 'lm_garnier.pdf', 6, 11);

-- ============================
-- STAGES (19 étudiants avec stage, 5 sans)
-- Étudiants SANS stage : 4, 5, 7, 8, 17
-- ============================

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(1, 'Stage de fin d''études', '2025-10-01', '2025-03-31', 6, 'mois', 'Développement d''une application web de gestion', 'Développement Full-Stack', 1, 1),
(2, 'Stage de fin d''études', '2025-10-15', '2025-04-15', 6, 'mois', 'Analyse de données massives pour la prédiction', 'Big Data et Machine Learning', 2, 4),
(3, 'Stage de fin d''études', '2025-10-01', '2025-03-31', 6, 'mois', 'Création d''un site e-commerce responsive', 'Développement Web', 3, 6);

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(4, 'Stage de fin d''études', '2025-10-15', '2025-04-15', 6, 'mois', 'Développement d''applications mobiles iOS/Android', 'Mobile Development', 6, 15);

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(5, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Mise en place d''une infrastructure sécurisée', 'Cybersécurité et Réseaux', 4, 9),
(6, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Migration vers le Cloud AWS', 'Cloud Computing', 5, 11),
(7, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Développement d''une application mobile de fitness', 'Applications mobiles', 6, 14);

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(8, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d''un ERP sur mesure', 'Développement logiciel', 7, 16),
(9, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Transformation digitale des processus internes', 'Digital & Innovation', 8, 17),
(10, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d''une plateforme web collaborative', 'Développement Web', 9, 18),
(11, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Optimisation des performances d''applications', 'Performance & Big Data', 10, 19);

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
(12, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Création d''interfaces utilisateur modernes', 'UX/UI Design', 1, 20),
(13, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Analyse de données clients pour le marketing', 'Data Analytics', 2, 21),
(14, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d''API REST pour microservices', 'Architecture logicielle', 3, 22),
(15, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Mise en place d''une solution IoT', 'Internet des Objets', 4, 23),
(16, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d''un chatbot intelligent', 'Intelligence Artificielle', 5, 24),
(17, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Automatisation des tests logiciels', 'QA & Testing', 6, 25),
(18, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement d''un système de monitoring', 'DevOps', 7, 26),
(19, 'Stage professionnel', '2025-04-15', '2025-07-15', 3, 'mois', 'Création d''un CMS personnalisé', 'Développement Web', 8, 27);

-- ============================
-- SOUTENANCES (pour les étudiants BUT3 2025 et certains BUT2 2025)
-- Seulement 12 soutenances sur 19 stages
-- ============================

INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
(1, 101, 'Bâtiment A', '2025-04-15', '09:00', '10:30', 1),
(2, 102, 'Bâtiment A', '2025-04-15', '14:00', '15:30', 2),
(3, 103, 'Bâtiment B', '2025-04-16', '09:00', '10:30', 3),
(4, 104, 'Bâtiment B', '2025-04-16', '14:00', '15:30', 4);

INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
(5, 201, 'Bâtiment C', '2025-07-01', '09:00', '10:00', 12),
(6, 202, 'Bâtiment C', '2025-07-01', '10:30', '11:30', 13),
(7, 203, 'Bâtiment C', '2025-07-01', '14:00', '15:00', 14),
(8, 204, 'Bâtiment C', '2025-07-02', '09:00', '10:00', 15),
(9, 201, 'Bâtiment C', '2025-07-02', '10:30', '11:30', 16),
(10, 202, 'Bâtiment C', '2025-07-02', '14:00', '15:00', 17),
(11, 203, 'Bâtiment C', '2025-07-03', '09:00', '10:00', 18),
(12, 204, 'Bâtiment C', '2025-07-03', '10:30', '11:30', 19);

-- ============================
-- JURYS (un jury par soutenance)
-- ============================
INSERT INTO JURY (id_jury, date_jury, h_jury, duree, id_soutenance) VALUES
(1, '2025-04-15', '09:00', 90, 1),
(2, '2025-04-15', '14:00', 90, 2),
(3, '2025-04-16', '09:00', 90, 3),
(4, '2025-04-16', '14:00', 90, 4),
(5, '2025-07-01', '09:00', 60, 5),
(6, '2025-07-01', '10:30', 60, 6),
(7, '2025-07-01', '14:00', 60, 7),
(8, '2025-07-02', '09:00', 60, 8),
(9, '2025-07-02', '10:30', 60, 9),
(10, '2025-07-02', '14:00', 60, 10),
(11, '2025-07-03', '09:00', 60, 11),
(12, '2025-07-03', '10:30', 60, 12);

-- ============================
-- COMPOSER (au moins 2 enseignants par jury)
-- ============================

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(1, 1),  -- Tuteur
(3, 1),  -- Autre enseignant
(5, 1);  -- Troisième enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(2, 2),  -- Tuteur
(4, 2),  -- Autre enseignant
(6, 2);  -- Troisième enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(3, 3),  -- Tuteur
(1, 3),  -- Autre enseignant
(7, 3);  -- Troisième enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(6, 4),  -- Tuteur
(2, 4),  -- Autre enseignant
(8, 4);  -- Troisième enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(8, 5),  -- Tuteur
(9, 5);  -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(9, 6),  -- Tuteur
(10, 6); -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(10, 7), -- Tuteur
(1, 7);  -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(1, 8),  -- Tuteur
(2, 8);  -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(2, 9),  -- Tuteur
(3, 9);  -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(3, 10), -- Tuteur
(4, 10); -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(4, 11), -- Tuteur
(5, 11); -- Autre enseignant

INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
(6, 12), -- Tuteur
(7, 12); -- Autre enseignant