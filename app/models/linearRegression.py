import numpy as np


def linear_regression(X, y):
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    X_y_mean = np.mean(X * y)
    X_square_mean = np.mean(X**2)

    slope = (X_mean * y_mean - X_y_mean) / (X_mean**2 - X_square_mean)
    intercept = y_mean - slope * X_mean
    return (slope, intercept)
