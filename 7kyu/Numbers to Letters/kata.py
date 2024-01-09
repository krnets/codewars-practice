from string import ascii_lowercase

def switcher(arr):
    letters = "".join(reversed(" ?!" + ascii_lowercase + "_"))
    return "".join(letters[x] for x in map(int, arr))
