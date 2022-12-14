# 7kyu - The Coupon Code

""" Your online store likes to give out coupons for special occasions. 
Some customers try to cheat the system by entering invalid codes or using expired coupons.

Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. 
All dates will be passed as strings in this format: "MONTH DATE, YEAR".

checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False """

# import datetime

# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     cur = datetime.datetime.strptime(current_date, '%B %d, %Y')
#     exp = datetime.datetime.strptime(expiration_date, '%B %d, %Y')
#     return entered_code is correct_code and cur <= exp

from datetime import datetime as dt

# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     format = '%B %d, %Y'
#     current = datetime.strptime(current_date, format)
#     expiration = datetime.strptime(expiration_date, format)
#     return entered_code is correct_code and current <= expiration

# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     parse = datetime.strptime
#     format = '%B %d, %Y'
#     return entered_code is correct_code and parse(current_date, format) <= parse(expiration_date, format)


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    format = "%B %d, %Y"
    current = dt.strptime(current_date, format)
    expiration = dt.strptime(expiration_date, format)
    return entered_code is correct_code and current <= expiration


q = check_coupon("123", "123", "September 5, 2014", "October 1, 2014")  # True
q
q = check_coupon("123a", "123", "September 5, 2014", "October 1, 2014")  # False
q
