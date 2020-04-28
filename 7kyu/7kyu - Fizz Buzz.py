# 7kyu - Fizz Buzz

""" Return an array containing the numbers from 1 to N, where N is the parametered value. 
N will never be less than 1

Replace certain values however if any of the following conditions are met:

    If the value is a multiple of 3: use the value 'Fizz' instead
    If the value is a multiple of 5: use the value 'Buzz' instead
    If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead """


# def fizzbuzz(n):
#     return ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, n+1)]

def fizzbuzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, n+1)]


q = fizzbuzz(10)
q
#  [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
