import yfinance as yf

def fetch_stock_data(ticker:str,name:str,period:str = "1y",):
  """株価データを取得する"""
  df = yf.download(
    ticker,
    period=period,
    progress=False,
  )

  # 銘柄名を追加
  df["name"] = name

  # MultiIndexを1階層にする
  if df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

  return df