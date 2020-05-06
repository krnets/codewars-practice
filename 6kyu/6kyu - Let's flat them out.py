# 6kyu - Let's flat them out

""" Sometimes we are faced with problems when we have a big nested dictionary with which it's hard to work. 
Now, we need to solve this problem by writing a function that will flatten a given dictionary.

Info Python dictionaries are a convenient data type to store and process configurations. 
They allow you to store data by keys to create nested structures. 
You are given a dictionary where the keys are strings and the values are strings or dictionaries. 
The goal is flatten the dictionary, but save the structures in the keys. 
The result should be a dictionary without the nested dictionaries. 
The keys should contain paths that contain the parent keys from the original dictionary. 
The keys in the path are separated by a /. If a value is an empty dictionary, 
then it should be replaced by an empty string "". """

""" {
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"
        }
    }
}

The result will be:

{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}

Input: An original dictionary as a dict.
Output: The flattened dictionary as a dict.
Precondition: Keys in a dictionary are non-empty strings. 
              Values in a dictionary are strings or dicts. root_dictionary != {}

flatten({"key": "value"}) == {"key": "value"}
flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
flatten({"empty": {}}) == {"empty": ""} """


# from collections import MutableMapping

# def flatten(dictionary, parent_key='', sep='/'):
#     result = []
#     for k, v in dictionary.items():
#         new_key = parent_key + sep + k if parent_key else k
#         if isinstance(v, MutableMapping):
#             result.extend(flatten(v, new_key, sep=sep).items())
#         else:
#             result.append((new_key, v))
#     return dict(result) or {parent_key: ''}

# def flatten(dictionary):
#     result = {}
#     for k, v in dictionary.items():
#         if v == {}:
#             result[k] = ""
#         elif isinstance(v, dict):
#             for l, w in flatten(v).items():
#                 result[k + '/' + l] = w
#         else:
#             result[k] = v
#     return result

def flatten(dictionary, prefix=[]):
    res = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict) and dictionary[key]:
            res.update(flatten(dictionary[key], prefix + [key]))
        else:
            res["/".join(prefix + [key])] = dictionary[key] or ''
    return res

# def flatten(dictionary):
#     stack = [((), dictionary)]
#     result = {}
#     while stack:
#         path, current = stack.pop()
#         for k, v in current.items():
#             if v == {}:
#                 result['/'.join(path + (k,))] = ''
#             if isinstance(v, dict):
#                 stack.append((path + (k,), v))
#             else:
#                 result['/'.join(path + (k,))] = v
#     return result


q = flatten({"key": "value"}), {"key": "value"}  # "Simple"
q
q = flatten({"key": {"deeper": {"more": {"enough": "value"}}}})
# {"key/deeper/more/enough": "value"}  # "Nested"
q
q = flatten({"empty": {}}), {"empty": ""}  # "Empty value"
q

q = flatten({
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"
        }
    }
})
q
#  {"name/first": "One", "name/last": "Drone", "job": "scout", "recent": "", "additional/place/zone": "1", "additional/place/cell": "2" })
