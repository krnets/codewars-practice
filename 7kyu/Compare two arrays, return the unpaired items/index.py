""" 7kyu - noobCode 04: HOT SINGLES...compare two arrays, return the unpaired items !

Write a function that takes two arguments, and returns a new array populated with the elements that only appear once, 
in either one array or the other, taken only once; display order should follow what appears in arr1 first, then arr2:

hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5]) # [4, 5]
hot_singles(["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"]) # ["tartar", "domino"]
hot_singles([77, "ciao"], [78, 42, "ciao"]) # [77, 78, 42]
hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]) # [4,5] """


# def hot_singles(arr1, arr2):
#     disjunctive_union = [x for x in arr1 + arr2
#                          if x not in set(arr1).intersection(set(arr2))]
#     return list(dict.fromkeys(disjunctive_union))

def hot_singles(arr1, arr2):
    return sorted(set(arr1).symmetric_difference(arr2), key=(arr1+arr2).index)


q = hot_singles(["tartar", "blanket", "domino"], [
                "blanket"]), ["tartar", "domino"]
q
q = hot_singles([77, "basketweave"], [78, 42, "basketweave"]), [77, 78, 42]
q
q = hot_singles([100, 45, "ciao"], [100, 2, 3, 45, 5]), ["ciao", 2, 3, 5]
q
q = hot_singles([10, 200, 30], [10, 20, 3, 4, 5, 5, 5, 200]), [30, 20, 3, 4, 5]
q
q = hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]), [4, 5]
q
