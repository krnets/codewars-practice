# 8kyu - Filter out the geese

""" Write a function goose_filter  that takes an array of strings as an argument and returns a filtered array 
containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:

["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

The elements in the returned array should be in the same order as in the initial array passed to your function, 
albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, 
and some elements may be repeated. """

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


# def goose_filter(birds):
#     res = []
#     for x in birds:
#         if x not in geese:
#             res.append(x)
#     return res

# def goose_filter(birds):
#     return [b for b in birds if b not in geese]

def goose_filter(birds):
    return list(filter(lambda b: b not in geese, birds))

q = goose_filter(["Mallard", "Hook Bill", "African",
                  "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
q
q = goose_filter(["Mallard", "Barbary", "Hook Bill",
                  "Blue Swedish", "Crested"])
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
q
q = goose_filter(["African", "Roman Tufted", "Toulouse",
                  "Pilgrim", "Steinbacher"])  # []
q
