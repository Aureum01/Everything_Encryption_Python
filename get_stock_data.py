import requests

# Define the function that gets stock data
def get_stock_data(symbol):
    # Use the Yahoo Finance API to get the stock data
    res = requests.get(
        f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary?symbol={symbol}",
        headers={
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "<your-api-key>"
        }
    )

    # Return the stock data
    return res.json()

# Define the symbols for the stocks you want to get data for
symbols = ["AAPL", "GOOGL", "TSLA", "MSFT"]

# Get the stock data for each symbol
for symbol in symbols:
    data = get_stock_data(symbol)

    # Print the stock data to the console
    print(f"{symbol}: {data['regularMarketPrice']['raw']}")
