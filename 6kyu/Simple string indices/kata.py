def solve(st, idx):
    stack = []
    matching_idx = dict()

    for i, c in enumerate(st):
        if c == "(": stack.append(i)
        elif c == ")" and stack: matching_idx[stack.pop()] = i
    return matching_idx.get(idx, -1)
