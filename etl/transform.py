# transform.py
import pandas as pd

def transform(clients, accounts, transactions, all_prices):
    #clean csv data - set ids to type int and date as datetime. Format ticker
    clients['client_id'] = clients['client_id'].astype(int)
    accounts['account_id'] = accounts['account_id'].astype(int)
    transactions['date'] = pd.to_datetime(transactions['date'])
    transactions['ticker'] = transactions['ticker'].str.upper()

    # Clean price column names
    all_prices = all_prices.drop(columns=["Dividends", "Stock Splits"], errors="ignore")
    all_prices = all_prices.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    # Merge transactions with latest price
    latest_prices = all_prices.sort_values('date').groupby('ticker').tail(1)
    trx_with_price = transactions.merge(latest_prices[['ticker', 'close']], on='ticker', how='left')

    # Build holdings
    holdings = (
        trx_with_price.groupby(['account_id', 'ticker'])
        .agg({
            'quantity': 'sum',
            'price': 'mean',
            'close': 'last'
        })
        .reset_index()
    )
    holdings["market_value"] = holdings["quantity"] * holdings["close"]
    holdings = holdings.rename(columns={"price": "avg_cost", "close": "latest_price"})

    return clients, accounts, transactions, holdings, all_prices

