# Beta - Sum of array's elements

""" You will be given an array of integers. 
You will need to return an integer that is the sum of the elements multiplied by an incrementing constant. 
The first element in the array is multiplied by 1, the second element multiplied by 2, etc:

a, b, c, d, ... => 1*a + 2*b + 3*c + 4*d + ...

Examples

8, 5, 4        =>  30    # 1*8 + 2*5 + 3*4 = 30
4, 9           =>  22    # 1*4 + 2*9 = 22
5, 4, 3, 2, 1  =>  55    # 1*5 + 2*4 + 3*3 + 4*2 + 5*1 = 55 """


def sum1(array):
    return sum(i * x for (i, x) in enumerate(array, 1))


q = sum1([8, 5, 4])  # 30
q
q = sum1([4, 9])  # 22
q
q = sum1([1, 2, 3, 4, 5])  # 55
q
