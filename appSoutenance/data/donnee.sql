-- ============================
-- INSERTION DES ENSEIGNANTS
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
(9, 'Bonnet', 'Antoine', '2004-03-14', 'M.', '0691234578', 'antoine.bonnet@edu.fr', 'abonnet', 'pass9'),
(10, 'Blanc', 'Sarah', '2004-06-22', 'Mme', '0612345987', 'sarah.blanc@edu.fr', 'sblanc', 'pass10'),
(11, 'Garnier', 'Maxime', '2004-01-08', 'M.', '0623456198', 'maxime.garnier@edu.fr', 'mgarnier', 'pass11'),
(12, 'Faure', 'Chloé', '2004-10-19', 'Mme', '0634567219', 'chloe.faure@edu.fr', 'cfaure', 'pass12'),
(13, 'Roussel', 'Nathan', '2004-05-30', 'M.', '0645678321', 'nathan.roussel@edu.fr', 'nroussel', 'pass13'),
(14, 'Vincent', 'Manon', '2004-08-11', 'Mme', '0656789432', 'manon.vincent@edu.fr', 'mvincent', 'pass14'),
(15, 'Muller', 'Arthur', '2004-02-25', 'M.', '0667891543', 'arthur.muller@edu.fr', 'amuller', 'pass15'),
(16, 'Lefevre', 'Jade', '2004-07-07', 'Mme', '0678912654', 'jade.lefevre@edu.fr', 'jlefevre', 'pass16'),
(17, 'Mercier', 'Paul', '2004-11-16', 'M.', '0689123765', 'paul.mercier@edu.fr', 'pmercier', 'pass17'),
(18, 'Lemoine', 'Louise', '2004-04-02', 'Mme', '0691234876', 'louise.lemoine@edu.fr', 'llemoine', 'pass18'),
(19, 'Andre', 'Theo', '2004-09-13', 'M.', '0612348765', 'theo.andre@edu.fr', 'tandre', 'pass19'),
(20, 'Roux', 'Clara', '2004-12-28', 'Mme', '0623459876', 'clara.roux@edu.fr', 'croux', 'pass20'),
(21, 'David', 'Victor', '2005-03-05', 'M.', '0634561987', 'victor.david@edu.fr', 'vdavid', 'pass21'),
(22, 'Bertrand', 'Zoé', '2005-06-18', 'Mme', '0645672198', 'zoe.bertrand@edu.fr', 'zbertrand', 'pass22'),
(23, 'Morel', 'Gabriel', '2005-01-21', 'M.', '0656783219', 'gabriel.morel@edu.fr', 'gmorel', 'pass23'),
(24, 'Fontaine', 'Alice', '2005-08-09', 'Mme', '0667894321', 'alice.fontaine@edu.fr', 'afontaine', 'pass24'),
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
(3, 'BUT2', 2025, 'Formation initiale'),
(4, 'BUT2', 2025, 'Formation initiale'),
(5, 'BUT2', 2025, 'Formation initiale'),
(6, 'BUT2', 2025, 'Formation initiale'),
(7, 'BUT2', 2025, 'Formation initiale'),
(8, 'BUT2', 2025, 'Formation initiale'),
(9, 'BUT2', 2025, 'Formation initiale'),
(10, 'BUT2', 2025, 'Formation initiale'),
(11, 'BUT2', 2025, 'Formation initiale'),
(12, 'BUT2', 2025, 'Formation initiale'),
(13, 'BUT2', 2025, 'Formation initiale'),
(14, 'BUT2', 2025, 'Formation initiale'),
(15, 'BUT2', 2025, 'Formation initiale'),
(16, 'BUT2', 2025, 'Formation initiale'),
(17, 'BUT2', 2025, 'Formation initiale'),
(18, 'BUT2', 2025, 'Formation initiale'),
(19, 'BUT2', 2025, 'Formation initiale'),
(20, 'BUT2', 2025, 'Formation initiale'),
(21, 'BUT2', 2025, 'Formation initiale'),
(22, 'BUT2', 2025, 'Formation initiale'),
(23, 'BUT2', 2025, 'Formation initiale'),
(24, 'BUT2', 2025, 'Formation initiale'),
(25, 'BUT2', 2025, 'Formation initiale'), (26, 'BUT2', 2025, 'Formation initiale'), (27, 'BUT2', 2025, 'Formation initiale'), (28, 'BUT2', 2025, 'Formation initiale'), (29, 'BUT2', 2025, 'Formation initiale'),
(30, 'BUT2', 2025, 'Formation initiale'),

