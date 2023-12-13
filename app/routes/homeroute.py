from flask import render_template
from app import app
import pandas as pd

from app.utils.graphic import GraphicGenerator

file_path = "datasets.csv"
life_expectancy_data = pd.read_csv(file_path)


@app.route("/", methods=["GET"])
def home():
    # Obtenez les premières lignes du dataframe
    data_head = life_expectancy_data.head().to_html()

    columns_of_interest = [
        "Life expectancy ",
        "Adult Mortality",
        "infant deaths",
        "Alcohol",
        "Schooling",
        "Population",
        "GDP",
    ]

    central_african_countries = [
        "Cameroon",
        "Central African Republic",
        "Chad",
        "Congo",
        "Democratic Republic of the Congo",
        "Equatorial Guinea",
        "Gabon",
        "Burundi",
        "Sao Tome and Principe",
    ]

    correlation_image = GraphicGenerator.generate_correlation_matrix(
        life_expectancy_data, columns_of_interest
    )

    # population growth

    return render_template(
        "index.html",
        data_head=data_head,
        correlation_image=correlation_image,
    )
