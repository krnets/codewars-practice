import pandas as pd

# def rename_columns(df, names):
#     return pd.DataFrame(data=df.values, columns=names)


# def rename_columns(df: pd.DataFrame, names: str) -> pd.DataFrame:
#     return df.rename(columns=dict(zip(df.columns, names)))


# def rename_columns(df: pd.DataFrame, names: str) -> pd.DataFrame:
#     return df.set_axis(names, axis=1)


def rename_columns(df: pd.DataFrame, names: str) -> pd.DataFrame:
    return pd.DataFrame(data=df.to_numpy(), columns=names)
