import pandas as pd

def add_moving_average(df: pd.DataFrame) -> pd.DataFrame:
  """移動平均線を追加する"""

  df["MA5"] = df["Close"].rolling(window=5).mean()
  df["MA25"] = df["Close"].rolling(window=5).mean()
  df["MA75"] = df["Close"].rolling(window=5).mean()

  return df