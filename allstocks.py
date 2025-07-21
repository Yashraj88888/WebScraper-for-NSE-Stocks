import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

# List of Indian stock symbols and exchanges
stock_symbols = [
    {'symbol': 'ADANIENT', 'exchange': 'NSE'},
    {'symbol': 'TECHM', 'exchange': 'NSE'},
    {'symbol': 'HCLTECH', 'exchange': 'NSE'},
    {'symbol': 'INDUSINDBK', 'exchange': 'NSE'},
    {'symbol': 'SHRIRAMFIN', 'exchange': 'NSE'},
    {'symbol': 'APOLLOHOSP', 'exchange': 'NSE'},
    {'symbol': 'CIPLA', 'exchange': 'NSE'},
    {'symbol': 'SUNPHARMA', 'exchange': 'NSE'},
    {'symbol': 'POWERGRID', 'exchange': 'NSE'},
    {'symbol': 'BRITANNIA', 'exchange': 'NSE'},
    {'symbol': 'ASIANPAINT', 'exchange': 'NSE'},
    {'symbol': 'COALINDIA', 'exchange': 'NSE'},
    {'symbol': 'HINDUNILVR', 'exchange': 'NSE'},
    {'symbol': 'BPCL', 'exchange': 'NSE'},
    {'symbol': 'SBILIFE', 'exchange': 'NSE'},
    {'symbol': 'BAJFINANCE', 'exchange': 'NSE'},
    {'symbol': 'ADANIPORTS', 'exchange': 'NSE'},
    {'symbol': 'NESTLEIND', 'exchange': 'NSE'},
    {'symbol': 'TCS', 'exchange': 'NSE'},
    {'symbol': 'ITC', 'exchange': 'NSE'},
    {'symbol': 'BAJAJFINSV', 'exchange': 'NSE'},
    {'symbol': 'ULTRACEMCO', 'exchange': 'NSE'},
    {'symbol': 'LT', 'exchange': 'NSE'},
    {'symbol': 'EICHERMOT', 'exchange': 'NSE'},
    {'symbol': 'BHARTIARTL', 'exchange': 'NSE'},
    {'symbol': 'TATACONSUM', 'exchange': 'NSE'},
    {'symbol': 'AXISBANK', 'exchange': 'NSE'},
    {'symbol': 'HDFCLIFE', 'exchange': 'NSE'},
    {'symbol': 'DRREDDY', 'exchange': 'NSE'},
    {'symbol': 'RELIANCE', 'exchange': 'NSE'},
    {'symbol': 'HDFCBANK', 'exchange': 'NSE'},
    {'symbol': 'SBIN', 'exchange': 'NSE'},
    {'symbol': 'NTPC', 'exchange': 'NSE'},
    {'symbol': 'BAJAJ-AUTO', 'exchange': 'NSE'},
    {'symbol': 'INFY', 'exchange': 'NSE'},
    {'symbol': 'TATASTEEL', 'exchange': 'NSE'},
    {'symbol': 'ONGC', 'exchange': 'NSE'},
    {'symbol': 'KOTAKBANK', 'exchange': 'NSE'},
    {'symbol': 'ICICIBANK', 'exchange': 'NSE'},
    {'symbol': 'M&M', 'exchange': 'NSE'},
    {'symbol': 'JSWSTEEL', 'exchange': 'NSE'},
    {'symbol': 'MARUTI', 'exchange': 'NSE'},
    {'symbol': 'HEROMOTOCO', 'exchange': 'NSE'},
    {'symbol': 'GRASIM', 'exchange': 'NSE'},
    {'symbol': 'TITAN', 'exchange': 'NSE'},
    {'symbol': 'WIPRO', 'exchange': 'NSE'},
    {'symbol': 'BEL', 'exchange': 'NSE'},
    {'symbol': 'TRENT', 'exchange': 'NSE'},
    {'symbol': 'TATAMOTORS', 'exchange': 'NSE'},
    {'symbol': 'HINDALCO', 'exchange': 'NSE'},
    {'symbol': 'INDUSTOWER', 'exchange': 'NSE'},
    {'symbol': 'CANBK', 'exchange': 'NSE'},
    {'symbol': 'IRFC', 'exchange': 'NSE'},
    {'symbol': 'NMDC', 'exchange': 'NSE'},
    {'symbol': 'OLA', 'exchange': 'NSE'},
    {'symbol': 'MOBIKWIK', 'exchange': 'NSE'},
    {'symbol': 'MOTHERSON', 'exchange': 'NSE'},
    {'symbol': 'BHEL', 'exchange': 'NSE'},
    {'symbol': 'UNIONBANK', 'exchange': 'NSE'},
    {'symbol': 'VAKRANGEE', 'exchange': 'NSE'},
    {'symbol': 'PFC', 'exchange': 'NSE'},
    {'symbol': 'HCC', 'exchange': 'NSE'},
    {'symbol': 'IOC', 'exchange': 'NSE'},
    {'symbol': 'TATAPOWER', 'exchange': 'NSE'},
    {'symbol': 'GMR', 'exchange': 'NSE'},
    {'symbol': 'INDHOTEL', 'exchange': 'NSE'},
    {'symbol': 'ADANIPOWER', 'exchange': 'NSE'},
    {'symbol': 'IREDA', 'exchange': 'NSE'},
    {'symbol': 'KBCGLOBAL', 'exchange': 'NSE'},
    {'symbol': 'RECLTD', 'exchange': 'NSE'},
    {'symbol': 'BANKBARODA', 'exchange': 'NSE'},
    {'symbol': 'GAIL', 'exchange': 'NSE'},
    {'symbol': 'APOLLOMICRO', 'exchange': 'NSE'},
    {'symbol': 'MANAPPURAM', 'exchange': 'NSE'},
    {'symbol': 'JSWENERGY', 'exchange': 'NSE'},
    {'symbol': 'FILATEX', 'exchange': 'NSE'},
    {'symbol': 'VEDL', 'exchange': 'NSE'},
    {'symbol': 'VBL', 'exchange': 'NSE'},
    {'symbol': 'IDEA', 'exchange': 'NSE'},
    {'symbol': 'ZOMATO', 'exchange': 'NSE'},
    {'symbol': 'GREAVESCOT', 'exchange': 'NSE'},
    {'symbol': 'YESBANK', 'exchange': 'NSE'},
    {'symbol': 'PNB', 'exchange': 'NSE'},
    {'symbol': 'ITI', 'exchange': 'NSE'},
    {'symbol': 'NHPC', 'exchange': 'NSE'},
    {'symbol': 'JPPOWER', 'exchange': 'NSE'},
    {'symbol': 'SAGILITY', 'exchange': 'NSE'},
    {'symbol': 'SUZLON', 'exchange': 'NSE'},
    {'symbol': 'FEDERALBNK', 'exchange': 'NSE'},
    {'symbol': 'EASEMYTRIP', 'exchange': 'NSE'},
    {'symbol': 'IDFCFIRSTB', 'exchange': 'NSE'},
    {'symbol': 'JIOFIN', 'exchange': 'NSE'},
    {'symbol': 'GTLINFRA', 'exchange': 'NSE'}
]


