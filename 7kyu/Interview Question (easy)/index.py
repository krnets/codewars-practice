""" 7kyu - GOOGLE Interview Question (EASY)

INTRODUCTION:

If I give you a name of a city as a string, I want you to return a string 
that shows how many times each letter shows up in the string by using an asterisk *

SEE TEST CASE!

As you can see for Chicago, in the return string, I only show the letter "c" once 
even though there are 2 "c" in Chicago (regardless of upper or lowercase).

I show 2 asteriks since there are 2 "c" in Chicago.

In the return string there are no spaces between the letters, asteriks, and commas.

"Chicago"  =>  "c:**,h:*,i:*,a:*,g:*,o:*"

Note that the return string contains the characters in order of first appearence in the original string. """

from collections import Counter

def get_strings(city):
    return ','.join(f'{ch}:{"*" * count}' for ch, count in Counter(city.lower().replace(' ', '')).items())


q = get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*"
q
q = get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*"
q
q = get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*"
q
