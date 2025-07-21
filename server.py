from fastapi import FastAPI, WebSocket
import requests
from bs4 import BeautifulSoup
import asyncio

app = FastAPI()

# List of stock symbols
stock_symbols = [
    {'symbol': 'ADANIENT', 'exchange': 'NSE'},
    {'symbol': 'RELIANCE', 'exchange': 'NSE'},
    {'symbol': 'TCS', 'exchange': 'NSE'},
    {'symbol': 'INFY', 'exchange': 'NSE'},
]

# Function to fetch stock data
async def fetch_stock_data(symbol, exchange):
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

# Websocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        stock_data = []
        for stock in stock_symbols:
            symbol, exchange = stock['symbol'], stock['exchange']
            price, percent_change, error = await fetch_stock_data(symbol, exchange)
            if price is not None and percent_change is not None:
                stock_data.append({'symbol': symbol, 'price': price, 'percent_change': percent_change})
        await websocket.send_json(stock_data)
        await asyncio.sleep(1)  # Fetch updates every 60 seconds
