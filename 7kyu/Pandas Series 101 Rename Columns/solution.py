import pandas as pd

# def rename_columns(df, names):
#     return pd.DataFrame(data=df.values, columns=names)

def rename_columns(df, names):
    return df.rename(columns=dict(zip(df.columns, names)))

