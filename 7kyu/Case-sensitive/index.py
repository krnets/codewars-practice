""" 7kyu - Case-sensitive!

Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. 
Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], 
but case_sensitive('codeWaRs') returns [False, ['W', 'R']]. """


def case_sensitive(s):
    return [not s or s.islower(), list(filter(str.isupper, s))]


q = case_sensitive('asd'), [True, []]
q
q = case_sensitive('cellS'), [False, ['S']]
q
q = case_sensitive('z'), [True, []]
q
q = case_sensitive(''), [True, []]
q
