# Stock Portfolio Tracker

The Stock Portfolio Tracker is a Python-based application that allows users to manage and track their stock investments. The application provides functionality to add, remove, view stocks in a portfolio, and calculate the performance of the portfolio using real-time stock data from the Alpha Vantage API.

## Features

- **Add Stock**: Add stocks to your portfolio by specifying the stock symbol and the number of shares. The application validates the stock symbol before adding it to the portfolio.
- **Remove Stock**: Remove stocks from your portfolio by specifying the stock symbol.
- **View Portfolio**: View the current stocks in your portfolio along with the number of shares.
- **Calculate Performance**: Calculate the total value of your portfolio based on real-time stock prices fetched from the Alpha Vantage API.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

You can install the required libraries using the following command:

```bash
pip install requests pandas
```

# Setup

- Clone the repository or download the source code.

- Replace the API_KEY in the script with your own Alpha Vantage API key. You can get a free API key by signing up at Alpha Vantage.

- Save the code in a file named stock_portfolio_tracker.py.

# Usage

Run the stock_portfolio_tracker.py script:

```bash
    Copy code
    python stock_portfolio_tracker.py
```

Follow the on-screen instructions to manage your stock portfolio.

# Code Overview

## Functions

-**get_stock_data(symbol)**: Fetches real-time stock data for the given symbol from the Alpha Vantage API.
-**is_valid_symbol(symbol)**: Validates the given stock symbol by checking if data can be fetched for it.
-**get_stock_performance(symbol)**: Retrieves the latest stock price for the given symbol.
-**load_portfolio()**: Loads the current portfolio from a JSON file.
-**save_portfolio(portfolio)**: Saves the current portfolio to a JSON file.
-**add_stock(symbol, shares)**: Adds the specified number of shares of the given stock symbol to the portfolio.
-**remove_stock(symbol)**: Removes the given stock symbol from the portfolio.
-**view_portfolio()**: Displays the current stocks in the portfolio.
-**calculate_portfolio_performance()**: Calculates and displays the total value of the portfolio based on real-time stock prices.

# Main Program

The main program provides a menu-based interface for the user to interact with the application. The user can choose to add, remove, view stocks in the portfolio, or calculate the portfolio's performance.

# Example

```bash
Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 1
Enter stock symbol: AAPL
Enter number of shares: 10
Added 10 shares of AAPL

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 1
Enter stock symbol: SLT
Enter number of shares: 30
Error fetching data for SLT: Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY.
Invalid stock symbol: SLT. Portfolio not updated.

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 1
Enter stock symbol: GM
Enter number of shares: 30
Added 30 shares of GM

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 3
AAPL: 10 shares
GM: 30 shares

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 4
AAPL: 10 shares @ 226.5 each = 2265.0
GM: 30 shares @ 46.42 each = 1392.6000000000001
Total portfolio value: 3657.6000000000004

Stock Portfolio Tracker
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Calculate Performance
5. Exit
Choose an option: 5

Process finished with exit code 0
```
