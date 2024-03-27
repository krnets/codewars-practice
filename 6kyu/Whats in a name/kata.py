def name_in_str(strng: str, name: str) -> bool:
    name = name.lower()
    i = 0
    for c in strng.lower():
        if c == name[i]:
            i += 1
            if i == len(name):
                return True
    return False
