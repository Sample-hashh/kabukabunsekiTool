from src.view import view_GCDC


for i, view in enumerate(view_GCDC()):
    viewType = ['ゴールデンクロス_5日＆25日', 'ゴールデンクロス_25日＆75日', 'デッドクロス_5日＆25日', 'デッドクロス_25日＆75日']
    print(f'---------{viewType[i]}---------')
    print(view.to_string())




