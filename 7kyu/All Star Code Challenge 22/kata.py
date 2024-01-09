# def to_time(seconds):
#     seconds_in_hour = 60 * 60
#     hours = seconds // seconds_in_hour
#     remaining_seconds = seconds - hours * seconds_in_hour
#     minutes = remaining_seconds // 60
#     return f"{hours} hour(s) and {minutes} minute(s)"


def to_time(seconds):
    return "{} hour(s) and {} minute(s)".format(*divmod(seconds // 60, 60))
