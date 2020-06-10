""" 7kyu - Dropcaps

DropCaps means that the first letter of the starting word of the paragraph should be in caps 
and the remaining lowercase, just like you see in the newspaper.

But for a change, let's do that for each and every word of the given String. 
Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.

*should work also on Leading and Trailing Spaces and caps.

drop_cap('apple') => "Apple"
drop_cap('apple of banana'); => "Apple of Banana"
drop_cap('one   space'); => "One   Space" 
drop_cap('   space WALK   '); => "   Space Walk   " 

Note: you will be provided atleast one word and should take string as input and return string as output. """

import re

# def drop_cap(st):
#     return re.sub(r'(\w+)', lambda m: m.group(1).title() if len(m.group(1)) > 2 else m.group(1), st)

# def drop_cap(st):
#     return re.sub(r'(\w{3,})', lambda m: m.group(1).title(), st)

def drop_cap(st):
    return re.sub(r'\w{3,}', lambda m: m[0].title(), st)


q = drop_cap('Apple Banana'), "Apple Banana"
q
q = drop_cap('apple or banana'), "Apple or Banana"
q
q = drop_cap('Apple'), "Apple"
q
q = drop_cap(''), ""
q
