""" 8kyu - Switch/Case - Bug Fixing #6

 Oh no! Timmy's evalObject function doesn't work. 
 He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function? """


# def eval_object(v):
#     return {"+": v['a'] + v['b'],
#             "-": v['a'] - v['b'],
#             "/": v['a'] / v['b'],
#             "*": v['a'] * v['b'],
#             "%": v['a'] % v['b'],
#             "**": v['a'] ** v['b'], }.get(v['operation'])

def eval_object(v):
    return eval('{a}{operation}{b}'.format(**v))


q = eval_object({'a': 1, 'b': 1, 'operation': '+'}), 2
q
q = eval_object({'a': 1, 'b': 1, 'operation': '-'}), 0
q
q = eval_object({'a': 1, 'b': 1, 'operation': '/'}), 1
q
q = eval_object({'a': 1, 'b': 1, 'operation': '*'}), 1
q
q = eval_object({'a': 1, 'b': 1, 'operation': '%'}), 0
q
q = eval_object({'a': 1, 'b': 1, 'operation': '**'}), 1
q
