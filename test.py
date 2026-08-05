import pandas as pd
import streamlit as st
from config.tickers import (get_nikkei_tickers,test_get_nikkei_tickers)
from src.fetch_data import fetch_stock_data
from src.indicators import (
    add_moving_average,

)
from src.signals import detect_golden_cross
from src.signals import detect_dead_cross

#日経225を取得
# NIKEI = get_nikkei_tickers()
NIKEI = test_get_nikkei_tickers()




df = fetch_stock_data(NIKEI[1])
df = add_moving_average(df)

df = detect_golden_cross(df)
df = detect_dead_cross(df)

print(df.tail(5))

