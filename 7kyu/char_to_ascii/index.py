""" 7kyu - char_to_ascii

Take a string and return a hash with all the ascii values of the characters in the string. 
Returns nil if the string is empty. The key is the character, and the value is the ascii value of the character. 
Repeated characters are to be ignored and non-alphebetic characters as well. """


def char_to_ascii(string):
    return {x: ord(x) for x in string if x.isalpha()} if string else None


q = char_to_ascii(""), None
q
q = char_to_ascii("a"), {"a": 97}
q
q = char_to_ascii("aaa"), {"a": 97}
q
