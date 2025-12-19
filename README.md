# SAE-3.01c-Projet-FI

##
Lien vers les diapositives de la soutenance de bilan de la 3e semaine : 

[Diaporama semaine 3](https://docs.google.com/presentation/d/1qlTzRkh3Dtm6tRGx9_wUHFio4fSNeo7LGqxjkEWp6G4/edit?usp=sharing)

## Description générale du projet  

  Dans le cadre de la SAE3.01c (projet en formation initiale), nous avons développé une application web permettant de gérer les soutenances, la gestion étant actuellement complexe et effectuée avec de multiples tableurs.  
    
  L'application compte 3 parties correspondant aux 3 rôles : une partie étudiant permettant aux étudiants de gérer leurs démarches de recherches de stage, leur stage et leur soutenance, une partie enseignant permettant aux enseignants de gérer les étudiants à tutorer et de poser et d'assister à des soutenances et une partie administrateur permettant de gérer les étudiants et les enseignants, de modifier des informations et de poser des soutenances.  
    
  L'application utilise Flask avec l'architecture MVT et est codée en Python, la base de données étant gérée à l'aide de l'ORM SQLAlchemy, les pages en elles-mêmes sont codées à l'aide de HTML et CSS.

## Composition de l'équipe de développeurs

- De Jesus Pinto Erika (@KuRika28)  
- Blandin Pernelle (@PernelleBlandin)  
- Fronton Maelyss (@Cherry5990)  
- Hachelef Asma (@Asminouch)  
- Pelletant Colin (colin2525)  

## Packages nécessaires au lancement de l'application

La liste des packages nécessaire à l'application se trouve dans le fichier `requirements.txt`  

## Commandes à effectuer pour lancer l'application

Tout d'abord nous vous conseillons de lancer l'application dans un environnement virtuel afin de ne pas surchager votre ordinateur. Vous pouvez par exemple utiliser `venv`.  
  
- Si vous ne l'avez pas installé, faites le avec la commande suivante :  
```sudo apt install python3-virtualenv```  
  
- Ensuite créez l'environnement virtuel :  
```virtualenv -p python3 venv```  

- Lancez l'environnement virtuel dans le dossier où se trouve le dossier `venv` :  
```source venv/bin/activate```

- Les packages que vous allez maintenant installer le seront dans cet environnement. Installez les packages nécessaires à l'application :  
```pip install -r requirements.txt -v```  

- Chargez la base de données en lançant cette commande depuis la racine du projet :  
```flask --app appSoutenance.app loaddb appSoutenance/data/arexis_donnees.csv```

- Maintenant lancez la commande
```flask run```
depuis la racine du projet, le serveur se lance et vous n'avez plus qu'à `Ctrl+clic` sur le lien pour voir la page s'afficher.
  
