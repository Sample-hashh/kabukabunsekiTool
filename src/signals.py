import pandas as pd

def detect_golden_cross(df:pd.DataFrame) -> pd.DataFrame:
  """ゴールデンクロスを判定する"""
  df["GC"] = ((df["MA25"].shift(1)<df["MA75"].shift(1)) & (df["MA25"] >= df["MA75"]))

  return df

def detect_dead_cross(df:pd.DataFrame) -> pd.DataFrame:
  """デッドクロスを判定する"""

  df["DC"] = ((df["MA25"].shift(1) > df["MA75"].shift(1)) & (df["MA25"] <= df["MA75"]))

  return df