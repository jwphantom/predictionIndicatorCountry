import pandas as pd
import numpy as np

from app.utils.central_african_countries import getCentralAfricanCountries

from app.models.linearRegression import linear_regression


def load_data(file_path):
    data = pd.read_csv(file_path)

    central_african_countries = getCentralAfricanCountries()

    filtered_data = data[data["Country"].isin(central_african_countries)]
    filtered_data["Year"] = pd.to_numeric(filtered_data["Year"], errors="coerce")
    mean_life_expectancy = (
        filtered_data.groupby(["Country", "Year"])["Life expectancy "]
        .mean()
        .reset_index()
    )
    return mean_life_expectancy


def predict_life_expectancy(country_data, country, year):
    subset = country_data[country_data["Country"] == country]
    X = subset["Year"].values
    y = subset["Life expectancy "].values

    if len(X) == 0 or len(y) == 0:
        return 0

    slope, intercept = linear_regression(X, y)
    prediction = slope * year + intercept
    return prediction


def get_life_expectancy_prediction(file_path, country, year):
    data = load_data(file_path)
    return predict_life_expectancy(data, country, year)
