# 7kyu - Populate hash with array keys and default value

""" Complete the function so that it takes an array of keys and a default value and returns dictionary 
with all keys set to the default value.

["draft", "completed"], 0   # should return {"draft": 0, "completed: 0} """


# def populate_dict(keys, default):
#     res = {}
#     for x in keys:
#         res[x] = default
#     return res

# def populate_dict(keys, default):
#     return {key: default for key in keys}

# populate_dict = dict.fromkeys

def populate_dict(keys, default):
    return dict.fromkeys(keys, default)

q = populate_dict(["draft", "completed"], 0)  # {"completed": 0, "draft": 0}
q
q = populate_dict(["a", "b", "c"], None)  # {"c": None, "b": None, "a": None}
q
q = populate_dict([1, 2, 3, 4], "OK")  # {1: "OK", 2: "OK", 3: "OK", 4: "OK"}
q
