# 7kyu - Greatest Difference

""" Your task is to find the number couple with the greatest difference from a given array of number-couples.

All number couples will be given as strings and all numbers in them will be positive integers.

For instance: ['56-23','1-100']; in this case, you should identify '1-100' as the number couple with 
the greatest difference and return it.

In case there are more than one option, for instance ['1-3','5-7','2-3'], you should identify 
whichever is first, so in this case '1-3'.

If there is no difference, like so ['11-11', '344-344'], return false. """

# def diff(arr):
#     ints = [list(map(int, x.split('-'))) for x in arr]
#     dist = [max(x) - min(x) for x in ints]
#     return False if sum(dist) == 0 else arr[dist.index(max(dist))] if arr else False


# def diff(arr):
#     ints = [list(map(int, x.split('-'))) for x in arr]
#     dist = [max(x) - min(x) for x in ints]
#     return arr[dist.index(max(dist))] if arr and sum(dist) else False

def diff(arr):
    couple = arr and max(arr, key=lambda x: abs(eval(x)))
    return bool(arr and eval(couple)) and couple


q = diff(['43-45', '1021-55', '000-18888', '92-34',
          '76-32', '99-1', '1020-54'])  # '000-18888'
q
q = diff(['1-2', '2-4', '5-7', '8-9', '44-45'])  # '2-4'
q
q = diff(['1-1000', '2-1000', '100-67', '98-45', '8-9'])  # '1-1000'
q
q = diff(['33-33', '77-77'])  # False
q
q = diff(['23-67', '67-23', '88-88', '45-46'])  # '23-67'
q
q = diff(['45896-2354', '4654-556767', '2455-423522',
          '3455-355', '34-34', '2524522-0'])  # '2524522-0'
q
q = diff(['1-1', '2-2', '1-0', '77-77'])  # '1-0'
q
q = diff(['0-0'])  # False
q
q = diff([])  # False
q
