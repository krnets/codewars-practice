# 7kyu - Case swapping

""" Given a string, swap the case for each of the letters.

e.g. CodEwArs --> cODeWaRS
Examples

""           ->   ""
"CodeWars"   ->   "cODEwARS"
"abc"        ->   "ABC"
"ABC"        ->   "abc"
"123235"     ->   "123235" """


# def swap(string):
#     return ''.join(x.lower() if x.upper() == x else x.upper() for x in string)

# def swap(string):
#     return string.swapcase()

swap = str.swapcase

q = swap('HelloWorld')  # 'hELLOwORLD'
q
q = swap('CodeWars')  # 'cODEwARS'
q
