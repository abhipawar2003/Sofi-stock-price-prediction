# Stock Price Prediction with LSTM and Gradient Boosting

This repository contains two implementations for predicting stock closing prices:
- **LSTM (Long Short-Term Memory)** Neural Network
- **Gradient Boosting Regressor**

- **The Notebook connect.ipynb contains the complete code refer this for the accuracy metrics and graphs visualization**

Each model implementation has its own directory with a `main.py` script to run predictions for today’s and tomorrow’s closing prices based on historical stock data.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Data Requirements](#data-requirements)
- [Usage](#usage)
  - [Running LSTM Model](#running-lstm-model)
  - [Running Gradient Boosting Model](#running-gradient-boosting-model)
- [Files and Directories](#files-and-directories)
- [License](#license)

## Project Overview

The project aims to predict stock closing prices based on historical data using two different approaches: a sequential LSTM model and a structured Gradient Boosting model. Both models rely on feature engineering, including moving averages and lagged prices, to capture patterns in stock price movements.

## Features

- **Data Preprocessing**: Handles missing values, scales data, and adds moving averages and lagged features.
- **Feature Engineering**: Adds useful indicators like moving averages and lagged values for short-term trend analysis.
- **Predictive Models**:
  - **LSTM** for sequential data prediction.
  - **Gradient Boosting Regressor** for structured, tabular prediction.
- **Accuracy Metrics**: Reports Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) for both training and testing data.

## Getting Started

### Installation

Clone the repository and install the required dependencies.

```bash
git clone https://github.com/abhipawar2003/Sofi-stock-price-prediction.git
cd your-repository
pip install -r requirements.txt

cd LSTM
# LSTM Stock Price Prediction

This directory contains code for predicting stock closing prices using an **LSTM (Long Short-Term Memory)** model, a type of recurrent neural network suited for time series data.

## Overview

The LSTM model predicts today’s and tomorrow’s stock closing prices based on historical price data, utilizing features like moving averages and lagged prices to capture trends.

## Requirements

Ensure the following dependencies are installed:

```bash
pip install -r ../requirements.txt

python3 main.py 

cd gradient_boosting

---

### `Gradient_Boosting/README.md`

```markdown
# Gradient Boosting Stock Price Prediction

This directory contains code for predicting stock closing prices using a **Gradient Boosting Regressor**, a structured machine learning model suitable for tabular data.

## Overview

The Gradient Boosting Regressor predicts today’s and tomorrow’s stock closing prices by leveraging historical price data. It uses engineered features such as moving averages and lagged prices to model price patterns.

## Requirements

Install the necessary dependencies using:

```bash
pip install -r ../requirements.txt

python3 main.py





---
License 
Each `README.md` is tailored for the specific model in its folder, outlining dependencies, data requirements, usage instructions, and relevant files. This setup makes each model self-contained and easy for others to understand and use. Let me know if you'd like further customization!
