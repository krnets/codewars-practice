# 7kyu - Xmas Tree

""" Create a function xMasTree(height) that returns a christmas tree of the correct height. 
The height is passed through to the function and the function should return a list containing each line of the tree.

xMasTree(5) should return : ['____#____', '___###___', '__#####__', '_#######_', '#########', '____#____', '____#____']
xMasTree(3) should return : ['__#__', '_###_', '#####', '__#__', '__#__']

The final idea is for the tree to look like this if you decide to print each element of the list:

xMasTree(5) will result in:
____#____              1
___###___              2
__#####__              3
_#######_              4
#########       -----> 5 - Height of Tree
____#____        1      
____#____        2 - Trunk/Stem of Tree

xMasTree(3) will result in:
__#__                  1
_###_                  2
#####          ----->  3 - Height of Tree
__#__           1
__#__           2 - Trunk/Stem of Tree

Pad with underscores i.e _ so each line is the same length. 
The last line forming the tree having only hashtags, no spaces. 
Also remember the trunk/stem of the tree. """


# # def xMasTree(n):
#     return [('#' * i).center(n*2-1, '_') for i in range(1, n*2, 2)] + 2 * ['#'.center(n*2-1, '_')]

from itertools import chain

def xMasTree(n):
    return [('#' * i).center(n*2-1, '_') for i in chain(range(1, n*2, 2), (1, 1))]


q = xMasTree(3)
q
#      ['__#__', '_###_', '#####', '__#__', '__#__']
q = xMasTree(7)
q
#      ['______#______', '_____###_____', '____#####____', '___#######___', '__#########__', '_###########_', '#############', '______#______', '______#______'])
q = xMasTree(2)
q
#      ['_#_', '###', '_#_', '_#_']
q = xMasTree(4)
q
#      ['___#___', '__###__', '_#####_', '#######', '___#___', '___#___'] )
q = xMasTree(6)
q
#      ['_____#_____', '____###____', '___#####___', '__#######__', '_#########_', '###########', '_____#_____', '_____#_____'])
