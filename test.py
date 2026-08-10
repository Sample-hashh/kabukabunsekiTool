import yfinance as yf
import pandas as pd


# テストする銘柄
TICKERS = {
    "7203.T": "トヨタ自動車",
    "8306.T": "三菱UFJフィナンシャル・グループ",
    "9432.T": "NTT",
}


def fetch_stock_data(ticker):
    """株価データ取得"""

    df = yf.download(
        ticker,
        period="1mo",   # 1か月分取得
        progress=False
    )

    return df


def main():

    for ticker, name in TICKERS.items():

        print("\n==============================")
        print(f"{name} ({ticker})")
        print("==============================")


        df = fetch_stock_data(ticker)


        # 取得確認
        if df.empty:
            print("データ取得失敗")
            continue


        print("取得成功")
        print(f"件数 : {len(df)}件")
        print()


        # 最新5件表示
        print(df.tail())


        print()
        print("カラム")
        print(df.columns)



if __name__ == "__main__":
    main()