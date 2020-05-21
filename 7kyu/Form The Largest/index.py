# 7kyu - Form The Largest

""" Given a number, Return _The Maximum number _ could be formed from the digits of the number given.

    Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive !alt !alt
    Digit Duplications could occur , So also consider it when forming the Largest

maxNumber (213) ==> return (321)
Explanation:
As 321 is _The Maximum number _ could be formed from the digits of the number *213*** .

maxNumber (7389) ==> return (9873)
Explanation:
As 9873 is _The Maximum number _ could be formed from the digits of the number *7389*** .

maxNumber (63729) ==> return (97632)
Explanation:
As 97632 is _The Maximum number _ could be formed from the digits of the number *63729*** .

maxNumber (566797) ==> return (977665)
Explanation:
As 977665 is _The Maximum number _ could be formed from the digits of the number *566797*** .

Note : Digit duplications are considered when forming the largest .

maxNumber (17693284) ==> return (98764321)
Explanation:
As 98764321 is _The Maximum number _ could be formed from the digits of the number *17693284*** . """


# def max_number(n):
#     return int(''.join(sorted(str(n))[::-1]))

def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))


q = max_number(213), 321
q
q = max_number(7389), 9873
q
q = max_number(63792), 97632
q
q = max_number(566797), 977665
q
q = max_number(1000000), 1000000
q
