""" 7kyu - Asterisk it

You are given a function that should insert an asterisk (*) between every pair of even digits in the given input,
and return it as a string. If the input is a sequence, concat the elements first as a string.

Input: The input can be an integer, a string of digits or a sequence containing integers only.
Output: Return a string.

5312708     -->  "531270*8"
"0000"      -->  "0*0*0*0"
[1, 4, 64]  -->  "14*6*4" """


import re

# def asterisc_it(n):
#     s = ''.join(map(str, n)) if isinstance(n, list) else str(n)
#     res = []
#     for i in range(len(s)-1):
#         if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
#             res.append(s[i])
#             res.append('*')
#         else:
#             res.append(s[i])
#     res.append(s[-1])
#     return ''.join(res)

# def asterisc_it(n):
#     s = ''.join(map(str, n)) if isinstance(n, list) else str(n)
#     return re.sub(r'(?<=[02468])(?=[02468])', r'*', s)

def asterisc_it(n):
    s = ''.join(map(str, n)) if isinstance(n, list) else str(n)
    return re.sub(r'([02468])(?=[02468])', r'\1*', s)

q = asterisc_it(5312708), '531270*8'
q
q = asterisc_it(9682135), '96*8*2135'
q
q = asterisc_it(2222), '2*2*2*2'
q
q = asterisc_it(1111), '1111'
q
q = asterisc_it(9999), '9999'
q
q = asterisc_it('0000'), '0*0*0*0'
q
q = asterisc_it(8), '8'
q
q = asterisc_it(2), '2'
q
q = asterisc_it(0), '0'
q
q = asterisc_it([1, 4, 64, 68, 67, 23, 1]), '14*6*4*6*8*67231'
q
