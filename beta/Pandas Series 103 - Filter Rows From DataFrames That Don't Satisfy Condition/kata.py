import pandas as pd


# def filter_dataframe(dataframe: pd.DataFrame, col, func):
#     return dataframe[~dataframe[col].apply(func)]


# def filter_dataframe(dataframe: pd.DataFrame, col, func):
#     mask = dataframe[col].apply(func)
#     return dataframe[~mask]


def filter_dataframe(dataframe, col, func):
    return dataframe[~func(dataframe[col])]
