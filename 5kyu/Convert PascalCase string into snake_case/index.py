""" 5kyu - Convert PascalCase string into snake_case

Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. 
Lowercase characters can be numbers. If method gets number, it should return string.

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1) """

import re

# def to_underscore(string):
#     return '_'.join(re.findall(r'([A-Z][a-z]+\d?)', string)).lower() if isinstance(string, str) else str(string)

# def to_underscore(string):
#     return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()

def to_underscore(string):
    return re.sub('(?<=.)(?=[A-Z])', '_', str(string)).lower()


q = to_underscore('TestController'), 'test_controller'
q
q = to_underscore(5), '5'
q
q = to_underscore('JustATest'), 'just_a_test'
q
