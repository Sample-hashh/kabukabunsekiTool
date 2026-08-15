from src.notification import send_email

send_email(
    "株価分析結果",
    "株価分析アプリからのテストメールです。"
)

print("メール送信完了")