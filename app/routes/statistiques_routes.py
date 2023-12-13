from flask import render_template, request
from app import app

from app.models.LifeExpectancy import get_life_expectancy_prediction
from app.models.Schooling import get_schooling_prediction
from app.models.Population import get_population_growth_prediction
from app.models.AlcoholConsumption import get_alcohol_consumption_prediction

from app.utils.central_african_countries import getCentralAfricanCountries

from app.utils.graphic import GraphicGenerator
import pandas as pd


file_path = "datasets.csv"


@app.route("/statistiques", methods=["GET"])
def statistiques():
    try:
        central_african_countries = getCentralAfricanCountries()

        year = 2016

        life = []
        schooling = []

        growth = []

        alcohol = []

        for country in central_african_countries:
            life.append(
                round(get_life_expectancy_prediction(file_path, country, int(year)), 3)
            )

            schooling.append(
                round(get_schooling_prediction(file_path, country, int(year)), 3)
            )

            growth.append(
                round(
                    get_population_growth_prediction(file_path, country, int(year)), 3
                )
            )

            alcohol.append(
                round(
                    get_alcohol_consumption_prediction(file_path, country, int(year)), 3
                )
            )

        df_graph1 = pd.DataFrame(
            {
                "Pays": central_african_countries,
                "Espérance de Vie": life,
                "Taux de Scolarisation": schooling,
            }
        )

        df_graph2 = pd.DataFrame(
            {
                "Pays": central_african_countries,
                "Scolarisation": schooling,
                "ConsommationAlcool": alcohol,
            }
        )

        esperanceVie_Scolarisation = GraphicGenerator.generate_scatter_plot_base64(
            df_graph1,
            "Espérance de Vie",
            "Taux de Scolarisation",
            "Pays",
            "Espérance de Vie vs Taux de Scolarisation ",
            "Espérance de Vie",
            "Taux de Scolarisation (%)",
        )

        populationGrowth_Graphic = GraphicGenerator.generate_histogram(
            growth, central_african_countries
        )

        alcool_VS_Scolarisation = GraphicGenerator.generate_scatter_plot_base64(
            df_graph2,
            "Scolarisation",
            "ConsommationAlcool",
            "Pays",
            "Taux de scolarisation VS Consommation d'alcool",
            "Année de scolarisation",
            "Consommation d'alcool (en litre)",
        )

        return render_template(
            "statistiques.html",
            esperanceVie_Scolarisation=esperanceVie_Scolarisation,
            populationGrowth_Graphic=populationGrowth_Graphic,
            alcool_VS_Scolarisation=alcool_VS_Scolarisation,
        )

    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error for debugging
        return render_template("statistiques.html", errorFull=True)
