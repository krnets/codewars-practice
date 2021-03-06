# 7kyu - Square Every Digit

""" For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer """


# def square_digits(num):
#     return int(''.join(str(int(x) * int(x)) for x in str(num)))

def square_digits(num):
    return int(''.join((str(int(d) ** 2)) for d in str(num)))
    
# def square_digits(num):
#     return int(''.join(map(lambda x: str(int(x)**2), str(num))))


q = square_digits(9119)  # 811181
q
