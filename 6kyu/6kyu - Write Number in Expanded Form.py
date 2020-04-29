# 6kyu - Write Number in Expanded Form

""" You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0. """


# def expanded_form(num):
#     p10s = [int(x) * pow(10, i) for (i, x) in enumerate(str(num)[::-1])]
#     return ' + '.join([str(x) for x in p10s if x][::-1])

# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num)-i-1) for i, x in enumerate(num) if int(x))

def expanded_form(num):
    return ' + '.join(x+'0'*(len(str(num))-i-1) for i, x in enumerate(str(num)) if int(x))


q = expanded_form(12), '10 + 2'
q
q = expanded_form(42), '40 + 2'
q
q = expanded_form(70304), '70000 + 300 + 4'
q
