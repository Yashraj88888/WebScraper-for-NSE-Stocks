import streamlit as st
import websocket
import json
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx

# Initialize session state for stock data
if "stock_data" not in st.session_state:
    st.session_state["stock_data"] = []

# WebSocket message handler
def on_message(ws, message):
    try:
        data = json.loads(message)
        st.session_state["stock_data"] = data  # Update session state with received data
        print(f"Received data: {data}")  # Debugging log
    except Exception as e:
        print(f"Error processing message: {e}")

# WebSocket error handler
def on_error(ws, error):
    print(f"WebSocket Error: {error}")

# WebSocket close handler
def on_close(ws, close_status_code, close_message):
    print("WebSocket connection closed.")

# WebSocket open handler
def on_open(ws):
    print("Connected to WebSocket server.")

# Function to start WebSocket connection
def start_websocket():
    ws_url = "ws://localhost:8000/ws"  # Replace with your WebSocket server URL
    ws = websocket.WebSocketApp(
        ws_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open,
    )
    ws.run_forever()

# Start WebSocket in a separate thread with Streamlit context
if "websocket_thread" not in st.session_state:
    thread = threading.Thread(target=start_websocket, daemon=True)
    add_script_run_ctx(thread)  # Ensures Streamlit context is added to the thread
    thread.start()
    st.session_state["websocket_thread"] = thread

# Display data in the Streamlit app
st.title("Real-Time Indian Stock Prices")

if st.session_state["stock_data"]:
    st.subheader("Stock Prices and Percentage Changes")
    for stock in st.session_state["stock_data"]:
        st.write(f"{stock['symbol']}: ₹{stock['price']} ({stock['percent_change']})")
else:
    st.info("Waiting for data...")
