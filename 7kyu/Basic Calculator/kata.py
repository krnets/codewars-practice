# 7kyu - Basic Calculator

""" Write a function called calculate that takes 3 values. The first and third values are numbers. 
The second value is a character. If the character is "+" , "-", "*", or "/", the function will return 
the result of the corresponding mathematical function on the two numbers. 
If the string is not one of the specified characters, the function should return null.

calculate(2,"+", 4); //Should return 6
calculate(6,"-", 1.5); //Should return 4.5
calculate(-4,"*", 8); //Should return -32
calculate(49,"/", -7); //Should return -7
calculate(8,"m", 2); //Should return null
calculate(4,"/",0) //should return null

Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made, return null. """


# def calculate(num1, operation, num2):
#     try:
#         return eval(str(num1)+operation+str(num2))
#     except:
#         return None

# def calculate(num1, operation, num2):
#     ops = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
#            '*': (lambda x, y: x * y), '/': (lambda x, y: x / y)}
#     try:
#         return ops[operation](num1, num2)
#     except:
#         return None

def calculate(num1, operation, num2):
    match operation:
        case '+': return num1+num2
        case '-': return num1-num2
        case '*': return num1*num2
        case '/': return num1/num2 if num2 != 0 else None
        case _: return None


q = calculate(3.2, "+", 8)  # 3 11.2, "3.2 + 8 = 11.2"
q
q = calculate(3.2, "-", 8)  # -4.8, "3.2 - 8 = -4.8"
q
q = calculate(3.2, "/", 8)  # 0.4, "3.2 / 8 = .4"
q
q = calculate(3.2, "*", 8)  # 25.6, "3.2 * 8 = 25.6"
q
q = calculate(-3, "+", 0)  # -3, "-3 + 0 = -3"
q
q = calculate(-3, "-", 0)  # -3, "-3 - 0 = -3"
q
q = calculate(-2, "/", -2)  # 1, "-2 / -2 = 1"
q
q = calculate(-3, "*", 0)  # 0, "-3 * 0 = 0"
q
q = calculate(-3, "/", 0)  # None, "-3 / 0 = None"
q
q = calculate(-3, "w", 0)  # None, "-3 w 0 = None"
q
q = calculate(-3, "w", 1)  # None, "-3 w 1 = None"
q
