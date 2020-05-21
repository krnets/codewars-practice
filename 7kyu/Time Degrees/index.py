# 7kyu - Time Degrees

""" Time, time, time. 
Your task is to write a function that will return the degrees on a analog clock from a digital time 
that is passed in as parameter. The digital time is type string and will be in the format 00:00.  
You also need to return the degrees on the analog clock in type string and format 360:360. 
Remember to round of the degrees. 
Remeber the basic time rules and format like 24:00 = 00:00 and 12:60 = 13:00. 
Create your own validation that should return "Check your time !" in any case the time is incorrect 
or the format is wrong  remember this includes passing in negatives times like "-01:-10".

A few examples :
clock_degree("00:00") will return : "360:360"
clock_degree("01:01") will return : "30:6"
clock_degree("00:01") will return : "360:6"
clock_degree("01:00") will return : "30:360"
clock_degree("01:30") will return : "30:180"
clock_degree("24:00") will return : "Check your time !"
clock_degree("13:60") will return : "Check your time !"
clock_degree("20:34") will return : "240:204"

Remember that discrete hour hand movement is required - snapping to each hour position and also coterminal angles are not allowed.  """


# def clock_degree(s):
#     hour, minute = map(int, s.split(':'))
#     if not 0 <= hour < 24 or not 0 <= minute < 60:
#         return 'Check your time !'
#     angles_in_hour = 360 / 12
#     angles_in_minute = 360 / 60
#     HH = (angles_in_hour * hour) % 360
#     MM = (angles_in_minute * minute)
#     HH = 360 if HH == 0 else HH
#     MM = 360 if MM == 0 else MM
#     return ':'.join(map(str, map(int, [HH, MM])))

def clock_degree(s):
    hours, minutes = map(int, s.split(':'))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        return 'Check your time !'
    hour_angle = 360 // 12
    minute_angle = 360 // 60
    HH = hour_angle * hours % 360 or 360
    MM = minute_angle * minutes or 360
    return f'{HH}:{MM}'


q = clock_degree("01:01"), "30:6"
q
q = clock_degree("00:00"), "360:360"
q
q = clock_degree("01:03"), "30:18"
q
q = clock_degree("01:30"), "30:180"
q
q = clock_degree("12:05"), "360:30"
q
q = clock_degree("26:78"), "Check your time !"
q
q = clock_degree("16:25"), "120:150"
q
q = clock_degree("17:09"), "150:54"
q
q = clock_degree("19:00"), "210:360"
q
q = clock_degree("20:34"), "240:204"
q
q = clock_degree("23:20"), "330:120"
q
q = clock_degree("24:00"), "Check your time !"
q
q = clock_degree("-09:00"), "Check your time !"
q
