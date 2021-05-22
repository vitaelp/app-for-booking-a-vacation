from flask import Flask, request
from flask import render_template
from Funktionen.visualisierung import balkendiagramm
import pandas as ps

app = Flask("Hello World")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string
    else:
        return render_template("index.html", name="Vita")


@app.route("/test")
def test():
    return "success"


@app.route("/liste")
def liste():
    seiten_titel = "Partygäste"
    gaeste_liste = ["Fabian", "Azra", "Michael", "Wolfgang"]
    return render_template("auflistung.html",titel=seiten_titel, partygaeste=gaeste_liste)


@app.route("/testvis")
def testvis():
    grafik_div=balkendiagramm()
    return grafik_div


if __name__ == "__main__":
    app.run(debug=True, port=5000)