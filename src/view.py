import pandas as pd

from config.tickers import get_nikkei_tickers

from src.fetch_data import fetch_stock_data
from src.indicators import add_moving_average
from src.signals import detect_golden_cross, detect_dead_cross


#日経225を取得
NIKEIS = {}

def Volume_sorted(result_df: pd.DataFrame) -> pd.DataFrame:
  """出来高順に並び替えたデータフレームを返す"""
  df_volume_sorted = result_df.sort_values(by="出来高",ascending=False)
  return df_volume_sorted

def View4_GCDC(view4_df: pd.DataFrame) -> list:
  """GCDC4種類のデータフレーム結果をリストに格納して返却す"""
  viewType = ['ゴールデンクロス_5日＆25日', 'ゴールデンクロス_25日＆75日', 'デッドクロス_5日＆25日', 'デッドクロス_25日＆75日']
  # 4種類の結果を格納するデータフレームリスト
  view4_dfs = []
  for vt in viewType:
     view4 = view4_df[view4_df[vt] == True]
     # 出来高順に並び替える
     df_volume = Volume_sorted(view4)
     view4_dfs.append(df_volume)
  return view4_dfs
  




def view_GCDC() -> pd.DataFrame:
  """ゴールデンクロスとデッドクロスを判定する"""
  NIKEIS = get_nikkei_tickers()
  results = []

  for ticker, name in NIKEIS.items():
      df = fetch_stock_data(ticker,name)

      # 株価取得失敗の場合
      if df.empty:
          print(f"取得失敗: {ticker} {name}")
          continue
  
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
  # 横幅を広げる
  pd.set_option("display.width", 2000) 

  result_df = pd.DataFrame(results)

  df_volumeList = View4_GCDC(result_df)



  return df_volumeList





