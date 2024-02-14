import re

def sort_the_inner_content(words):
    return re.sub(r"\B\w+\B", lambda m: "".join(sorted(m.group(), reverse=True)), words)
