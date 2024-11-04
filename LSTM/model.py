# model.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.layers import Input

def load_and_train_model():
    # Load and preprocess data
    data = pd.read_csv("sofi_historical_data.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['Volume'] = data['Volume'].str.replace(',', '').astype(float)

    data['5_day_avg'] = data['Close'].rolling(window=5).mean()
    data['10_day_avg'] = data['Close'].rolling(window=10).mean()
    data['lag_1'] = data['Close'].shift(1)
    data.dropna(inplace=True)

    # Define features and target
    x = data[['lag_1', '5_day_avg', '10_day_avg']]
    y = data['Close']

    # Separate scalers for features (X) and target (y)
    x_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()

    # Fit and transform X and y separately
    x_scaled = x_scaler.fit_transform(x)
    y_scaled = y_scaler.fit_transform(y.values.reshape(-1, 1))

    # Reshape X for LSTM model
    x_scaled = x_scaled.reshape((x_scaled.shape[0], 1, x_scaled.shape[1]))

    # Split into train/test sets
    train_size = int(len(x_scaled) * 0.8)
    x_train, x_test = x_scaled[:train_size], x_scaled[train_size:]
    y_train, y_test = y_scaled[:train_size], y_scaled[train_size:]

    # LSTM Model
    model = Sequential()
    model.add(Input(shape=(x_train.shape[1], x_train.shape[2])))
    model.add(LSTM(50, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(x_train, y_train, epochs=50, batch_size=16, validation_data=(x_test, y_test), verbose=0)

    return model, x_scaler, y_scaler, x_test, y_test
