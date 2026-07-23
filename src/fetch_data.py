import yfinance as yf

def fetch_stock_data(ticker:str,period:str = "1y",):
  """株価データを取得する"""
  df = yf.download(
    ticker,
    period=period,
    progress=False,
  )

  return df