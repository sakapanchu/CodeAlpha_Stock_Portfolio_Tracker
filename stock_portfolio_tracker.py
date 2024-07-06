import requests
import json
import pandas as pd

# Constants
API_KEY = 'MQULRNI61A8AWKBT'
PORTFOLIO_FILE = 'portfolio.json'

# Functions to interact with the Alpha Vantage API
def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (5min)' in data:
            return data
        else:
            error_message = data.get('Note', data.get('Error Message', 'Unknown error'))
            print(f"Error fetching data for {symbol}: {error_message}")
            return None
    else:
        print(f"HTTP Error {response.status_code} for {symbol}")
        return None

def is_valid_symbol(symbol):
    data = get_stock_data(symbol)
    return data is not None

def get_stock_performance(symbol):
    data = get_stock_data(symbol)
    if data:
        time_series = data.get('Time Series (5min)', {})
        if time_series:
            df = pd.DataFrame.from_dict(time_series, orient='index').astype(float)
            latest_price = df['4. close'].iloc[0]
            return latest_price
    return None

# Functions to manage the portfolio
def load_portfolio():
    try:
        with open(PORTFOLIO_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(portfolio, f)

def add_stock(symbol, shares):
    if is_valid_symbol(symbol):
        portfolio = load_portfolio()
        if symbol in portfolio:
            portfolio[symbol] += shares
        else:
            portfolio[symbol] = shares
        save_portfolio(portfolio)
        print(f"Added {shares} shares of {symbol}")
    else:
        print(f"Invalid stock symbol: {symbol}. Portfolio not updated.")

def remove_stock(symbol):
    portfolio = load_portfolio()
    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"Removed {symbol}")
    else:
        print(f"{symbol} not found in portfolio")

def view_portfolio():
    portfolio = load_portfolio()
    if portfolio:
        for symbol, shares in portfolio.items():
            print(f"{symbol}: {shares} shares")
    else:
        print("Portfolio is empty")

def calculate_portfolio_performance():
    portfolio = load_portfolio()
    total_value = 0
    for symbol, shares in portfolio.items():
        price = get_stock_performance(symbol)
        if price:
            total_value += price * shares
            print(f"{symbol}: {shares} shares @ {price} each = {shares * price}")
        else:
            print(f"Failed to fetch data for {symbol}")
    print(f"Total portfolio value: {total_value}")

# Main program
def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")# possible stock symbols -- AAPL,F,GM,MSFT,FB,TSLA,JPM,BAC,C,JNJ,PFE,MRK,KO,PG,PEP...ect..
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Calculate Performance")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            calculate_portfolio_performance()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()

