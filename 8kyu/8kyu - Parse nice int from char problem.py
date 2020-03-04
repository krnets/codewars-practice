# 8kyu - Parse nice int from char problem

""" Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only. """


# def get_age(age):
#     return int(age[0])

# def get_age(age):
#     return int(age.split(' ')[0])

def get_age(age):
    return int(age.split()[0])


q = get_age("2 years old")  # 2
q
q = get_age("4 years old")  # 4
q
q = get_age("5 years old")  # 5
q
q = get_age("7 years old")  # 7
q
