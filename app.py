from src.view import view_GCDC
from src.notification import send_email

body = ""
for i, view in enumerate(view_GCDC()):
    viewType = ['ゴールデンクロス_5日＆25日', 'ゴールデンクロス_25日＆75日', 'デッドクロス_5日＆25日', 'デッドクロス_25日＆75日']
    print(f'---------{viewType[i]}---------')
    print(view.to_string())
    # メール本文に追加
    body += f'---------{viewType[i]}---------\n'
    body += view.to_string()
    body += '\n\n'

# メール送信
send_email(
    "【株価分析】本日のクロス判定",
    body
)



