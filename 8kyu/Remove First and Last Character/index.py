# 8kyu - Remove First and Last Character

""" It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry with strings with less than two characters. """


# def remove_char(s):
#     res = []
#     for i in range(1, len(s) - 1):
#         res.append(s[i])
#     return ''.join(res)

def remove_char(s):
    return s[1:-1]


q = remove_char('eloquent')  # 'loquen'
q
q = remove_char('country')  # 'ountr'
q
q = remove_char('person')  # 'erso'
q
q = remove_char('place')  # 'lac'
q
q = remove_char('ok')  # ''
q
