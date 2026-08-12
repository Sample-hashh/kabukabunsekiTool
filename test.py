from src.notification import send_email

send_email(
    "テストメール",
    "株価分析アプリからのテストメールです。"
)

print("メール送信完了")