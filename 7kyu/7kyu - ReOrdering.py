# 7kyu - ReOrdering

""" There is a sentence which has a mistake in its ordering.

The part with a capital letter should be the first word.

Please build a function for re-ordering """


# def re_ordering(text):
#     arr = text.split()
#     upper = list(filter(lambda x: x[0].upper() == x[0], arr))
#     lower = list(filter(lambda x: x[0].lower() == x[0], arr))
#     return ' '.join(upper + lower)


def re_ordering(text):
    return ' '.join(sorted(text.split(), key=str.islower))


q = re_ordering('ming Yao')  # 'Yao ming'
q
q = re_ordering('Mano donowana')  # 'Mano donowana'
q
q = re_ordering('wario LoBan hello')  # 'LoBan wario hello'
q
q = re_ordering('bull color pig Patrick')  # 'Patrick bull color pig'
q
q = re_ordering('ming Yao')  # 'Yao ming'
q
q = re_ordering('Mano donowana')  # 'Mano donowana'
q
q = re_ordering('wario LoBan hello')  # 'LoBan wario hello'
q
q = re_ordering('bull color pig Patrick')  
q
#     'Patrick bull color pig'
q = re_ordering('jojo ddjajdiojdwo ana G nnibiial')
q
#     'G jojo ddjajdiojdwo ana nnibiial'
q = re_ordering(
    'is one of those rare names that s both exotic and simple Adira')
q
#     'Adira is one of those rare names that s both exotic and simple'
q = re_ordering(
    'is an older name than annabel Amabel and a lot more distinctive')
q
#     'Amabel is an older name than annabel and a lot more distinctive'