# 6kyu - Braces status

""" Write a function that checks the braces status in a string, and return True 
if all braces are properly closed, or False otherwise. 
Available types of brackets: (), [], {}.

Please note, you need to write this function without using regex!

'([[some](){text}here]...)'  =>  True
'{([])}'                     =>  True
'()[]{}()'                   =>  True
'(...[]...{(..())}[abc]())'  =>  True
'1239(df){'                  =>  False
'[()])'                      =>  False
')12[x]34('                  =>  False """


# def braces_status(string):
#     string = ''.join(x for x in string if x in '()[]{}')
#     while '()' in string or '[]' in string or '{}' in string:
#         string = string.replace('()', '')
#         string = string.replace('[]', '')
#         string = string.replace('{}', '')
#     return not string

def braces_status(string):
    pairs = ['()', '[]', '{}']
    string = ''.join(x for x in string if x in ''.join(pairs))
    while any(b in string for b in pairs):
        for i in range(len(pairs)):
            string = string.replace(pairs[i], '')
    return not string


q = braces_status('[()]'), True
q
q = braces_status('{[]}'), True
q
q = braces_status('{[()]}'), True
q
q = braces_status('([)]'), False
q
q = braces_status('([[some](){text}here]...)'), True
q
q = braces_status('}'), False
q
q = braces_status('[()]]'), False
q
q = braces_status('[()]{('), False
q
q = braces_status('()[]{}()'), True
q
q = braces_status('[[[['), False
q
q = braces_status('1239(df)'),  False
q
q = braces_status(')12[x]34('), False
q
q = braces_status('(...[]...{(..())}[abc]())'), True
q
