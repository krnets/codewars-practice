# 7kyu - Counting in the Amazon

"""  The Arara are an isolated tribe found in the Amazon who count in pairs. 
For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak

Take a given number and return the Arara's equivalent.

count_arara(3) # -> 'adak anane'
count_arara(8) # -> 'adak adak adak adak' """


# def count_arara(n):
#     return 'adak ' * (n // 2) + 'anane' if n % 2 else ('adak ' * (n // 2)).rstrip()

def count_arara(n):
    return ' '.join(['adak'] * (n // 2) + ['anane'] * (n % 2))


q = count_arara(1)  # "anane"
q
q = count_arara(2)  # "adak"
q
q = count_arara(3)  # "adak anane"
q
q = count_arara(8)  # adak adak adak adak
q
q = count_arara(9)  # "adak adak adak adak anane"
q
