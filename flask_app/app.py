import os
import pathlib
import sqlite3

from flask import Flask, redirect , url_for, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    