# 8kyu - Short Long Short

""" Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string 
on the outside and the longer string on the inside. The strings will not be the same length, 
but they may be empty ( length 0 ).

solution("1", "22") # returns "1221"
solution("22", "1") # returns "1221" """


# def solution(a, b):
#     if len(a) < len(b):
#         return a + b + a
#     else:
#         return b + a + b

# def solution(a, b):
#     return a+b+a if len(a) < len(b) else b+a+b

def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short


q = solution('45', '1'), '1451'
q
q = solution('13', '200'), '1320013'
q
q = solution('Soon', 'Me'), 'MeSoonMe'
q
q = solution('U', 'False'), 'UFalseU'
q
