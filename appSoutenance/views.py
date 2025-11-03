from .app import app
from flask import render_template, request, url_for , redirect

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/enseignant/')
def accueil_enseignant():
    return render_template("prof/accueil_enseignant.html")

@app.route('/etudiant/')
def accueil_etudiant():
    return render_template("etudiant/accueil_etu.html")

@app.route('/admin/')
def accueil_admin():
    return render_template("admin/accueil_admin.html")

if __name__== "__main__":
    app.run()