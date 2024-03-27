# def testit(n: int):
#   return f"{n:b}".count("1")


def testit(n: int):
    return n.bit_count()
