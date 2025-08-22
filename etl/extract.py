#extract.py

import pandas as pd
import yfinance as yf

def extract(csv_folder='data/raw'):
    #reading in the csvs
    clients = pd.read_csv(f"{csv_folder}/clients.csv")
    accounts = pd.read_csv(f"{csv_folder}/accounts.csv")
    transactions = pd.read_csv(f"{csv_folder}/transactions.csv")
    securities = pd.read_csv(f"{csv_folder}/securities.csv")

    # Pull prices & metadata from yfinance
    tickers = securities['ticker'].unique().tolist()
    all_prices = pd.DataFrame()
    all_meta = []

    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(start="2023-01-01", end="2023-03-31").reset_index()
        hist['ticker'] = symbol
        all_prices = pd.concat([all_prices, hist])

        info = ticker.info
        all_meta.append({
            "ticker": symbol,
            "name": info.get('longName', symbol),
            "sector": info.get('sector', "Unknown"),
            "currency": info.get('currency', "USD")
        })

    yf_securities = pd.DataFrame(all_meta)

    return clients, accounts, transactions, securities, all_prices, yf_securities