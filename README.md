# Stock Portfolio ETL Project

## Overview
This project demonstrates a **full ETL pipeline** for a mock stock portfolio management system. The pipeline extracts client, account, transaction, and security data, retrieves stock prices and metadata from Yahoo Finance, transforms the data to calculate holdings and market values, and loads everything into a SQLite database.  

A Jupyter notebook is included for **data exploration and visualization**, showing portfolio values, top holdings, and diversification per client. That is titled etl_demo.ipynb in the notebooks folder (see structure below).

---

## Folder Structure

stock-portfolio-etl/
│
├── data/
│ └── raw/ # CSVs for clients, accounts, transactions, securities
├── etl/
│ ├── init.py # makes folder a package
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── pipeline.py # main pipeline
├── notebooks/
│ └── etl_demo.ipynb # analysis and visualizations
├── venv/ # optional virtual environment
├── requirements.txt
├── README.md
└── .gitignore

## Requirements

- Python 3.11+  
- Packages listed in `requirements.txt`:

## Example packages:

pandas
yfinance
sqlalchemy
matplotlib

## How to Run
### 1. Run ETL Pipeline
From the project root:
`python -m etl.pipeline`

This will extract data from CSVs and Yahoo Finance, transform it, and load all tables into data/stock_data.db.

2. Explore & Visualize Data
Open the notebook:

jupyter notebook notebooks/etl_demo.ipynb
The notebook connects to the SQLite database and produces:

Portfolio value per client (bar chart)

Top 10 holdings across all clients (bar chart)

Individual client portfolio diversification (pie chart)

Optional Demo
A small sample database data/stock_data.db can be included to allow running the notebook without fetching live Yahoo Finance data.

Portfolio Highlights
Modular ETL design (extract.py, transform.py, load.py)

Uses Python packages for data analysis, database handling, and plotting

Professional-ready structure suitable for GitHub portfolio

Includes visual storytelling in Jupyter notebook for recruiters or technical reviewers