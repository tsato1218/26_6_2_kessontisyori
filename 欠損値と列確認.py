import pandas as pd

#これは確認するだけのコード

file_path=r".csv"#パスを入れるとこ
df=pd.read_csv(file_path)#dfを作成

print('==========df.info=============================')#確認
df.info()
col_count = df.shape[1]

if col_count >= 20:
    print("!!!!!!!!!!!!!!!!!!!!!!!列が多いかもしれない!!!!!!!!!!!!!!!!!!!!!!!!!")

print('==========欠損値の割合======================')#10%付近超えてたら見に行く
missing_rate = df.isna().mean() * 100
print(missing_rate[missing_rate >= 10].sort_values(ascending=False))

for i in df.columns:
    if df[i].dtype== object:#もっと簡単な奴があるらしいぞ.select_dtypes(include=["object", "category", "string"]).columns
        print(f'=============={i}の中身の数=================')
        print(df[i].nunique())#名前とかIDとか多くなるから確認

        if df[i].nunique()<=20:
            print(f'==========={i}の中身==========')
            print(df[i].value_counts())#20くらいだと違う表現してるだけかもしれん
