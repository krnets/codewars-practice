from datetime import datetime


# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     if entered_code is correct_code:
#         input_format = "%B %d, %Y"
#         d1 = datetime.strptime(current_date, input_format)
#         d2 = datetime.strptime(expiration_date, input_format)
#         return d1 <= d2
#     return False


def check_coupon(entered_code, correct_code, *dates):
    d1, d2 = map(lambda x: datetime.strptime(x, "%B %d, %Y"), dates)
    return entered_code is correct_code and d1 <= d2