(31, 'BUT2', 2025, 'Formation apprentissage'), (32, 'BUT2', 2025, 'Formation apprentissage'), (33, 'BUT2', 2025, 'Formation apprentissage'), (34, 'BUT2', 2025, 'Formation apprentissage'), (35, 'BUT2', 2025, 'Formation apprentissage'),
(36, 'BUT2', 2025, 'Formation apprentissage'), (37, 'BUT2', 2025, 'Formation apprentissage'), (38, 'BUT2', 2025, 'Formation apprentissage'), (39, 'BUT2', 2025, 'Formation apprentissage'), (40, 'BUT2', 2025, 'Formation apprentissage'),
(41, 'BUT2', 2025, 'Formation apprentissage'), (42, 'BUT2', 2025, 'Formation apprentissage'), (43, 'BUT2', 2025, 'Formation apprentissage'), (44, 'BUT2', 2025, 'Formation apprentissage'), (45, 'BUT2', 2025, 'Formation apprentissage'),
(46, 'BUT2', 2025, 'Formation apprentissage'), (47, 'BUT2', 2025, 'Formation apprentissage'), (48, 'BUT2', 2025, 'Formation apprentissage'), (49, 'BUT2', 2025, 'Formation apprentissage'), (50, 'BUT2', 2025, 'Formation apprentissage'),
(51, 'BUT2', 2025, 'Formation apprentissage'), (52, 'BUT2', 2025, 'Formation apprentissage'), (53, 'BUT2', 2025, 'Formation apprentissage'), (54, 'BUT2', 2025, 'Formation apprentissage'), (55, 'BUT2', 2025, 'Formation apprentissage'),
(56, 'BUT2', 2025, 'Formation apprentissage'), (57, 'BUT2', 2025, 'Formation apprentissage'), (58, 'BUT2', 2025, 'Formation apprentissage'), (59, 'BUT2', 2025, 'Formation apprentissage'), (60, 'BUT2', 2025, 'Formation apprentissage'),

(61, 'BUT3', 2025, 'Formation initiale'), (62, 'BUT3', 2025, 'Formation initiale'), (63, 'BUT3', 2025, 'Formation initiale'), (64, 'BUT3', 2025, 'Formation initiale'), (65, 'BUT3', 2025, 'Formation initiale'),
(66, 'BUT3', 2025, 'Formation initiale'), (67, 'BUT3', 2025, 'Formation initiale'), (68, 'BUT3', 2025, 'Formation initiale'), (69, 'BUT3', 2025, 'Formation initiale'), (70, 'BUT3', 2025, 'Formation initiale'),
(71, 'BUT3', 2025, 'Formation initiale'), (72, 'BUT3', 2025, 'Formation initiale'), (73, 'BUT3', 2025, 'Formation initiale'), (74, 'BUT3', 2025, 'Formation initiale'), (75, 'BUT3', 2025, 'Formation initiale'),
(76, 'BUT3', 2025, 'Formation initiale'), (77, 'BUT3', 2025, 'Formation initiale'), (78, 'BUT3', 2025, 'Formation initiale'), (79, 'BUT3', 2025, 'Formation initiale'), (80, 'BUT3', 2025, 'Formation initiale'),
(81, 'BUT3', 2025, 'Formation initiale'), (82, 'BUT3', 2025, 'Formation initiale'), (83, 'BUT3', 2025, 'Formation initiale'), (84, 'BUT3', 2025, 'Formation initiale'), (85, 'BUT3', 2025, 'Formation initiale'),
(86, 'BUT3', 2025, 'Formation initiale'), (87, 'BUT3', 2025, 'Formation initiale'), (88, 'BUT3', 2025, 'Formation initiale'), (89, 'BUT3', 2025, 'Formation initiale'), (90, 'BUT3', 2025, 'Formation initiale'),

