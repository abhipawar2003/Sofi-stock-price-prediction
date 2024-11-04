# predict.py

import numpy as np

def predict_tomorrow_price(model, data):
    # Extract the latest data for prediction
    latest_data = data[['lag_1', '5_day_avg', '10_day_avg']].iloc[-1].values.reshape(1, -1)

    # Predict tomorrow's price
    tomorrow_price = model.predict(latest_data)[0]

    return tomorrow_price
