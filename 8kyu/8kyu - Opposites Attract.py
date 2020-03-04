# 8kyu - Opposites Attract

""" Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't. """


# def lovefunc(flower1, flower2):
#     return True if ((flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)) else False

def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2

# def lovefunc(flower1, flower2):
#     return (flower1 - flower2) % 2

# def lovefunc(flower1, flower2):
#     return (flower1 ^ flower2) % 2


q = lovefunc(1, 4)  # True
q
q = lovefunc(2, 2)  # False
q
q = lovefunc(0, 1)  # True
q
q = lovefunc(0, 0)  # False
q
