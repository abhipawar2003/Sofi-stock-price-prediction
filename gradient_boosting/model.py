# model.py

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def load_and_train_model():
    # Load and preprocess data
    data = pd.read_csv("sofi_historical_data.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['Volume'] = data['Volume'].str.replace(',', '').astype(float)

    # Feature Engineering
    data['5_day_avg'] = data['Close'].rolling(window=5).mean()
    data['10_day_avg'] = data['Close'].rolling(window=10).mean()
    data['lag_1'] = data['Close'].shift(1)
    data.dropna(inplace=True)

    # Define features and target
    x = data[['lag_1', '5_day_avg', '10_day_avg']]
    y = data['Close']

    # Split into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

    # Gradient Boosting Model
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    model.fit(x_train, y_train)

    return model, x_train, x_test, y_train, y_test
