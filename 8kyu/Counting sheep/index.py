# 8kyu - Counting sheep...

""" Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present). """

array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]


# def count_sheeps(sheep):
#     count = 0
#     for x in sheep:
#         if x:
#             count += 1
#     return count

# def count_sheeps(sheep):
#     return sheep.count(True)

# def count_sheeps(sheep):
#     return [x for x in sheep if x].count(True)

def count_sheeps(sheep):
    return len([x for x in sheep if x])


# 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))
q = count_sheeps(array1)
q
