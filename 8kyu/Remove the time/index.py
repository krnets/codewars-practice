# 8kyu - Remove the time

""" You're re-designing a blog and the blog's posts have the following format 
for showing the date and time a post was made:

Weekday Month Day, time e.g., Friday May 2, 7pm

You're running out of screen real estate, and on some pages you want to display a shorter format, 
Weekday Month Day that omits the time.

Write a function, shortenToDate, that takes the Website date/time in its original string format, 
and returns the shortened format.

Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". 
Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2". """


def shorten_to_date(long_date):
    return long_date.split(',')[0]


q = shorten_to_date("Monday February 2, 8pm")  # "Monday February 2"
q
q = shorten_to_date("Tuesday May 29, 8pm")  # "Tuesday May 29"
q
q = shorten_to_date("Wed September 1, 3am")  # "Wed September 1"
q
q = shorten_to_date("Friday May 2, 9am")  # "Friday May 2"
q
q = shorten_to_date("Tuesday January 29, 10pm")  # "Tuesday January 29"
q
