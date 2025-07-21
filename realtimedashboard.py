import streamlit as st
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup


#defined heading
st.header('Real Time Stock Prices')
#defined side optionbar
ticker = st.sidebar.text_input('Symbol Code','INFY')
exchange = st.sidebar.text_input('Exchange','NSE')

#defined data to be fetched from url
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
response = requests.get(url)

#parsed the data from html format
soup = BeautifulSoup(response.text,'html.parser')

#defined what data to exactly extract
class1 = "YMlKec fxKbKc"
price=float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
st.write(price)
print(response.status_code)

