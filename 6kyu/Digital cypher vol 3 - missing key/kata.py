def find_the_key(message, code):
    offset = ord("a") - 1
    key_cycle = [d - (ord(c) - offset) for d, c in zip(code, message)]
    key_joined = "".join(map(str, key_cycle))
    n = len(key_joined)

    for i in range(1, n + 1):
        sub = key_joined[:i]

        if key_joined == (n * sub)[:n]:
            return int(sub)
