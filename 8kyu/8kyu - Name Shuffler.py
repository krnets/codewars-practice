# 8kyu - Name Shuffler

""" Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john" """


def name_shuffler(str):
    firstname, lastname = str.split()
    return f'{lastname} {firstname}'

# def name_shuffler(str):
#     return ' '.join(str.split()[::-1])


q = name_shuffler('john McClane')  # 'McClane john'
q
q = name_shuffler('Mary jeggins')  # 'jeggins Mary'
q
q = name_shuffler('tom jerry')  # 'jerry tom'
q
