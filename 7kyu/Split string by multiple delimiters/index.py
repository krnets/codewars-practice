# 7kyu - Split string by multiple delimiters

""" Your task is to write function which takes string and list of delimiters as an input 
and returns list of strings/characters after splitting given string.

multiple_split('Hi, how are you?', [' ']) => ['Hi,', 'how', 'are', 'you?']
multiple_split('1+2-3', ['+', '-']) => ['1', '2', '3']

List of delimiters is optional and can be empty, so take that into account.

Important note: Result cannot contain empty string. """


def multiple_split(string, delimiters=[]):
    for d in delimiters:
        string = string.replace(d, '|')
    return [x for x in string.split('|') if x]


q = multiple_split('Hi everybody!', [' ', '!'])  
q
#      ['Hi', 'everybody']
q = multiple_split('(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*'])
q
#      ['1', '2', '6', '3', '9']
q = multiple_split('Solve_this|kata-very\quickly!', ['!', '|', '\\', '_', '-'])
q
#      ['Solve', 'this', 'kata', 'very', 'quickly']
