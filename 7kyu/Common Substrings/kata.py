def substring_test(s1, s2):
    if s1 and s2:
        s1, s2 = map(str.lower, [s1, s2])
        smallest, largest = (s1, s2) if len(s1) < len(s2) else (s2, s1)

        for i in range(len(smallest) - 1):
            if smallest[i : i + 2] in largest:
                return True
    return False
