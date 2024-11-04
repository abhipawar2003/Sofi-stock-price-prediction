
import pandas as pd

def predict_tomorrow_price(model, x_scaler, y_scaler, data):
    # Prepare the latest data for prediction as a DataFrame
    latest_data = pd.DataFrame([data[['lag_1', '5_day_avg', '10_day_avg']].iloc[-1]])
    latest_data_scaled = x_scaler.transform(latest_data).reshape((1, 1, latest_data.shape[1]))

    # Predict tomorrow's price in the scaled range
    tomorrow_price_scaled = model.predict(latest_data_scaled)

    # Inverse transform to get the price in the original scale
    tomorrow_price = y_scaler.inverse_transform([[tomorrow_price_scaled[0][0]]])[0][0]

    return tomorrow_price
