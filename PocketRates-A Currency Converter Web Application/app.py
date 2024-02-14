import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import requests
import json

image=Image.open("logo.png")
st.image(image,width=390)
st.title("Currency Converter App")
st.markdown("""
This app converts currency values 
""")

st.sidebar.header("Input Options")
currency_list={'INR', 'USD','CAD', 'CNY', 'EUR', 'GBP', 'JPY', 'CHF', 'AUD', 'NZD'}
base_price_unit=st.sidebar.selectbox('Select base currency',currency_list)
symbols_price_unit=st.sidebar.selectbox('Select target currency',currency_list)

@st.cache
def load_data():
        url = ''.join(['https://api.ratesapi.io/api/latest?base=', base_price_unit, '&symbols=', symbols_price_unit])
        response = requests.get(url)
        data = response.json()
        base_currency = pd.Series( data['base'], name='base_currency')
        rates_df = pd.DataFrame.from_dict( data['rates'].items() )
        rates_df.columns = ['converted_currency', 'price']
        conversion_date = pd.Series( data['date'], name='date' )
        df = pd.concat( [base_currency, rates_df, conversion_date], axis=1 )
        return df

df = load_data()

st.header('Currency conversion')

st.write(df)

st.header('Currency conversion chart')

st.line_chart(df['price'])