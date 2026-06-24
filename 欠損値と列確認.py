import pandas as pd

#これはexcel用で確認するだけのコード

file_path=r.xlsx"#パスを入れるとこ
df=pd.read_excel(file_path)#dfを作成

print('==========df.info=============================')#確認
df.info()

col_count = df.shape[1]

print(f"列数: {col_count}")

if col_count >= 20:
    print("!!!!!!!!!!!!!!!!!!!!!!!列が多いかもしれない!!!!!!!!!!!!!!!!!!!!!!!!!")

print('==========欠損値の割合======================')#10%付近超えてたら見に行く
print(f'{df.isna().mean() * 100}')

for i in df.columns:
    if df[i].dtype== object:　　　　#もっと簡単な奴があるらしいぞ.select_dtypes(include=["object", "category", "string"]).columns
        print(f'=============={i}の中身の数=================')
        print(df[i].nunique())#名前とかIDとか多くなるから確認

        if df[i].nunique()<=20:
            print(f'==========={i}の中身==========')
            print(df[i].value_counts())#20くらいだと違う表現してるだけかもしれん
