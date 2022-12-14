import re

# def filter_string(string):
#     return int(''.join(re.findall('\d+', string)))
    
# def filter_string(string):
#     return int(re.sub('\D', '', string))

def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))

q = filter_string("123")  # 123
q
q = filter_string("a1b2c3")  # 123
q
q = filter_string("aa1bb2cc3dd")  # 123
q
q = filter_string("aa 11  # 3dd")  # 1123
q
q = filter_string("11bb2c23c3")  # 112233
q