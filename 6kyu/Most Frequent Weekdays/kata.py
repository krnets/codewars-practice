# from collections import defaultdict
# from datetime import date, timedelta


# def most_frequent_days(year):
#     dt = date(year, 1, 1)
#     counter = defaultdict(int)

#     while dt.year == year:
#         counter[dt.strftime("%A")] += 1
#         dt += timedelta(days=1)

#     most = max(counter.values())
#     dow = [date(2024, 1, i).strftime("%A") for i in range(1, 8)]

#     return sorted((k for k, v in counter.items() if v == most), key=dow.index)


from calendar import day_name, weekday

def most_frequent_days(year):
    most = {weekday(year, 1, 1), weekday(year, 12, 31)}
    return [day_name[day] for day in sorted(most)]
