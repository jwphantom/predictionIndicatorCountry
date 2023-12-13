import math
from flask import render_template, request
from app import app
from app.models.formulate_description import formulate_description

from app.models.LifeExpectancy import get_life_expectancy_prediction
from app.models.AdultMortality import get_adult_mortality_prediction
from app.models.infantDeaths import get_infant_mortality_prediction
from app.models.Schooling import get_schooling_prediction
from app.models.underFiveDeaths import get_under_five_deaths_prediction
from app.models.Population import get_population_growth_prediction
from app.models.AlcoholConsumption import get_alcohol_consumption_prediction

file_path = "datasets.csv"


@app.route("/request_predictionLife", methods=["POST"])
def request_predictionLife():
    try:
        if request.method == "POST":
            year = request.form["year"]

            # Check if year contains only digits
            if not year.isdigit():
                return render_template("predictions.html", yearError=True)

            if int(year) <= 2015:
                return render_template("predictions.html", yearError=True)

            pays = request.form["pays"]

            life = get_life_expectancy_prediction(file_path, pays, int(year))

            adultMortality = get_adult_mortality_prediction(file_path, pays, int(year))

            infantMortality = get_infant_mortality_prediction(
                file_path, pays, int(year)
            )

            schooling = get_schooling_prediction(file_path, pays, int(year))

            underFiveDeath = get_under_five_deaths_prediction(
                file_path, pays, int(year)
            )

            population = (
                (
                    get_population_growth_prediction(file_path, pays, int(year))
                    - get_population_growth_prediction(file_path, pays, (int(year) - 1))
                )
                / get_population_growth_prediction(file_path, pays, (int(year) - 1))
                * 100
            )

            alcohol = get_alcohol_consumption_prediction(file_path, pays, int(year))

            predictions = {
                "life": math.ceil(life),
                "adultMortality": math.ceil(adultMortality),
                "infantMortality": math.ceil(infantMortality),
                "schooling": math.ceil(schooling),
                "underFiveDeath": math.ceil(underFiveDeath),
                "population": round(population, 3),
                "alcohol": round(alcohol, 3),
            }

            description = formulate_description(pays, year, predictions)

        return render_template(
            "predictions.html",
            life=math.ceil(life),
            year=year,
            pays=pays,
            adultMortality=math.ceil(adultMortality),
            infantMortality=math.ceil(infantMortality),
            schooling=math.ceil(schooling),
            underFiveDeath=math.ceil(underFiveDeath),
            population=round(population, 3),
            alcohol=round(alcohol, 3),
            description=description,
        )

    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error for debugging
        return render_template("predictions.html", error=True)