(91, 'BUT3', 2025, 'Formation apprentissage'), (92, 'BUT3', 2025, 'Formation apprentissage'), (93, 'BUT3', 2025, 'Formation apprentissage'), (94, 'BUT3', 2025, 'Formation apprentissage'), (95, 'BUT3', 2025, 'Formation apprentissage'),
(96, 'BUT3', 2025, 'Formation apprentissage'), (97, 'BUT3', 2025, 'Formation apprentissage'), (98, 'BUT3', 2025, 'Formation apprentissage'), (99, 'BUT3', 2025, 'Formation apprentissage'), (100, 'BUT3', 2025, 'Formation apprentissage'),
(101, 'BUT3', 2025, 'Formation apprentissage'), (102, 'BUT3', 2025, 'Formation apprentissage'), (103, 'BUT3', 2025, 'Formation apprentissage'), (104, 'BUT3', 2025, 'Formation apprentissage'), (105, 'BUT3', 2025, 'Formation apprentissage'),
(106, 'BUT3', 2025, 'Formation apprentissage'), (107, 'BUT3', 2025, 'Formation apprentissage'), (108, 'BUT3', 2025, 'Formation apprentissage'), (109, 'BUT3', 2025, 'Formation apprentissage'), (110, 'BUT3', 2025, 'Formation apprentissage'),
(111, 'BUT3', 2025, 'Formation apprentissage'), (112, 'BUT3', 2025, 'Formation apprentissage'), (113, 'BUT3', 2025, 'Formation apprentissage'), (114, 'BUT3', 2025, 'Formation apprentissage'), (115, 'BUT3', 2025, 'Formation apprentissage'),
(116, 'BUT3', 2025, 'Formation apprentissage'), (117, 'BUT3', 2025, 'Formation apprentissage'), (118, 'BUT3', 2025, 'Formation apprentissage'), (119, 'BUT3', 2025, 'Formation apprentissage'), (120, 'BUT3', 2025, 'Formation apprentissage');

