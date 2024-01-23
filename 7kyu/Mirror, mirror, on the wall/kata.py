def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]