import nselib
from nselib import capital_market
import streamlit as st

st.header('Indian Stock Market Dashboard')
instrument = st.sidebar.selectbox('Intrument Type', options=('NSE Equity Market','NSE Derivatives Market'))
#Applying conditions and the required functions from library under each instrument type
if instrument == 'NSE Equity Market':
    data_info = st.sidebar.selectbox('Data to Extract',options=('bhav_copy_with_delivery','equity_list','fno_equity_list','market_watch_all_indices','nifty50_equity_list','block_deals_data','bulk_deals_data'))
    #segragting functions according to number of inputs needed to give the output
    if (data_info == 'equity_list') or (data_info == 'fno_equity_list') or (data_info == 'nifty50_equity_list'):
        #capital_market.equity_list()
        #getattr(capital market,'equity_list()') is same as above line
        data =  getattr(capital_market,data_info)() #extra () to get 
        
    if (data_info == 'bhav_copy_with_delivery'):
        date = st.sidebar.text_input('Date','22-12-2023') #default value set
        data = getattr(capital_market,data_info)(date)
         
    if (data_info == 'block_deals_data') or (data_info == 'bulk_deals_data'):
        period_ = st.sidebar.text_input('Period', '1M')
        data = getattr (capital_market, data_info)(period = period_ )
        
st.write(data)

    