HOLES = [1, 0, 0, 0, 0, 0, 1, 0, 2, 1]

def get_num(n):
    return 0 if n == 0 else HOLES[n % 10] + get_num(n // 10)
