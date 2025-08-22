#pipeline.py

from .extract import extract
from .transform import transform
from .load import load

def run_etl():

    #Extract function to return 6 dataframes based on the tuple set in extract.py file
    clients, accounts, transactions, securities, all_prices, yf_securities = extract()

    #tranform function to return transformed dataframes from tranform.py
    clients, accounts, transactions, holdings, all_prices = transform(clients, accounts, transactions, all_prices)

    #load into sql database
    load(clients, accounts, transactions, securities, all_prices, holdings)

if __name__ == "__main__":
    run_etl()