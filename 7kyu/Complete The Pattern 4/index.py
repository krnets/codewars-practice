# 7kyu - Complete The Pattern #4

""" You have to write a function pattern which creates the following pattern upto n number of rows. 
If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

pattern(4):

1234
234
34
4

pattern(6):

123456
23456
3456
456
56
6

Note: There are no blank spaces
Hint: Use \n in string to jump to next line """

# def pattern(n):
#     result = []
#     for i in range(1, n+1):
#         block = []
#         for j in range(i, n+1):
#             block.append(j)
#         result.append(''.join(map(str, block)))
#     return '\n'.join(result)


def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(i, n+1)) for i in range(1, n+1))


q = pattern(1), "1"
q
q = pattern(2), "12\n2"
q
q = pattern(5), "12345\n2345\n345\n45\n5"
q
