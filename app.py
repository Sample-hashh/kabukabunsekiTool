from src.fetch_data import fetch_stock_data
from src.indicators import add_moving_average
from src.signals import detect_golden_cross
from src.signals import detect_dead_cross
from src.indicators import add_rsi

df = fetch_stock_data("7203.T")

df = add_moving_average(df)

df = detect_golden_cross(df)
df = detect_dead_cross(df)

df = add_rsi(df)

print(df[["Close","MA25","GC","DC","RSI"]].tail(30))
