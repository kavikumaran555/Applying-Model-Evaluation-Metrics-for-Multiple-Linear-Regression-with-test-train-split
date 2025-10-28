# Applying-Model-Evaluation-Metrics-for-Multiple-Linear-Regression-with-test-train-split
Project Title

Engine Mileage Prediction using Linear Regression

Project Overview

This project applies a Multiple Linear Regression model to predict a car’s Miles per Gallon (MPG) using features like Engine Size, Weight, and Horsepower.
It demonstrates how to split data into training and testing sets, train a model, and evaluate performance using R² Score and Mean Absolute Error (MAE).

Dataset

The dataset file used:
engine_mileage_data.csv

Columns:

Engine_Size — engine capacity in liters

Weight — vehicle weight in kilograms or pounds

Horsepower — engine power output

Miles_per_Gallon — fuel efficiency (target variable)

Steps in the Code

Import necessary Python libraries.

Load and display the dataset using pandas.

Split features (X) and target (y).

Split data into training and testing sets using train_test_split.

Train the Linear Regression model.

Predict mileage using test data.

Evaluate model accuracy using:

R² Score — measures model fit (closer to 1 = better).

Mean Absolute Error (MAE) — measures prediction difference (lower = better).

Libraries Used

pandas

numpy

scikit-learn (sklearn)

matplotlib
