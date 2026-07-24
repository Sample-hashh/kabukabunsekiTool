from src.fetch_data import fetch_stock_data
from src.indicators import add_moving_average
from src.signals import detect_golden_cross

df = fetch_stock_data("7203.T")

df = add_moving_average(df)

df = detect_golden_cross(df)

print(df[["Close","MA25","GC"]].tail(20))
