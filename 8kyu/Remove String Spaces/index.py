# 8kyu - Remove String Spaces

""" Simple, remove the spaces from the string, then return the resultant string. """


# def no_space(x):
#     return ''.join(x.split(' '))

def no_space(x):
    return x.replace(' ', '')


q = no_space('8 j 8   mBliB8g  imjB8B8  jl  B')  # '8j8mBliB8gimjB8B8jlB'
q
# '88Bifk8hB8BB8BBBB888chl8BhBfd'
q = no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd')
q
q = no_space('8aaaaa dddd r     ')  # '8aaaaaddddr'
q
q = no_space('jfBm  gk lf8hg  88lbe8 ')  # 'jfBmgklf8hg88lbe8')
q
q = no_space('8j aam')  # '8jaam'
q
