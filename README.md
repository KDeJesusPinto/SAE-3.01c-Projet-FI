# SAE-3.01c-Projet-FI

##
Lien vers les diapositives de la soutenance de bilan de la 3e semaine : 

[Diaporama semaine 3](https://docs.google.com/presentation/d/1qlTzRkh3Dtm6tRGx9_wUHFio4fSNeo7LGqxjkEWp6G4/edit?usp=sharing)

## Développeurs :
- De Jesus Pinto Erika (KuRika28)
- Blandin Pernelle (PernelleBlandin)
- Fronton Maelyss (Cherry5990)
- Hachelef Asma (Asminouch)
- Pelletant Colin (colin2525)

### Chargement de la base de données 
flask --app appSoutenance.app loaddb appSoutenance/data/arexis_donnees.csv

### Lancement du shell
flask --app appSoutenance.app shell 

### Lancement des tests

Pour avoir le rapport de tests dans le terminal faites : 
    coverage run -m pytest
    coverage report -m

Lancer la commande *coverage html* pour créer un dossier "htmlcov". Dans ce fichier, faites glisser le fichier "index.html" dans votre navigateur web, afin d'avooir un rapport de test plus lisible.
    
