# 7kyu - Sort the Gift Code

""" Santa's senior gift organizer Elf developed a way to represent up to 26 gifts by assigning 
a unique alphabetical character to each gift. After each gift was assigned a character, 
the gift organizer Elf then joined the characters to form the gift ordering code.

Santa asked his organizer to order the characters in alphabetical order, but the Elf 
fell asleep from consuming too much hot chocolate and candy canes! Can you help him out?

Write a function called sort_gift_code that accepts a string containing up to 26 
unique alphabetical characters, and returns a string containing the same characters in alphabetical order. """


def sort_gift_code(code):
    return ''.join(sorted(code))


q = sort_gift_code('abcdef')  # 'abcdef'
q
q = sort_gift_code('pqksuvy')  # 'kpqsuvy'
q
# 'abcdefghijklmnopqrstuvwxyz'
q = sort_gift_code('zyxwvutsrqponmlkjihgfedcba')
q
