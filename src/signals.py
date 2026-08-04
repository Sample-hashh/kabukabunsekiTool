import pandas as pd

def detect_golden_cross(df:pd.DataFrame) -> pd.DataFrame:
  """ゴールデンクロスを判定する"""
  #5日25日
  df["GC_5and25"] = ((df["MA5"].shift(1)<df["MA25"].shift(1)) & (df["MA5"] >= df["MA25"]))
  #25日75日
  df["GC_25and75"] = ((df["MA25"].shift(1)<df["MA75"].shift(1)) & (df["MA25"] >= df["MA75"]))

  return df

def detect_dead_cross(df:pd.DataFrame) -> pd.DataFrame:
  """デッドクロスを判定する"""
  #5日255日
  df["DC_5and25"] = ((df["MA5"].shift(1) > df["MA25"].shift(1)) & (df["MA5"] <= df["MA25"]))
  #25日75日
  df["DC_25and75"] = ((df["MA25"].shift(1) > df["MA75"].shift(1)) & (df["MA25"] <= df["MA75"]))

  return df
