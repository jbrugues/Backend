import yfinance as yf
import pandas as pd

# Download some stock data
ticker = "SPY"
data = yf.download(ticker, start="2024-01-01", end="2024-12-31")

print(f"Downloaded {len(data)} days of data for {ticker}")
print(data.head())
