# Remember you have a CHANGE dictionary to work with ;)

CHANGE = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
    "dollar": 1.00,
}


def change_count(change):
    return f"${sum(map(CHANGE.get, change.split())):.2f}"
