import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# A simple stock app

Shown are the stock closing price and volume of TCS!
""")

tickerSymbol='TCS.NS'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='id',start='2010-01-01',end='2024-02-10')
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
