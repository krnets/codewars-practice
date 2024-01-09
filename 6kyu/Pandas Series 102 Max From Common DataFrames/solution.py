import pandas as pd

def max_common(df_a, df_b):
    return pd.concat([df_a, df_b]).filter(df_a.columns).groupby(level=0).max()
