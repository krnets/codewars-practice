# def expression_out(exp):
#     ops_table = { "+": "Plus", "-": "Minus", "*": "Times", "/": "Divided By", "**": "To The Power Of", "=": "Equals", "!=": "Does Not Equal" }
#     num_spelled = { "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten" }
#     arr = []

#     for i, token in enumerate(exp.split()):
#         if i == 1 and token in num_spelled:
#             return "That's not an operator!"
#         else:
#             if token in ops_table:
#                 arr.append(ops_table[token])
#             elif token in num_spelled:
#                 arr.append(num_spelled[token])
#             else:
#                 return "That's not an operator!"
#     return " ".join(arr)

def expression_out(exp):
    ops_table = { "+": "Plus", "-": "Minus", "*": "Times", "/": "Divided By", "**": "To The Power Of", "=": "Equals", "!=": "Does Not Equal" }
    num_spelled = { "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten" }
    arr = exp.split()
    if arr[1] not in ops_table:
        return "That's not an operator!"
    return ' '.join((num_spelled.get(x), ops_table.get(x))[i & 1] for i, x in enumerate(arr))
