from flask import render_template, request
from app import app


@app.route("/predictions", methods=["GET"])
def prédictions():
    return render_template("predictions.html")
