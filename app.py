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
NIKEIS = {}


def view_GCDC() -> pd.DataFrame:
  NIKEIS = get_nikkei_tickers()
  results = []

  for ticker, name in NIKEIS.items():
      df = fetch_stock_data(ticker,name)
      df = add_moving_average(df)

      df = detect_golden_cross(df)
      df = detect_dead_cross(df)

      #最新日のデータを取得
      latest = df.iloc[-1]
      results.append(
      {
        "銘柄": ticker,
        "銘柄名": latest["name"],
        "終値": latest["Close"],
        "出来高": latest["Volume"],
        "MA5": latest["MA5"],
        "MA25": latest["MA25"],
        "MA75": latest["MA75"],
        "ゴールデンクロス_5日＆25日": latest["GC_5and25"],
        "ゴールデンクロス_25日＆75日": latest["GC_25and75"],
        "デッドクロス_5日＆25日": latest["DC_5and25"],
        "デッドクロス_25日＆75日": latest["DC_25and75"],        
      }
      )
  # 全行表示する
  pd.set_option("display.max_rows", None)
  # 全列表示する
  pd.set_option("display.max_columns", None)

  result_df = pd.DataFrame(results)

  # 出来高順に並び替える
  df_volume = result_df.sort_values(by="出来高",ascending=False)

  return df_volume

print(view_GCDC())

# st.title("📈 株価分析アプリ")

# st.write("こんにちは！")
# st.dataframe(view_GCDC())
