import re
import datetime as dt


def date_correct(date):
    if not date:
        return date
    if re.fullmatch(r"(\d{2}\.){2}\d{4}", date):
        dd, mm, yy = map(int, date.split("."))
        plus_years, mm = divmod(mm, 12)
        yy += plus_years
        if mm == 0:
            mm = 12
            yy -= 1
        return (dt.date(yy, mm, 1) + dt.timedelta(days=dd - 1)).strftime("%d.%m.%Y")
