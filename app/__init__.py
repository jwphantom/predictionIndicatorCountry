# app/__init__.py

from flask import Flask, g

app = Flask(__name__)


from app.routes import homeroute, prédictions_routes, statistiques_routes

from app.routes.request import predictionLife_request

from app.utils.graphic import GraphicGenerator

from app.models import LifeExpectancy

from app import errors
