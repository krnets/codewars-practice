from calendar import month_abbr


def driver(data):
    name = data[2][:5].upper().ljust(5, "9")
    decade = data[3][-2]
    month = list(month_abbr).index(data[3][3:6]) + (50 if data[-1] == "F" else 0)
    date = data[3][:2]
    year = data[3][-1]
    initials = data[0][0] + (data[1][0] if data[1] else "9")

    return f"{name}{decade}{month:02d}{date}{year}{initials}9AA"
