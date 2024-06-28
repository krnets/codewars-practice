# def format_duration(seconds):
#     if seconds == 0:
#         return "now"
#     res = []
#     years, seconds = divmod(seconds, 60**2 * 24 * 365)
#     days, seconds = divmod(seconds, 60**2 * 24)
#     hours, seconds = divmod(seconds, 60**2)
#     minutes, seconds = divmod(seconds, 60)

#     if years:
#         res.append("{} year{}".format(years, ("", "s")[years > 1]))
#     if days:
#         res.append("{} day{}".format(days, ("", "s")[days > 1]))
#     if hours:
#         res.append("{} hour{}".format(hours, ("", "s")[hours > 1]))
#     if minutes:
#         res.append("{} minute{}".format(minutes, ("", "s")[minutes > 1]))
#     if seconds:
#         res.append("{} second{}".format(seconds, ("", "s")[seconds > 1]))
#     return res[0] if len(res) == 1 else ", ".join(res[:-1]) + " and " + res[-1]

# duration_units = {
#     "year": 60**2 * 24 * 365,
#     "day": 60**2 * 24,
#     "hour": 60**2,
#     "minute": 60,
#     "second": 1,
# }

# def format_duration(seconds):
#     if seconds == 0:
#         return "now"
#     res = []
#     for name, divisor in duration_units.items():
#         unit, seconds = divmod(seconds, divisor)
#         if unit:
#             res.append(f"{unit} {name}" + ("", "s")[unit > 1])
#     if len(res) == 1:
#         return res[0]
#     return ", ".join(res[:-1]) + " and " + res[-1]

duration_units = {
    "second": 1,
    "minute": (m := 60),
    "hour": (h := m**2),
    "day": (d := 24 * h),
    "year": 365 * d,
}


def format_duration(seconds):
    if seconds == 0:
        return "now"
    res = []

    for name, divisor in reversed(duration_units.items()):
        unit, seconds = divmod(seconds, divisor)
        if unit:
            res.append(f"{unit} {name}" + ("", "s")[unit > 1])

    if len(res) == 1:
        return res[0]
    return ", ".join(res[:-1]) + " and " + res[-1]
