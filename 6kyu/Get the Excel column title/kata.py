from string import ascii_uppercase

def get_column_title(num):
    assert isinstance(num, int) and num > 0
    excel_col = ""
    while num:
        num, r = divmod(num - 1, 26)
        excel_col = ascii_uppercase[r] + excel_col
    return excel_col
