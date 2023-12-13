import pandas as pd
import numpy as np

from app.utils.central_african_countries import getCentralAfricanCountries
from app.models.linearRegression import linear_regression


def load_data(file_path):
    data = pd.read_csv(file_path)

    central_african_countries = getCentralAfricanCountries()

    filtered_data = data[data["Country"].isin(central_african_countries)]
    filtered_data["Year"] = pd.to_numeric(filtered_data["Year"], errors="coerce")
    filtered_data["Alcohol"] = filtered_data["Alcohol"].fillna(
        filtered_data["Alcohol"].mean()
    )
    mean_values = (
        filtered_data.groupby(["Country", "Year"])[
            [
                "Life expectancy ",
                "Adult Mortality",
                "infant deaths",
                "Schooling",
                "under-five deaths ",
                "Alcohol",
            ]
        ]
        .mean()
        .reset_index()
    )
    return mean_values


def predict_alcohol_consumption(country_data, country, year):
    subset = country_data[country_data["Country"] == country]
    X = subset["Year"].values
    y = subset["Alcohol"].values

    if len(X) == 0 or len(y) == 0:
        return 0

    slope, intercept = linear_regression(X, y)
    prediction = slope * year + intercept
    return prediction


def get_alcohol_consumption_prediction(file_path, country, year):
    data = load_data(file_path)
    return predict_alcohol_consumption(data, country, year)
