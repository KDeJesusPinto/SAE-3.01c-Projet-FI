from .app import app
from flask import render_template, request, url_for , redirect

@app.route('/')
@app.route('/connexion/')
def index():
    return render_template("index.html", title="Soutenance - Connexion")

#Pour page enseignants
@app.route('/enseignant/')
def accueil_enseignant():
    return render_template("enseignant/accueil_enseignant.html", title="Accueil")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    return render_template("enseignant/lst_etudiants_enseignant.html", title="Liste des étudiants")


#Pour page étudiants
@app.route('/etudiant/')
def accueil_etudiant():
    return render_template("etudiant/accueil_etu.html", title="Accueil")



#Pour page administrateur
@app.route('/admin/')
def accueil_admin():
    return render_template("admin/accueil_admin.html", title="Accueil")




if __name__== "__main__":
    app.run()