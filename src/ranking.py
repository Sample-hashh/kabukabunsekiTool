import pandas as pd

def create_ranking(df:pd.DataFrame) -> pd.DataFrame:
  """おすすめスコアを計算する"""

  score = 0
  score += df["GC"].astype(int) * 30
  score += (df["MACD"] > df["Signal"]).astype(int) * 20
  score += df["RSI"].between(40,60).astype(int) * 15
  score += (df["Volume_Ratio"] >= 2).astype(int) * 15
  score += df["Breakout"].astype(int) * 10
  score += df["Pullback"].astype(int) * 10

  df["Score"] = score

  return df