-- ============================
-- TUTEURS (120 tuteurs, répartis sur 20 enseignants, 6 étudiants par prof)
-- ============================
INSERT INTO TUTORER (id_enseignant, id_etudiant, annee) VALUES
(1, 1, 2025), (2, 2, 2025), (3, 3, 2025), (4, 4, 2025), (5, 5, 2025), (6, 6, 2025), (7, 7, 2025), (8, 8, 2025), (9, 9, 2025), (10, 10, 2025), (11, 11, 2025), (12, 12, 2025), (13, 13, 2025), (14, 14, 2025), (15, 15, 2025), (16, 16, 2025), (17, 17, 2025), (18, 18, 2025), (19, 19, 2025), (20, 20, 2025),
(1, 21, 2025), (2, 22, 2025), (3, 23, 2025), (4, 24, 2025), (5, 25, 2025), (6, 26, 2025), (7, 27, 2025), (8, 28, 2025), (9, 29, 2025), (10, 30, 2025), (11, 31, 2025), (12, 32, 2025), (13, 33, 2025), (14, 34, 2025), (15, 35, 2025), (16, 36, 2025), (17, 37, 2025), (18, 38, 2025), (19, 39, 2025), (20, 40, 2025),
(1, 41, 2025), (2, 42, 2025), (3, 43, 2025), (4, 44, 2025), (5, 45, 2025), (6, 46, 2025), (7, 47, 2025), (8, 48, 2025), (9, 49, 2025), (10, 50, 2025), (11, 51, 2025), (12, 52, 2025), (13, 53, 2025), (14, 54, 2025), (15, 55, 2025), (16, 56, 2025), (17, 57, 2025), (18, 58, 2025), (19, 59, 2025), (20, 60, 2025),
(1, 61, 2025), (2, 62, 2025), (3, 63, 2025), (4, 64, 2025), (5, 65, 2025), (6, 66, 2025), (7, 67, 2025), (8, 68, 2025), (9, 69, 2025), (10, 70, 2025), (11, 71, 2025), (12, 72, 2025), (13, 73, 2025), (14, 74, 2025), (15, 75, 2025), (16, 76, 2025), (17, 77, 2025), (18, 78, 2025), (19, 79, 2025), (20, 80, 2025),
(1, 81, 2025), (2, 82, 2025), (3, 83, 2025), (4, 84, 2025), (5, 85, 2025), (6, 86, 2025), (7, 87, 2025), (8, 88, 2025), (9, 89, 2025), (10, 90, 2025), (11, 91, 2025), (12, 92, 2025), (13, 93, 2025), (14, 94, 2025), (15, 95, 2025), (16, 96, 2025), (17, 97, 2025), (18, 98, 2025), (19, 99, 2025), (20, 100, 2025),
(1, 101, 2025), (2, 102, 2025), (3, 103, 2025), (4, 104, 2025), (5, 105, 2025), (6, 106, 2025), (7, 107, 2025), (8, 108, 2025), (9, 109, 2025), (10, 110, 2025), (11, 111, 2025), (12, 112, 2025), (13, 113, 2025), (14, 114, 2025), (15, 115, 2025), (16, 116, 2025), (17, 117, 2025), (18, 118, 2025), (19, 119, 2025), (20, 120, 2025);

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
-- Groupe 1 : Soutenance groupée (1, 31, 61)
(1, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-15', NULL, 'Stage obtenu', NULL, 'cv_dupont.pdf', 'lm_dupont.pdf', 1, 1),
(2, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-10', NULL, 'Stage obtenu', NULL, 'cv_legrand.pdf', 'lm_legrand.pdf', 2, 31),
(3, 'Salon', 'Contact direct', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_barbier.pdf', 'lm_barbier.pdf', 3, 61),

-- Groupe 2 : Soutenance groupée (2, 32)
(4, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-12', NULL, 'Stage obtenu', NULL, 'cv_moreau.pdf', 'lm_moreau.pdf', 2, 2),
(5, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-08', NULL, 'Stage obtenu', NULL, 'cv_gauthier.pdf', 'lm_gauthier.pdf', 4, 32),

-- Groupe 3 : Soutenance seule (3)
(6, 'Réseau personnel', 'Recommandation', 'Acceptée', '2025-09-18', NULL, 'Stage obtenu', NULL, 'cv_laurent.pdf', 'lm_laurent.pdf', 3, 3),

-- Apprentis avec stage mais sans soutenance (33, 91)
(7, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-05', NULL, 'Stage obtenu', NULL, 'cv_perrin.pdf', 'lm_perrin.pdf', 5, 33),
(8, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-25', NULL, 'Stage obtenu', NULL, 'cv_denis.pdf', 'lm_denis.pdf', 6, 91),

-- Initial avec stage mais sans soutenance (4, 62)
(9, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-14', NULL, 'Stage obtenu', NULL, 'cv_simon.pdf', 'lm_simon.pdf', 4, 4),
(10, 'Salon', 'Contact direct', 'Acceptée', '2025-09-11', NULL, 'Stage obtenu', NULL, 'cv_arnaud.pdf', 'lm_arnaud.pdf', 7, 62),

-- Etudiants avec plusieurs démarches mais pas de stage (5, 34)
(11, 'Indeed', 'Réponse à offre', 'Refusée', '2025-09-16', NULL, 'Refusé', 'Profil junior', 'cv_michel.pdf', 'lm_michel.pdf', 5, 5),
(12, 'LinkedIn', 'Réponse à offre', 'En attente', '2025-09-22', NULL, NULL, NULL, 'cv_michel.pdf', 'lm_michel2.pdf', 8, 5),
(13, 'Site entreprise', 'Candidature spontanée', 'Refusée', '2025-09-07', '2025-09-21', 'Refusé', 'Profil inadapté', 'cv_michel.pdf', 'lm_michel3.pdf', 1, 5),

(14, 'Réseau personnel', 'Recommandation', 'Refusée', '2025-09-19', NULL, 'Refusé', 'Pas de poste', 'cv_robin.pdf', 'lm_robin.pdf', 6, 34),
(15, 'Site entreprise', 'Candidature spontanée', 'En attente', '2025-09-15', NULL, NULL, NULL, 'cv_robin.pdf', 'lm_robin2.pdf', 6, 34),

-- Nouveaux étudiants avec stage pour plus de soutenances (11, 63, 92)
(16, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_garnier.pdf', 'lm_garnier.pdf', 1, 11),
(17, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-22', NULL, 'Stage obtenu', NULL, 'cv_martinez.pdf', 'lm_martinez.pdf', 2, 63),
(18, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-25', NULL, 'Stage obtenu', NULL, 'cv_dumont.pdf', 'lm_dumont.pdf', 3, 92),

-- Etudiants avec stage validé mais SANS soutenance (pour tests création)
(19, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_david.pdf', 'lm_david.pdf', 1, 21),
(20, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-22', NULL, 'Stage obtenu', NULL, 'cv_bertrand.pdf', 'lm_bertrand.pdf', 2, 22),
(21, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-25', NULL, 'Stage obtenu', NULL, 'cv_morel.pdf', 'lm_morel.pdf', 3, 23),
(22, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_fontaine.pdf', 'lm_fontaine.pdf', 4, 24),
(23, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-22', NULL, 'Stage obtenu', NULL, 'cv_guerin.pdf', 'lm_guerin.pdf', 5, 25),
(24, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-25', NULL, 'Stage obtenu', NULL, 'cv_rousseau.pdf', 'lm_rousseau.pdf', 6, 26),
(25, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_blanc.pdf', 'lm_blanc.pdf', 7, 27),
(26, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-22', NULL, 'Stage obtenu', NULL, 'cv_garnier.pdf', 'lm_garnier.pdf', 8, 28),
(27, 'Site entreprise', 'Candidature spontanée', 'Acceptée', '2025-09-25', NULL, 'Stage obtenu', NULL, 'cv_chevalier.pdf', 'lm_chevalier.pdf', 1, 29),
(28, 'Indeed', 'Réponse à offre', 'Acceptée', '2025-09-20', NULL, 'Stage obtenu', NULL, 'cv_francois.pdf', 'lm_francois.pdf', 2, 30),
(29, 'LinkedIn', 'Réponse à offre', 'Acceptée', '2025-09-22', NULL, 'Stage obtenu', NULL, 'cv_faure.pdf', 'lm_faure.pdf', 3, 12);

-- ============================
-- STAGES 
-- ============================

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, duree_stage, unite_duree, titre_stage, theme_stage, id_maitre, id_demarche) VALUES
-- Stages pour Groupe 1
(1, 'Stage de fin d''études', '2025-10-01', '2025-03-31', 6, 'mois', 'Développement d''une application web de gestion', 'Développement Full-Stack', 1, 1),
(2, 'Alternance', '2025-09-01', '2026-08-31', 12, 'mois', 'Développement Backend Java', 'Backend', 2, 2),
(3, 'Stage de fin d''études', '2025-04-01', '2025-09-30', 6, 'mois', 'Data Science et IA', 'IA', 3, 3),

-- Stages pour Groupe 2
(4, 'Stage de fin d''études', '2025-10-15', '2025-04-15', 6, 'mois', 'Analyse de données massives', 'Big Data', 2, 4),
(5, 'Alternance', '2025-09-01', '2026-08-31', 12, 'mois', 'Sécurité des réseaux', 'Cybersécurité', 4, 5),

-- Stage pour Groupe 3
(6, 'Stage de fin d''études', '2025-10-01', '2025-03-31', 6, 'mois', 'Site e-commerce', 'Web', 3, 6),

-- Stages sans soutenance
(7, 'Alternance', '2025-09-01', '2026-08-31', 12, 'mois', 'DevOps et Cloud', 'Cloud', 5, 7),
(8, 'Alternance', '2025-09-01', '2026-08-31', 12, 'mois', 'Support technique', 'Support', 6, 8),
(9, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Application mobile', 'Mobile', 4, 9),
(10, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Refonte site web', 'Web', 7, 10),

-- Nouveaux stages pour soutenances supplémentaires
(11, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Développement Web', 'Web', 1, 16),
(12, 'Stage de fin d''études', '2025-04-01', '2025-06-30', 3, 'mois', 'Data Analyst', 'Data', 2, 17),
(13, 'Alternance', '2025-09-01', '2026-08-31', 12, 'mois', 'Admin Sys', 'Réseau', 3, 18),

-- Stages sans soutenance (pour tests création)
(14, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Dev Mobile', 'Mobile', 1, 19),
(15, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Dev Web', 'Web', 2, 20),
(16, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Data Science', 'Data', 3, 21),
(17, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Cyber', 'Secu', 4, 22),
(18, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Reseau', 'Reseau', 5, 23),
(19, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Cloud', 'Cloud', 6, 24),
(20, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'IA', 'IA', 7, 25),
(21, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Big Data', 'Data', 8, 26),
(22, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'DevOps', 'DevOps', 1, 27),
(23, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Fullstack', 'Web', 2, 28),
(24, 'Stage professionnel', '2025-04-01', '2025-06-30', 3, 'mois', 'Backend', 'Web', 3, 29);

-- ============================
-- DÉMARCHES ET STAGES SUPPLÉMENTAIRES
-- ============================
INSERT INTO DEMARCHE (id_demarche, source, typeD, situation, date_envoi, id_entreprise, id_etudiant) VALUES
(44, 'Import', 'Stage', 'Acceptée', '2025-01-10', 1, 25), (45, 'Import', 'Stage', 'Acceptée', '2025-01-10', 1, 26), (46, 'Import', 'Stage', 'Acceptée', '2025-01-10', 1, 27),
(47, 'Import', 'Stage', 'Acceptée', '2025-01-10', 2, 28), (48, 'Import', 'Stage', 'Acceptée', '2025-01-10', 2, 29), (49, 'Import', 'Stage', 'Acceptée', '2025-01-10', 2, 30),
(50, 'Import', 'Stage', 'Acceptée', '2025-01-10', 3, 71), (51, 'Import', 'Stage', 'Acceptée', '2025-01-10', 3, 72), (52, 'Import', 'Stage', 'Acceptée', '2025-01-10', 3, 73),
(53, 'Import', 'Stage', 'Acceptée', '2025-01-10', 4, 74), (54, 'Import', 'Stage', 'Acceptée', '2025-01-10', 4, 75), (55, 'Import', 'Stage', 'Acceptée', '2025-01-10', 4, 76);

INSERT INTO STAGE (id_stage, typeS, date_debut, date_fin, titre_stage, id_demarche) VALUES
(20, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe A1', 44), (21, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe A2', 45), (22, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe A3', 46),
(23, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe B1', 47), (24, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe B2', 48), (25, 'Stage BUT2', '2025-05-01', '2025-06-30', 'Projet Groupe B3', 49),
(26, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe C1', 50), (27, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe C2', 51), (28, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe C3', 52),
(29, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe D1', 53), (30, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe D2', 54), (31, 'Stage BUT3', '2025-03-01', '2025-08-31', 'Expertise Groupe D3', 55);

-- ============================
-- SOUTENANCES
-- ============================
INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
(1, 101, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 1), (2, 101, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 2), (3, 101, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 3),
(4, 102, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 4), (5, 102, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 5), (6, 102, 'Bâtiment A', '2025-04-15', '09:00', '09:45', 6),
(7, 103, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 7), (8, 103, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 8), (9, 103, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 9),
(10, 101, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 10), (11, 101, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 11), (12, 101, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 12),
(13, 102, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 13), (14, 102, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 14), (15, 102, 'Bâtiment A', '2025-04-15', '10:00', '10:45', 15),
(16, 103, 'Bâtiment B', '2025-04-15', '10:00', '10:45', 16), (17, 103, 'Bâtiment B', '2025-04-15', '10:00', '10:45', 17), (18, 103, 'Bâtiment B', '2025-04-15', '10:00', '10:45', 18),
(19, 104, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 19), (20, 104, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 20), (21, 104, 'Bâtiment B', '2025-04-15', '09:00', '09:45', 21),
(22, 105, 'Bâtiment A', '2025-06-15', '09:00', '09:45', 22), (23, 105, 'Bâtiment A', '2025-06-15', '09:00', '09:45', 23), (24, 105, 'Bâtiment A', '2025-06-15', '09:00', '09:45', 24),
(25, 105, 'Bâtiment A', '2025-06-15', '10:00', '10:45', 25);

INSERT INTO SOUTENANCE (id_soutenance, salle, nom_bat, dateS, h_debut, h_fin, id_stage) VALUES
-- Groupe 1 : 2 élèves BUT2 FI (1, 2)
(1, 101, 'Bâtiment A', '2025-06-20', '09:00', '10:00', 1),
(4, 101, 'Bâtiment A', '2025-06-20', '09:00', '10:00', 4),

-- Groupe 2 : 3 élèves BUT2 Alternance (31, 32, 33)
(2, 201, 'Bâtiment C', '2025-06-21', '09:00', '10:00', 2),
(5, 201, 'Bâtiment C', '2025-06-21', '09:00', '10:00', 5),
(7, 201, 'Bâtiment C', '2025-06-21', '09:00', '10:00', 7),

-- Groupe 3 : 2 élèves BUT2 FI (6, 11)
(6, 101, 'Bâtiment A', '2025-06-20', '14:00', '15:00', 6),
(10, 101, 'Bâtiment A', '2025-06-20', '14:00', '15:00', 11),

-- BUT3 (Restent individuels ou séparés pour l'instant)
(3, 101, 'Bâtiment A', '2025-07-03', '09:00', '10:00', 3), -- BUT3 FI
(8, 201, 'Bâtiment C', '2025-07-03', '10:00', '11:00', 8), -- Etu 91 (BUT3 App)
(9, 201, 'Bâtiment C', '2025-07-03', '11:00', '12:00', 10), -- Etu 62 (BUT3 FI)
(11, 202, 'Bâtiment C', '2025-07-03', '15:00', '16:00', 12), -- Etu 63 (BUT3 FI)
(12, 202, 'Bâtiment C', '2025-07-03', '16:00', '17:00', 13); -- Etu 92 (BUT3 App)
(26, 106, 'Bâtiment B', '2025-06-16', '09:00', '10:00', 26), (27, 106, 'Bâtiment B', '2025-06-16', '10:00', '11:00', 27), (28, 106, 'Bâtiment B', '2025-06-16', '11:00', '12:00', 28),
(29, 106, 'Bâtiment B', '2025-06-16', '13:00', '14:00', 29), (30, 106, 'Bâtiment B', '2025-06-16', '14:00', '15:00', 30), (31, 106, 'Bâtiment B', '2025-06-16', '15:00', '16:00', 31);

-- ============================
-- JURYS
-- ============================
INSERT INTO JURY (id_jury, date_jury, h_jury, duree, id_soutenance) VALUES
(1, '2025-06-20', '09:00', 60, 1),
(4, '2025-06-20', '09:00', 60, 4),
(2, '2025-06-21', '09:00', 60, 2),
(5, '2025-06-21', '09:00', 60, 5),
(7, '2025-06-21', '09:00', 60, 7),
(6, '2025-06-20', '14:00', 60, 6),
(10, '2025-06-20', '14:00', 60, 10),
(3, '2025-07-03', '09:00', 60, 3),
(8, '2025-07-03', '10:00', 60, 8),
(9, '2025-07-03', '11:00', 60, 9),
(11, '2025-07-03', '15:00', 60, 11),
(12, '2025-07-03', '16:00', 60, 12);
(20, '2025-06-15', '09:00', 45, 20), (21, '2025-06-15', '09:00', 45, 21), (22, '2025-06-15', '09:00', 45, 22),
(23, '2025-06-15', '10:00', 45, 23), (24, '2025-06-15', '10:00', 45, 24), (25, '2025-06-15', '10:00', 45, 25),
(26, '2025-06-16', '09:00', 60, 26), (27, '2025-06-16', '10:00', 60, 27), (28, '2025-06-16', '11:00', 60, 28),
(29, '2025-06-16', '13:00', 60, 29), (30, '2025-06-16', '14:00', 60, 30), (31, '2025-06-16', '15:00', 60, 31);

-- ============================
-- COMPOSITIONS DES JURYS
-- ============================
INSERT INTO COMPOSER (id_enseignant, id_soutenance) VALUES
-- Groupe 1 (Soutenances 1, 4) : Jury 1, 2
(1, 1), (2, 1),
(1, 4), (2, 4),

-- Groupe 2 (Soutenances 2, 5, 7) : Jury 7, 8
(7, 2), (8, 2),
(7, 5), (8, 5),
(7, 7), (8, 7),

-- Groupe 3 (Soutenance 6, 10) : Jury 5, 6
(5, 6), (6, 6),
(5, 10), (6, 10),

-- BUT3
(1, 3), (2, 3),
(7, 8), (8, 8),
(9, 9), (10, 9),
(13, 11), (14, 11),
(15, 12), (16, 12);
