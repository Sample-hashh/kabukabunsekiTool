from src.fetch_data import fetch_stock_data
from src.indicators import (add_moving_average,add_rsi,add_macd,add_volume_analysis)
from src.signals import detect_golden_cross
from src.signals import detect_dead_cross

df = fetch_stock_data("7203.T")

df = add_moving_average(df)
df = add_rsi(df)
df= add_macd(df)


df = detect_golden_cross(df)
df = detect_dead_cross(df)


#print(df.tail(20))
print(
    df[
        [
            "Volume",
            "Volume_MA20",
            "Volume_Ratio",
        ]
    ].tail(20)
)
