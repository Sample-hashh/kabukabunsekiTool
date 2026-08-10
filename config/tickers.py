import pandas as pd

def get_nikkei_tickers() -> None:
# CSV読み込み（タブ区切りの場合）
    df = pd.read_csv(
    r"data\nikkei225.csv",
    encoding="cp932",
    sep=","
)

# yfinance用ティッカー作成
    NIKEI = {f"{code}.T": name for code, name in zip(df["コード"], df["銘柄名"])
    }
    return NIKEI  

#テスト用
def test_get_nikkei_tickers():
    NIKEI = ["1332.T", "1333.T", "1605.T"]
    return NIKEI



# テスト用
def test_get_nikkei_tickers() -> None:
    test_df = pd.DataFrame({
        "コード": ["7203", "8306", "6758", "9984"],
        "銘柄名": ["トヨタ自動車", "三菱UFJ", "ソニーグループ", "ソフトバンクグループ"]
    })

    test_NIKEI = {
        f"{code}.T": name
        for code, name in zip(test_df["コード"], test_df["銘柄名"])
    }

    return test_NIKEI