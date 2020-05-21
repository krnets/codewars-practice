# 7kyu - No ifs no buts

""" Write a function that accepts two parameters (a and b) and says whether a is smaller, bigger, or equal to b.

Here is an example code:

var noIfsNoButs = function (a,b) {
  if(a > b) return a + " is greater than " + b
  else if(a < b) return a + " is smaller than " + b
  else if(a == b) return a + " is equal to " + b
}

There's only one problem...
You can't use if statements, and you can't use shorthands like (a < b)?true:false;
in fact the word "if" and the character "?" are not allowed in the code.
Inputs are guarenteed to be numbers """


def no_ifs_no_buts(a, b):
    cmp = {
        -1:  " is smaller than ",
        0: " is equal to ",
        1: " is greater than "
    }
    return str(a) + cmp[(a > b) - (a < b)] + str(b)


q = no_ifs_no_buts(45, 51)  # "45 is smaller than 51"
q
q = no_ifs_no_buts(1, 2)  # "1 is smaller than 2"
q
q = no_ifs_no_buts(-3, 2)  # "-3 is smaller than 2"
q
q = no_ifs_no_buts(1, 1)  # "1 is equal to 1"
q
q = no_ifs_no_buts(100, 100)  # "100 is equal to 100"
q
q = no_ifs_no_buts(100, 80)  # "100 is greater than 80"
q
q = no_ifs_no_buts(20, 19)  # "20 is greater than 19"
q
