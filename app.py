from src.fetch_data import fetch_stock_data

df = fetch_stock_data("7203.T")

print(df.tail())