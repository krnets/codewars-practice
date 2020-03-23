# 7kyu - Parts of a list

""" Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

    Each two non empty parts will be in a pair
    Each part will be in a string
    Elements of a pair must be in the same order as in the original array.

a = ["az", "toto", "picaro", "zone", "kiwi"] -->
[["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"], ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]]

a = ["az", "toto", "picaro", "zone", "kiwi"] -->
[("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]  """


# def partlist(arr):
#     return list(zip([' '.join(arr[0:i]) for i, x in enumerate(arr)], [' '.join(arr[i:]) for i, x in enumerate(arr)]))[1:]

def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]


q = partlist(["I", "wish", "I", "hadn't", "come"])
q
#      [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")])

q = partlist(["cdIw", "tzIy", "xDu", "rThG"])
q
#      [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])

q = partlist(["vJQ", "anj", "mQDq", "sOZ"])
q
#      [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])
