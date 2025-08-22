# load.py
from sqlalchemy import create_engine

def load(clients, accounts, transactions, securities, all_prices, holdings, db_path="data/stock_data.db"):
    engine = create_engine(f"sqlite:///{db_path}")

    clients.to_sql('clients', engine, index=False, if_exists='replace')
    accounts.to_sql('accounts', engine, index=False, if_exists='replace')
    transactions.to_sql('transactions', engine, index=False, if_exists='replace')
    securities.to_sql('securities', engine, index=False, if_exists='replace')
    all_prices.to_sql('all_prices', engine, index=False, if_exists='replace')
    holdings.to_sql('holdings', engine, index=False, if_exists='replace')

    print("Data Loaded into Sqlite - Good job buddy")

