# 7kyu - String Reordering

""" The input will be an array of dictionaries.

Return the values as a string-seperated sentence in the order of their keys' integer equivalent (increasing order).

The keys are not reoccurring and their range is -999 < key < 999. 
The dictionaries' keys & values will always be strings and will always not be empty.

Input:
List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]

Output:
'Vatsan took his dog for a spin' """


def sentence(input):
    pairs = [list(*x.items()) for x in input]
    ordered = sorted(pairs, key=lambda k: int(k[0]))
    return ' '.join(word for i, word in ordered)


List = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
]

q = sentence(List)  # 'Vatsan took his dog for a spin'
q
