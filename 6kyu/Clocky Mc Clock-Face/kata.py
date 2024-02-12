# def what_time_is_it(angle):
#     hour_angle = 360 // 12
#     minute_angle = hour_angle / 60
#     hh = angle // hour_angle
#     mm = (angle // minute_angle) % 60

#     return f"{int(12 if hh == 0 else hh):02}:{int(mm):02}" if angle % 360 else "12:00"


def what_time_is_it(angle):
    h, m = divmod(angle, 30)
    return "{:02}:{:02}".format(int(h or 12), int(m * 2))
