# 7kyu - Convert Hash To An Array

""" Convert a hash into an array. Nothing more, Nothing less.

{name: 'Jeremy', age: 24, role: 'Software Engineer'}

should be converted into

[["name", "Jeremy"], ["age", 24], ["role", "Software Engineer"]]

Note: The output array should be sorted alphabetically. """


# def convert_hash_to_array(hash):
#     return sorted([key, value] for key, value in hash.items())

# def convert_hash_to_array(hash):
#     return [[key, value] for key, value in sorted(hash.items())]

def convert_hash_to_array(hash):
    return sorted(map(list, hash.items()))


q = convert_hash_to_array({"name": "Jeremy"}), [["name", "Jeremy"]]
q
q = convert_hash_to_array({"name": "Jeremy", "age": 24}), [
    ["age", 24], ["name", "Jeremy"]]
q
q = convert_hash_to_array({"name": "Jeremy", "age": 24, "role": "Software Engineer"}), [
    ["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
q
q = convert_hash_to_array({"product": "CodeWars", "power_level_over": 9000}), [
    ["power_level_over", 9000], ["product", "CodeWars"]]
q
q = convert_hash_to_array({}), []
q
