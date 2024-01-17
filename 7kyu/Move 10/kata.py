from string import ascii_lowercase as abc


def move_ten(st):
    return st.translate(str.maketrans(abc, abc[10:] + abc[:10]))
