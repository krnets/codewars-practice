# 8kyu - altERnaTIng cAsE <=> ALTerNAtiNG CaSe

""" Define to_alternating_case such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. 
For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

As usual, your function/method should be pure, i.e. it should not mutate the original string. """


# def to_alternating_case(string):
#     res = ''
#     for c in string:
#         if c.upper() == c:
#             res += c.lower()
#         else:
#             res += c.upper()
#     return res

# def to_alternating_case(string):
#     return ''.join([c.upper() if c.islower() else c.lower() for c in string])

def to_alternating_case(string):
    return string.swapcase()


q = to_alternating_case("hello world")  # "HELLO WORLD"
q
q = to_alternating_case("HELLO WORLD")  # "hello world"
q
q = to_alternating_case("hello WORLD")  # "HELLO world"
q
q = to_alternating_case("HeLLo WoRLD")  # "hEllO wOrld"
q
q = to_alternating_case("12345")  # "12345"
q
q = to_alternating_case("1a2b3c4d5e")  # "1A2B3C4D5E"
q
# "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
q = to_alternating_case("String.prototype.toAlternatingCase")
q
q = to_alternating_case(to_alternating_case("Hello World"))  # "Hello World"
q

title = "altERnaTIng cAsE"
q = to_alternating_case(title)
q
# "ALTerNAtiNG CaSe"
