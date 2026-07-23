from src.fetch_data import fetch_stock_data
from src.indicators import add_moving_average

df = fetch_stock_data("7203.T")

df = add_moving_average(df)

print(df.tail())
