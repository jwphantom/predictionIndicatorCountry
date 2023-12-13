import pandas as pd
import numpy as np

from app.utils.central_african_countries import getCentralAfricanCountries

from app.models.linearRegression import linear_regression


def load_data(file_path):
    data = pd.read_csv(file_path)
    central_african_countries = getCentralAfricanCountries()

    filtered_data = data[data["Country"].isin(central_african_countries)]
    filtered_data["Year"] = pd.to_numeric(filtered_data["Year"], errors="coerce")
    mean_values = (
        filtered_data.groupby(["Country", "Year"])[
            [
                "Life expectancy ",
                "Adult Mortality",
                "infant deaths",
                "Schooling",
                "under-five deaths ",
            ]
        ]
        .mean()
        .reset_index()
    )
    return mean_values


def predict_under_five_deaths(country_data, country, year):
    subset = country_data[country_data["Country"] == country]
    X = subset["Year"].values
    y = subset["under-five deaths "].values

    if len(X) == 0 or len(y) == 0:
        return 0

    slope, intercept = linear_regression(X, y)
    prediction = slope * year + intercept
    return prediction


def get_under_five_deaths_prediction(file_path, country, year):
    data = load_data(file_path)
    return predict_under_five_deaths(data, country, year)
