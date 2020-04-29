# 6kyu - Write Number in Expanded Form - Part 2

""" You will be given a number and you will need to return it as a string in Expanded Form. """

# def expanded_form(num):
#     integer, decimal = str(num).split('.')
#     decimal = ' + '.join(x+'/1'+'0'*(i+1) for i, x in enumerate(str(decimal)) if int(x))
#     if int(integer):
#         if int(integer) > 9:
#             integer = ' + '.join(x+'0'*(len(str(integer))-i-1) for i, x in enumerate(str(integer)) if int(x))
#             return ' + '.join([integer, decimal])
#         return ' + '.join([integer, decimal])
#     else:
#         return decimal

# def expanded_form(num):
#     parts = str(num).split('.')
#     integer = filter(bool, [int(x) * 10**i for i, x in enumerate(parts[0][::-1])][::-1])
#     decimal = [x+'/' + str(10**(i+1)) for i, x in enumerate(parts[1]) if int(x)]
#     return ' + '.join(list(map(str, integer)) + decimal)


def expanded_form(num):
    parts = str(num).split('.')
    integer = [x + '0' * i for i, x in enumerate(parts[0][::-1]) if int(x)][::-1]
    decimal = [x + '/' + str(10**(i+1)) for i, x in enumerate(parts[1]) if int(x)]
    return ' + '.join(integer + decimal)


q = expanded_form(1.24)  # '1 + 2/10 + 4/100'
q
q = expanded_form(7.304)  # '7 + 3/10 + 4/1000'
q
q = expanded_form(0.04)  # '4/100'
q
q = expanded_form(7909.304)  # '7 + 3/10 + 4/1000'
q
