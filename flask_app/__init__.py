import os
import pathlib
import sqlite3

from database.info import info

from flask import Flask, redirect , url_for, render_template


app = Flask(__name__)

base =  info(os.path.join(pathlib.Path(__file__).parent.absolute(), "database/database.sqlite"))

base.connection()

lst_fam = base.familles()

base.deconnection()

data = {
    "lst_fam" : lst_fam
}

@app.route("/")
def home():
    return render_template("index.html",data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    