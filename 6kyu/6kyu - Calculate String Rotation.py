# 6kyu - Calculate String Rotation

"""  Write a function that receives two strings and returns n, where n is equal to the number of characters 
we should shift the first string forward to match the second.

For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 
5 characters forward to produce the second string, so 5 would be returned.
If the second string isn't a valid rotation of the first string, the method returns -1.

 "coffee", "eecoff" => 2 
 "eecoff", "coffee" => 4 
 "moose", "Moose" => -1 
 "isn't", "'tisn" => 2 
 "Esham", "Esham" => 0 
 "dog", "god" => -1


shiftedDiff("coffee", "eecoff") => 2
shiftedDiff("eecoff", "coffee") => 4
shiftedDiff("moose", "Moose") => nil
shiftedDiff("isn't", "'tisn") => 2
shiftedDiff("Esham", "Esham") => 0
shiftedDiff("dog", "god") => nil """


# def shifted_diff(first, second):
#     for i in range(len(first)):
#         if second == first[-i:] + first[:-i]:
#             return i
#     return -1

# def shifted_diff(first, second):
#     return max(i if second == first[-i:] + first[:-i] else -1 for i in range(len(first)))

def shifted_diff(first, second):
    return (second + second).find(first) if len(first) == len(second) else -1


q = shifted_diff("eecoff", "coffee")  # 4
q
q = shifted_diff("Moose", "moose")  # -1
q
q = shifted_diff("isn't", "'tisn")  # 2
q
q = shifted_diff("Esham", "Esham")  # 0
q
q = shifted_diff(" ", " ")  # 0
q
q = shifted_diff("hoop", "pooh")  # -1
q
q = shifted_diff("  ", " ")  # -1
q
