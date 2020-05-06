# 7kyu - Decreasing Inputs

""" This kata is all about adding numbers.

You will create a function named add. It will return the sum of all the arguments. Sounds easy, doesn't it?

Well Here's the Twist. The inputs will gradually decrease with their index as parameter to the function.

  add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7

Remember the function will return 0 if no arguments are passed and it must round the result if sum is a float.

  add() #=> 0
  add(1,2,3) #=> 3
  add(1,4,-6,20) #=> 6 """


# def add(*args):
#     return round(sum(x / (i+1) for i, x in enumerate(args)))

def add(*args):
    return round(sum(x / i for i, x in enumerate(args, 1)))


q = add(100, 200, 300), 300
q
q = add(2), 2
q
q = add(4, -3, -2), 2
q
