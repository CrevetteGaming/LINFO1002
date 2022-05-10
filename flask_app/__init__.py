# Code écrit par  Nicolas Swinnen , étudiant de l'EPL, faculté de l'Université Catholique de Louvain.
# Lien • Github : https://github.com/CrevetteGaming/LINFO1002

import os
import pathlib
import sqlite3
from flask import *

from database.info import *


app = Flask(__name__,template_folder='templates', static_folder='static')

#liaison avec la base de donnée
base =  info(os.path.join(pathlib.Path(__file__).parent.absolute(), "database/database.sqlite"))

#recolte des données en se connectant à la db
base.connection()

lst_fam = base.familles()
naissances = base.date_naissance()
#animal_races_pourcentage = base.animal_races_pourcentage()

#dictionnaire nombre de naissances/jour
naissances_jour = {}
for date in naissances:
    naissances_jour[date] = naissances_jour.get(date,0)+1
#print (naissances_jour)

#recup race pourcentage
race_pourc = base.animal_races_pourcentage()

#deconnection db
base.deconnection()

#informations pour le graphique
data = {
    "lst_fam" : lst_fam,
    "date_naissances" : naissances,
    "naissances_jour" : naissances_jour,
    "race_pourc" : race_pourc

}



# home page
@app.route('/')  # root : main page
def home():
    # by default, 'render_template' looks inside the folder 'template'
    return render_template("index.html",data=data)

# about page
@app.route("/about")
def about():
    return render_template("about.html")

#contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    