import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from dotenv import load_dotenv


# .envを読み込む
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def send_email(subject:str,body:str) -> None:
    """
    Gmailを使ってメールを送信する

    Args:
        subject (str): メール件名
        body (str): メール本文
    """
    # メール本文を作成
    message = MIMEText(body,"plain","utf-8")

    # メール件名を設定
    message["Subject"] = Header(subject,"utf-8")

    # 送信元・送信先を設定
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    # GmailのSMTPサーバーへ接続
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(SENDER_EMAIL,SENDER_PASSWORD)

        # メール送信
        server.send_message(message)





