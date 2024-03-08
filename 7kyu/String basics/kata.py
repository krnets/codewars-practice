# def get_users_ids(string):
#     return [w.replace("uid", "", 1).strip()
#             for w in string.lower().replace("#", "").split(",")]

import re

def get_users_ids(string):
    return [re.findall("(?<=uid).*", w)[0].strip() 
            for w in string.replace("#", "").lower().split(",")]
