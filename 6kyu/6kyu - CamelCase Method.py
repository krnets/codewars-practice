# 6kyu - CamelCase Method

""" Write simple camel_case function for strings. 
All words must have their first letter capitalized without spaces.

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord """


# def camel_case(string):
#     return ''.join(x.title() for x in string.split())

def camel_case(string):
    return string.title().replace(' ', '')


q = camel_case("test case"), "TestCase"
q
q = camel_case("camel case method"), "CamelCaseMethod"
q
q = camel_case("say hello "), "SayHello"
q
q = camel_case(" camel case word"), "CamelCaseWord"
q
q = camel_case(""), ""
q
