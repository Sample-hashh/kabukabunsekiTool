from src.view import view_GCDC

# GC・DCを表示させる
print(view_GCDC())
for gcdc in view_GCDC():
    print(gcdc.to_string())


