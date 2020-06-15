""" 6kyu - Simple Fun #318: Sort String

Your task is to sort the characters in a string according to the following rules:

- Rule1: English alphabets are arranged from A to Z, case insensitive.
  ie. "Type" --> "epTy"
- Rule2: If the uppercase and lowercase of an English alphabet exist
  at the same time, they are arranged in the order of oringal input.
  ie. "BabA" --> "aABb"
- Rule3: non English alphabet remain in their original position.
  ie. "By?e" --> "Be?y"

[input] string s
A non empty string contains any characters(English alphabets or non English alphabets).

[output] a string
A sorted string according to the rules above.

For s = "cba", the output should be "abc".
For s = "Cba", the output should be "abC".
For s = "cCBbAa", the output should be "AaBbcC".
For s = "c b a", the output should be "a b c".
For s = "-c--b--a-", the output should be "-a--b--c-".
For s = "Codewars", the output should be "aCdeorsw". """


def sort_string(s):
    letters = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    return ''.join(next(letters) if c.isalpha() else c for c in s)


q = sort_string("a"), "a"
q
q = sort_string("cba"), "abc"
q
q = sort_string("Cba"), "abC"
q
q = sort_string("cCBbAa"), "AaBbcC"
q
q = sort_string("!"), "!"
q
q = sort_string("c b a"), "a b c"
q
q = sort_string("-c--b--a-"), "-a--b--c-"
q
q = sort_string("cbaCcC"), "abcCcC"
q
q = sort_string("Codewars"), "aCdeorsw"
q
q = sort_string(
    " MkWD{RB=//k-^ J@,xH Vfi uAz+$ kV _[ }a!}%pSBwn !kKB (b  q PQF +}wS  .kfU r wFNEs#NsR UVMdG")
q
#    " AaBB{Bb=//D-^ d@,Ef FfF GHi+$ Jk _[ }k!}%kkKkM !MnN (N  p PqQ +}Rr  .RSS s suUUV#VVW wwwxz"
