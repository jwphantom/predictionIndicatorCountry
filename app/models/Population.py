import pandas as pd
import numpy as np

from app.utils.central_african_countries import getCentralAfricanCountries
from app.models.linearRegression import linear_regression


def load_data(file_path):
    data = pd.read_csv(file_path)
    central_african_countries = getCentralAfricanCountries()

    filtered_data = data[data["Country"].isin(central_african_countries)]
    filtered_data["Year"] = pd.to_numeric(filtered_data["Year"], errors="coerce")

    # Calculate population growth rate
    filtered_data["Population Growth Rate"] = (
        filtered_data.groupby("Country")["Population"].pct_change() * 100
    )

    # Drop NaN values that result from pct_change()
    filtered_data = filtered_data.dropna(subset=["Population Growth Rate"])

    return filtered_data


def predict_population_growth(country_data, country, year):
    country_df = country_data[country_data["Country"] == country]
    X = country_df["Year"].values
    y = country_df["Population Growth Rate"].values

    if len(X) == 0 or len(y) == 0:
        return 1

    slope, intercept = linear_regression(X, y)
    prediction = slope * year + intercept
    return prediction


def get_population_growth_prediction(file_path, country, year):
    data = load_data(file_path)
    return predict_population_growth(data, country, year)
