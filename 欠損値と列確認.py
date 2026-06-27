import pandas as pd

file_path = r"C:\Users\81805\Documents\train.csv"
df = pd.read_csv(file_path)

def NA_rate(dataframe):
    print('========== dataframe.info =============================')
    dataframe.info()

    print('\n========== 行数・列数 =============================')
    print(dataframe.shape)

    col_count = dataframe.shape[1]

    if col_count >= 20:
        print(f"警告: 列数が{col_count}列あります。列が多い")
    
    print('\n========== 欠損値の割合 10%以上 ======================')
    missing_rate = dataframe.isna().mean() * 100
    print(missing_rate[missing_rate >= 10].sort_values(ascending=False))

    print('\n========== カテゴリ列の確認 ======================')
    cat_cols = dataframe.select_dtypes(include=["object", "category", "string"]).columns
    
    for col in cat_cols:
        unique_count = dataframe[col].nunique(dropna=False)

        print(f'\n============== {col} の確認 =================')
        print(f'種類数: {unique_count}')
    
        if unique_count <= 20:
            print(f'=========== {col} の中身 ===========')
            print(dataframe[col].value_counts(dropna=False))

NA_rate(df)
