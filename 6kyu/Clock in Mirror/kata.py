def what_is_the_time(time_in_mirror):
    hh, mm = map(int, time_in_mirror.split(":"))
    mm = (60 - mm) % 60
    hh = (12, 11)[mm > 0] - hh % 12
    hh = (12, hh)[hh > 0]
    return "{:02}:{:02}".format(hh, mm)
