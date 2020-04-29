# 7kyu - Jumping Number (Special Numbers Series #4)

""" Jumping number is the number that All adjacent digits in it differ by 1.
Given a number, Find if it is Jumping or not . """

# def jumping_number(number):
#     s = str(number)
#     return 'Not!!' if any(abs(int(s[i-1]) - int(s[i])) != 1 for i in range(1, len(s))) else 'Jumping!!'

def jumping_number(number):
    arr = list(map(int, str(number)))
    return ['Not!!', 'Jumping!!'][all(map(lambda x, y: abs(x-y) == 1, arr, arr[1:]))]

# Single Digit Number
q = jumping_number(1), "Jumping!!"
q
q = jumping_number(7), "Jumping!!"
q
q = jumping_number(9), "Jumping!!"
q

# Two Digit Number
q = jumping_number(23), "Jumping!!"
q
q = jumping_number(32), "Jumping!!"
q
q = jumping_number(79), "Not!!"
q
q = jumping_number(98), "Jumping!!"
q

# Larger Numbers
q = jumping_number(8987), "Jumping!!"
q
q = jumping_number(4343456), "Jumping!!"
q
q = jumping_number(98789876), "Jumping!!"
q
