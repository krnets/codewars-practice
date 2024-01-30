def sing():
    n = 99
    res = []
    while n:
        res.append(f"{n} bottle{'s' if n > 1 else ''} of beer on the wall, {n} bottle{'s' if n > 1 else ''} of beer.")
        n -= 1
        res.append(f"Take one down and pass it around, {n if n else 'no more'} bottle{'' if n == 1 else 's'} of beer on the wall.")
    res.append("No more bottles of beer on the wall, no more bottles of beer.")
    res.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return res
