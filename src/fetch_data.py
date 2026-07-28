import yfinance as yf

def fetch_stock_data(ticker:str,period:str = "1y",):
  """株価データを取得する"""
  df = yf.download(
    ticker,
    period=period,
    progress=False,
  )

  # MultiIndexを1階層にする
  if df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

  return df