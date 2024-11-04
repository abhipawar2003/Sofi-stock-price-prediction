# webscrape.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def scrape_sofi_data():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to SoFi Yahoo Finance page
    driver.get("https://finance.yahoo.com/quote/SOFI/history")
    time.sleep(5)

    # Step 1: Open the Date Range dropdown
    try:
        date_range_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'tertiary-btn') and contains(@class, 'menuBtn')]"))
        )
        date_range_button.click()
        time.sleep(2)
    except Exception as e:
        print("Error opening date range dropdown:", e)

    # Step 2: Select "Max" date range
    try:
        max_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@value='MAX']"))
        )
        max_option.click()
        time.sleep(2)
    except Exception as e:
        print("Error selecting Max date range:", e)

    # Step 3: Scrape historical data
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table yf-h2urb6')]//tbody/tr"))
        )
        rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'table yf-h2urb6')]//tbody/tr")
        historical_data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) == 7:
                historical_data.append([col.text for col in cols])

        # Save data to CSV
        df = pd.DataFrame(historical_data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
        df.to_csv("sofi_historical_data.csv", index=False)
        print("Data saved to sofi_historical_data.csv")
    except Exception as e:
        print("Error scraping historical data:", e)
    finally:
        driver.quit()
