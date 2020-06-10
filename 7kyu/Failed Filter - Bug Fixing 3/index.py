""" 7kyu - Failed Filter - Bug Fixing #3

Oh no, Timmy's filter doesn't seem to be working.
Your task is to fix the FilterNumber function to remove all the numbers from the string.  """


def filter_numbers(string):
    return ''.join(x for x in string if not x.isdigit())


q = filter_numbers("test123"), 'test'
q
q = filter_numbers("a1b2c3"), 'abc'
q
q = filter_numbers("aa1bb2cc3dd"), 'aabbccdd'
q
