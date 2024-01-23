from datetime import datetime
from dateutil.relativedelta import relativedelta


# def how_many_years(date1, date2):
#     y1 = datetime.strptime(date1, "%Y/%m/%d")
#     y2 = datetime.strptime(date2, "%Y/%m/%d")
#     return abs(relativedelta(y1, y2).years)


def how_many_years(date1, date2):
    y1 = datetime.strptime(date1, "%Y/%m/%d").year
    y2 = datetime.strptime(date2, "%Y/%m/%d").year
    return abs(y1 - y2)
