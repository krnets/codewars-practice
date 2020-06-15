""" Beta - Sort by number

The company Evaluators evaluates products' quality in chunks of 9 products. 
The row of a product in a chunk is expressed by a single lowercase letter from [a-i] 
and the final evaluation is hierarchical and expressed by an integer in range [1-9]. 
The final output of the evaluation process is a string consisting of 9 succesive structures 
of <product + evaluation>. The issue occuring there was that nor products were evaluated 
by the order they inserted the chunk neither the evaluation has a related order. 
The challenge here is to modify the provided string such as your output to be a sorted string 
by the evaluation of the products.

example 1

    s = 'a3h9c4i1d2e7f8g6b5' # input
    sortByNum(s)
    'i1d2a3c4b5g6e7f8h9' # output

example 2

    s = 'b9i5a8f3d7h4e6c2g1' # input
    sortByNum(s)
    'g1c2f3h4i5e6d7a8b9' # output

Every input will always contain 9 structures. 
Products will always be letters from a to i and all evaluations will always integers from 1 to 9. 
All bounds inclusive. """

# def sort_by_num(s):
#     chunks = [s[i:i+2] for i in range(0, len(s), 2)]
#     return ''.join(sorted(chunks, key=lambda x: x[-1]))

import re

def sort_by_num(s):
    return ''.join(sorted(re.findall('..', s), key=min))


q = sort_by_num('b9i5a8f3d7h4e6c2g1'), 'g1c2f3h4i5e6d7a8b9'
q
q = sort_by_num('a3h9c4i1d2e7f8g6b5'), 'i1d2a3c4b5g6e7f8h9'
q
