import re

def domain_name(url):
    pattern = r"(https?:\/\/)?(www\.)?"
    return re.sub(pattern, "", url).split(".")[0]
