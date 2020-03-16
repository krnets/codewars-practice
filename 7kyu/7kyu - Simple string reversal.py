# 7kyu - Simple string reversal

""" In this Kata, we are going to reverse a string while maintaining spaces.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"

More examples in the test cases. All input will be lower case letters and in some cases spaces. """

# def solve(s):
#     spc = [x[0] for x in enumerate(s) if not x[1].isalpha()]
#     rev = list(''.join([x[::-1] for x in s.split()][::-1]))[::-1]
#     out = ''
#     for i in range(len(s)):
#         if i in spc:
#             out += ' '
#         else:
#             out += rev.pop()
#     return out

# def solve(s):
#     out = []
#     rev = list(filter(str.isalpha, s))
#     spc = [x[0] for x in enumerate(s) if not x[1].isalpha()]
#     [out.append(' ') if i in spc else out.append(rev.pop()) for i in range(len(s))]
#     return ''.join(out)

def solve(s):
    it = reversed(s.replace(' ', ''))
    return ''.join(c if c == ' ' else next(it) for c in s)

# def solve(s):
#     rev = list(s.replace(' ', '')[::-1])
#     for i in [i for i, item in enumerate(s) if item == ' ']:
#         rev.insert(i, ' ')
#     return ''.join(rev)

# def solve(s):
#     rev = list(filter(str.isalpha, s))[::-1]
#     [rev.insert(pos, ' ') for pos in [i for i, c in enumerate(s) if c == ' ']]
#     return ''.join(rev)


q = solve("codewars")  # "srawedoc"
q
q = solve("your code")  # "edoc ruoy"
q
q = solve("your code rocks")  # "skco redo cruoy"
q
q = solve("i love codewars")  # "s rawe docevoli"
q
