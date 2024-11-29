import yfinance as yf

# List of currency pairs to fetch
currency_pairs = ['EURUSD=X', 'GBPUSD=X', 'USDPLN=X', 'AUDUSD=X', 'USDCAD=X']

# Fetch data using yfinance
def get_currency_rates(pairs):
    currency_data = {}
    for pair in pairs:
        ticker = yf.Ticker(pair)
        info = ticker.history(period="1d")  # Fetch 1 day of data
        if not info.empty:
            # Extract last closing price
            last_price = info['Close'].iloc[-1]
            currency_data[pair] = last_price
        else:
            currency_data[pair] = "Data unavailable"
    return currency_data

# Display fetched data
currency_rates = get_currency_rates(currency_pairs)
for pair, rate in currency_rates.items():
    print(f"{pair}: {rate}")
