import pandas as pd
import streamlit as st
from src.fetch_data import fetch_stock_data
from src.indicators import (
    add_moving_average,
    add_rsi,
    add_macd,
    add_volume_analysis,
    add_breakout,
)
from src.signals import detect_golden_cross
from src.signals import detect_dead_cross
from src.signals import detect_pullback
from src.ranking import create_ranking
from config.tickers import TICKERS

def view_ranking() -> pd.DataFrame:
  results = []
  for ticker in TICKERS:
      df = fetch_stock_data(ticker)
      df = add_moving_average(df)
      df = add_rsi(df)
      df= add_macd(df)
      df = add_volume_analysis(df)
      df = add_breakout(df)


      df = detect_golden_cross(df)
      df = detect_dead_cross(df)

      df = detect_pullback(df)

      df = create_ranking(df)
      #最新日のデータを取得
      latest = df.iloc[-1]
      results.append(
      {
          "Ticker": ticker,
          "Score": latest["Score"],
      }
      )
  ranking_df = pd.DataFrame(results)
  return ranking_df

st.title("📈 株価分析アプリ")

st.write("こんにちは！")
st.dataframe(view_ranking())
