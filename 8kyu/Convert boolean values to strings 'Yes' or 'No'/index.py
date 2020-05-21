# 8kyu - Convert boolean values to strings 'Yes' or 'No'

""" Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false. """


# def bool_to_word(boolean):
#     return 'Yes' if boolean else 'No'

def bool_to_word(boolean):
    return ['No', 'Yes'][boolean]


q = bool_to_word(True)  # 'Yes'
q
q = bool_to_word(False)  # 'No'
q
