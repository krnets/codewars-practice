def replace_all(obj, find, replace):
    if not obj:
        return obj
    if isinstance(obj[0], str):
        return "".join(replace if c == find else c for c in obj)
    return [replace if x == find else x for x in obj]