# Function to fetch stock price and percentage change from Google Finance
def fetch_stock_data(symbol, exchange):
    url = f'https://www.google.com/finance/quote/{symbol}:{exchange}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None, None, f"HTTP Error {response.status_code}"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find(class_="YMlKec fxKbKc")
    percent_change_element = soup.find(class_="JwB6zf")
    
    try:
        price = float(price_element.text.strip()[1:].replace(",", "")) if price_element else None
        percent_change = percent_change_element.text.strip() if percent_change_element else None
        return price, percent_change, None
    except (ValueError, AttributeError):
        return None, None, "Parsing Error"

# Streamlit UI
st.header("Real-Time Indian Stock Prices and Percentage Changes")

# Fetch and display stock data
stock_data = {}
for stock in stock_symbols:
    symbol, exchange = stock['symbol'], stock['exchange']
    price, percent_change, error = fetch_stock_data(symbol, exchange)
    if price is not None and percent_change is not None:
        stock_data[symbol] = (price, percent_change)
    else:
        st.error(f"Failed to fetch {symbol}: {error}")

# Display stock data
st.subheader("Stock Prices and Percentage Changes")
for i in range(5):
    for symbol, data in stock_data.items():
        price, percent_change = data
        st.write(f"{symbol}: ₹{price} ({percent_change})")

# Periodic update (Streamlit auto-refresh workaround)
time.sleep(60)
