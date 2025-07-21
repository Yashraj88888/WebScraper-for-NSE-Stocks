import nsepy as nse
from datetime import date

# Fetch historical data for INFY
try:
    stock_price = nse.get_history(symbol='INFY', index=False, start=date(2024, 7, 30), end=date(2024, 9, 30))
    if stock_price.empty:
        print("No data available for the given date range.")
    else:
        print(stock_price)
except Exception as e:
    print(f"An error occurred: {e}")
