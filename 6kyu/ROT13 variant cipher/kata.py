from string import ascii_lowercase as abc


def encrypter(strng: str):
    step_one = str.maketrans(abc, abc[13:] + abc[:13])
    step_two = str.maketrans(abc, abc[::-1])
    return strng.translate(step_one).translate(step_two)
