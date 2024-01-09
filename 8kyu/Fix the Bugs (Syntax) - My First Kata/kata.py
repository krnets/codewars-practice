# def my_first_kata(a, b):
#     if type(a) is int and type(b) is int:
#         return a % b + b % a
#     else:
#         return False

def my_first_kata(a, b):
    try:
        return a % b + b % a
    except:
        return False
