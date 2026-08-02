import pandas as pd

def add_moving_average(df: pd.DataFrame) -> pd.DataFrame:
  """移動平均線を追加する"""

  df["MA5"] = df["Close"].rolling(window=5).mean()
  df["MA25"] = df["Close"].rolling(window=5).mean()
  df["MA75"] = df["Close"].rolling(window=5).mean()

  return df

def add_rsi(df:pd.DataFrame,period:int=14) -> pd.DataFrame:
  """RSIを追加する"""

  #前日との差分
  delta = df["Close"].diff()
  #上昇した日だけ取り出す
  gain = delta.clip(lower=0)
  #下落した日だけ取り出す
  loss = -delta.clip(upper=0)
  #14日平均を求める
  avg_gain = gain.rolling(14).mean()
  avg_loss = loss.rolling(14).mean()
  #rsを計算
  rs = avg_gain / avg_loss
  #RSIを計算
  df["RSI"] = 100 - (100/(1 + rs))

  return df

def add_macd(df:pd.DataFrame) -> pd.DataFrame:
  """MACDを追加する"""
  ema12 = df["Close"].ewm(span=12,adjust=False).mean()
  ema26 = df["Close"].ewm(span=26,adjust=False).mean()

  df["MACD"] = ema12 - ema26
  df["Signal"] = df["MACD"].ewm(span=9,adjust=False).mean()
  df["Histogram"] = df["MACD"] - df["Signal"]
  return df

def add_volume_analysis(df:pd.DataFrame) -> pd.DataFrame:
  """出来高分析を追加する"""

  #20日平均出来高
  df["Volume_MA20"] = df["Volume"].rolling(window=20).mean()

  #今日の出来高は平均の何倍か
  df["Volume_Ratio"] = df["Volume"] / df["Volume_MA20"]

  return df

def add_breakout(df:pd.DataFrame,period:int=20) -> pd.DataFrame:
  """高値更新(ブレイクアウト)を判定する"""

  #過去20日の最高値
  df["High20"] = df["High"].rolling(window=period).max()
  #昨日までの最高値
  previous_high = df["High20"].shift(1)
  #高値更新
  df["Breakout"] = df["Close"] > previous_high

  return df





