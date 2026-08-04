import pandas as pd

# CSV読み込み（タブ区切りの場合）
df = pd.read_csv(
    r"..\data\nikkei225.csv",
    encoding="cp932",
    sep=","
)

# yfinance用ティッカー作成
NIKEI = [
    f"{code}.T"
    for code in df["コード"]
]

print(NIKEI)
