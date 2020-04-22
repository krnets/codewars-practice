# 7kyu - Thinkful - Logic Drills: Graceful addition

""" You like the way the Python + operator easily handles adding different numeric types, 
but you need a tool to do that kind of addition without killing your program with a 
TypeError exception whenever you accidentally try adding incompatible types like strings and lists to numbers.

You decide to write a function my_add() that takes two arguments. 
If the arguments can be added together it returns the sum. 
If adding the arguments together would raise an error the function should return None instead.

For example, my_add(1, 3.414) would return 4.414, but my_add(42, " is the answer.") would return None.

Hint: using a try / except statement may simplify this kata. """


# def my_add(a, b):
#     try: return a + b
#     except: return

# def my_add(a, b):
#     return a + b if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)) else None

def my_add(a, b):
    is_num = lambda x: isinstance(x, (int, float, complex))
    return a + b if is_num(a) and is_num(b) else None


q = my_add(1, 3.414), 4.414
q
q = my_add(42, " is the answer."), None
q
q = my_add(10, "2"), None
q
