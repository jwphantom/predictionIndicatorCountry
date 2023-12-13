import base64
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np
import seaborn as sns
import pandas as pd
from flask import Flask, send_file


class GraphicGenerator:
    @staticmethod
    def generate_correlation_matrix(data, columns_of_interest):
        # Calcul de la matrice de corrélation
        correlation_matrix = data[columns_of_interest].corr()

        # Créez une figure pour afficher la matrice de corrélation
        fig = Figure(figsize=(12, 8))
        ax = fig.subplots()

        # Utilisez seaborn pour afficher la matrice de corrélation sous forme de heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix of Selected Factors")

        # Convertissez la figure en une image base64
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        imageBase64 = "data:image/png;base64," + data

        return imageBase64

    @staticmethod
    def generate_scatter_plot_base64(
        data, x_col, y_col, label_col, title, x_label, y_label
    ):
        town_names = ["Yaoundé", "Douala", "Bafoussam"]

        fig = Figure()

        ax = fig.subplots()

        for i in range(len(data)):
            ax.scatter(data[x_col][i], data[y_col][i], label=data[label_col][i])

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.legend()
        ax.grid(True)

        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        imageBase64 = "data:image/png;base64," + data

        return imageBase64

    @staticmethod
    def generate_histogram(data, x_col):
        fig = Figure()
        ax = fig.subplots()

        x_values = range(1, len(data) + 1)
        labels = x_col

        colors = [
            "#5B47FB",
            "#9e93ff",
            "#8275f9",
            "orange",
            "purple",
            "#50C878",
            "#ED2939",
            "#40E0D0",
            "#FFD700",
        ]

        # Assurez-vous que la longueur des étiquettes et des données est la même
        assert len(labels) == len(
            data
        ), "Le nombre d'étiquettes doit correspondre au nombre de données"

        # Création des barres avec les étiquettes
        for x, y, color, label in zip(x_values, data, colors, labels):
            ax.bar(x, y, color=color, label=label)

        ax.set_xticks(x_values)

        # Ici, vous pouvez choisir de ne pas inclure toutes les étiquettes dans la légende si elles sont trop nombreuses
        ax.legend()

        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        imageBase64 = "data:image/png;base64," + data

        return imageBase64
