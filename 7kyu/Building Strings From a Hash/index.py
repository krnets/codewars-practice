# 7kyu - Building Strings From a Hash

""" Complete the solution so that it takes the object or hash passed in and generates a human readable string 
from its key/value pairs.

The format should be "KEY = VALUE". 
Each key/value pair should be separated by a comma except for the last pair.

solution({"a": 1, "b": '2'}) # should return "a = 1,b = 2" """

# def solution(pairs):
#     res = ''
#     for x in pairs:
#         res += str(x)
#         res += ' = '
#         res += str(pairs[x])
#         res += ','
#     return res[:-1]


# def solution(pairs):
#     res = ''
#     for x in sorted(pairs, key=lambda x: str(x)):
#         res += f'{str(x)} = {str(pairs[x])},'
#     return res[:-1]


# def solution(pairs):
#     return ','.join(f'{str(x)} = {str(pairs[x])}' for x in sorted(pairs, key=str))


# def solution(pairs):
#     return ','.join(sorted('{} = {}'.format(k, pairs[k]) for k in pairs))


# def solution(pairs):
#     return ','.join(sorted(f'{key} = {value}' for key, value in pairs.items()))


def solution(pairs):
    return ",".join(f"{k} = {pairs[k]}" for k in sorted(pairs.keys(), key=str))


q = solution({"a": 1, "b": 2})  # 'a = 1,b = 2'
q
q = solution({"a": "b", "b": "a"})  # 'a = b,b = a'
q
q = solution({0: "a", "b": 2})  # '0 = a,b = 2'
q
q = solution({"b": 1, "c": 2, "e": 3})  # 'b = 1,c = 2,e = 3'
q
q = solution({})  # ''
q
q = solution({"a": -3, 0: -4, 2: -3, "z": 10, "y": 8, 1: 9, "x": 8})
q
#     0 = -4,1 = 9,2 = -3,a = -3,x = 8,y = 8,z = 10
