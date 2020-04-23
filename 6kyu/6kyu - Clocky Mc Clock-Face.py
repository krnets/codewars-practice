# 6kyu - Clocky Mc Clock-Face

""" Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

And because the local council has lost most of our tax money to a Nigerian email scam 
there are no funds to fix the clock properly.

Instead, they are asking for volunteer programmers to write some code that tell the time 
by only looking at the remaining hour-hand!

Given the angle (in degrees) of the hour-hand, return the time in HH:MM format. 
Round down to the nearest minute.

    12:00 = 0 degrees
    03:00 = 90 degrees
    06:00 = 180 degrees
    09:00 = 270 degrees
    12:00 = 360 degrees

    0 <= angle <= 360 """

# def what_time_is_it(angle):
#     hour_angle = 360 / 12
#     min_angle = hour_angle / 60
#     hours = int(angle // hour_angle)
#     if hours == 0:
#         hours = 12
#     mins = int((angle // min_angle) % 60)
#     return str(hours).zfill(2) + ':' + str(mins).zfill(2)


def what_time_is_it(angle):
    a_per_hour = 360 / 12
    hours, mins = divmod(angle % 360, a_per_hour)
    return '{:02}:{:02}'.format(int(hours) or 12, int(mins * 2))


q = what_time_is_it(249.894), '08:19'
q
q = what_time_is_it(206.944), '06:53'
q
q = what_time_is_it(0), '12:00'
q
q = what_time_is_it(360), '12:00'
q
q = what_time_is_it(90), '03:00'
q
q = what_time_is_it(180), '06:00'
q
q = what_time_is_it(270), '09:00'
q
q = what_time_is_it(30), '01:00'
q
