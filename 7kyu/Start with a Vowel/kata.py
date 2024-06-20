import re

def vowel_start(st):
    chars = re.sub(r"[\W_]", "", st.lower())
    return re.sub(r"\B([aeiou])", r" \1", chars)
