import re

# def bracket_buster(string):
#     if not isinstance(string, str):
#         return "Take a seat on the bench."
#     return [*re.findall(r"\[([\w\s'?[-]*)\]", string)]

import re

def bracket_buster(string):
    return [*re.findall(r"\[(.*?)\]", string)] if isinstance(string, str) else "Take a seat on the bench."

