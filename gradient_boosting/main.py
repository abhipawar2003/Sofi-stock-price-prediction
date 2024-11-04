# main.py

import time
import pandas as pd
from LSTM.webscrape import scrape_sofi_data
from LSTM.model import load_and_train_model
from LSTM.predict import predict_tomorrow_price

def main():
    while True:
        # Step 1: Scrape data and save it
        scrape_sofi_data()

        # Load and preprocess the data for feature engineering
        data = pd.read_csv("sofi_historical_data.csv")
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        data['Volume'] = data['Volume'].str.replace(',', '').astype(float)

        # Ensure the required columns are created
        data['5_day_avg'] = data['Close'].rolling(window=5).mean()
        data['10_day_avg'] = data['Close'].rolling(window=10).mean()
        data['lag_1'] = data['Close'].shift(1)
        data.dropna(inplace=True)

        # Step 2: Train the model with new data
        model, _, _, _, _ = load_and_train_model()

        # Step 3: Predict tomorrow's price using the latest data
        tomorrow_price = predict_tomorrow_price(model, data)

        # Output the predicted price for tomorrow
        print(f"Predicted closing price for tomorrow: {tomorrow_price}")

        # Wait for 1 hour (3600 seconds) before next iteration
        time.sleep(3600)

if __name__ == "__main__":
    main()
