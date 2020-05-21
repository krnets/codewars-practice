# 7kyu - SillyCASE

""" Create a function that takes a string and returns that string with the first half lowercased and the last half uppercased.

eg: foobar == fooBAR

If it is an odd number then 'round' it up to find which letters to uppercase. See example below.

sillycase("brian")  
//         --^-- midpoint  
//         bri    first half (lower-cased)  
//            AN second half (upper-cased)   """

# from math import ceil

# def sillycase(silly):
#     half = ceil(len(silly) / 2)
#     return silly[:half].lower() + silly[half:].upper()


def sillycase(silly):
    half = (len(silly) + 1) // 2
    return silly[:half].lower() + silly[half:].upper()


q = sillycase('foobar')  # "fooBAR"
q
q = sillycase('codewars')  # "codeWARS"
q
q = sillycase('brian')  # 'briAN'
q
