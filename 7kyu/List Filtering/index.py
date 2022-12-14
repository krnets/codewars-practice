# 7kyu - List Filtering

""" In this kata you will create a function that takes a list of non-negative integers and strings and 
returns a new list with the strings filtered out.

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123] """


# def filter_list(l):
#     return [x for x in l if isinstance(x, int)]


# def filter_list(l):
#     return [*filter(lambda x: isinstance(x, int), l)]

# filter_list = lambda l: [elem for elem in l if isinstance(elem, int)]

filter_list = lambda l: [elem for elem in l if not isinstance(elem, str)]

q = filter_list([1, 2, 'a', 'b'])  # [1,2]
q
q = filter_list([1, 'a', 'b', 0, 15])  # [1,0,15]
q
q = filter_list([1, 2, 'aasf', '1', '123', 123])  # [1,2,123]
q
