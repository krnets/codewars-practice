# 8kyu - You only need one - Beginner

""" You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not. """


# def check(seq, elem):
#     return seq.__contains__(elem)

def check(seq, elem):
    return elem in seq

# from operator import contains as check


q = check([66, 101], 66)  # True
q
q = check([78, 117, 110, 99, 104, 117, 107, 115], 8)  # False
q
q = check([101, 45, 75, 105, 99, 107], 107)  # True
q
q = check([80, 117, 115, 104, 45, 85, 112, 115], 45)  # True
q
q = check(['t', 'e', 's', 't'], 'e')  # True
q
q = check(["what", "a", "great", "kata"], "kat")  # False
q
q = check([66, "codewars", 11, "alex loves pushups"],
          "alex loves pushups")  # True
q
q = check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come")  # False
q
q = check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")  # True
q
q = check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)  # False
q
q = check(["anyone", "want", "to", "hire", "me?"], "me?")  # True
q
