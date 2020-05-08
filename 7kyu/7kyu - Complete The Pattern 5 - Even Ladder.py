# 7kyu - Complete The Pattern #5 - Even Ladder

""" Write a function pattern which creates the following pattern upto n number of rows.

    If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

    If any odd number is passed as argument then the pattern should last upto the largest even number 
    which is smaller than the passed odd number.

    If the argument is 1 then also it should return "".

pattern(8):

22
4444
666666
88888888

pattern(5):

22
4444

Note: There are no spaces in the pattern
Hint: Use \n in string to jump to next line """


# def pattern(n):
#     return '\n'.join(str(x) * x for x in range(1, n+1) if x % 2 == 0) if n > 0 else ''

def pattern(n):
    return '\n'.join(str(i) * i for i in range(2, n+1, 2))


q = pattern(2), "22"
q
q = pattern(1), ""
q
q = pattern(5), "22\n4444"
q
