# 8kyu - Well of Ideas - Easy Version

""" For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. 
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. 
If there are no good ideas, as is often the case, return 'Fail!'. """


# def well(x):
#     res = len(list(filter(lambda l: l == 'good', x)))
#     return 'Fail!' if res == 0 else 'Publish!' if res <= 2 else 'I smell a series!'

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


q = well(['bad', 'bad', 'bad'])  # 'Fail!'
q
q = well(['good', 'bad', 'bad', 'bad', 'bad'])  # 'Publish!'
q
q = well(['good', 'bad', 'bad', 'bad', 'bad', 'good',
          'bad', 'bad', 'good'])  # 'I smell a series!'
q
