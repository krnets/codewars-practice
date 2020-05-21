# 6kyu - Format a string of names like 'Bart, Lisa & Maggie'.

""" Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, 
which should be separated by an ampersand.

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'. """

# def namelist(names):
#     ns = [x.get('name') for x in names]
#     if len(ns) > 1:
#         return ', '.join(ns[0:-1]) + ' & ' + ns[-1]
#     elif len(ns) == 1:
#         return ns[0]
#     else:
#         return ''

def namelist(names):
    ns = [x.get('name') for x in names]
    if len(ns) > 1:
        return '{} & {}'.format(', '.join(ns[0:-1]), ns[-1])
    elif len(ns) == 1:
        return ns[0]
    else:
        return ''


q = namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
q
#     'Bart, Lisa, Maggie, Homer & Marge',
q = namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
q
#    'Bart, Lisa & Maggie',
q = namelist([{'name': 'Bart'}, {'name': 'Lisa'}])  # 'Bart & Lisa',
q
q = namelist([{'name': 'Bart'}])  # 'Bart'
q
q = namelist([])  # ''
q
