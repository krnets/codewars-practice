""" 5kyu - Geohashing

Implement the Geohashing algorithm proposed by xkcd:
https://xkcd.com/426/

the Geohashing algorithm

Specifically, given the the Dow opening and a date in date object (optional), return the geohashing coordinates,
using the following steps (adapted from explainxkcd, slightly modified):

    Take the provided date and convert it in the format yyyy-mm-dd- at UTC time, then append the most recent opening value
    for the Dow Jones Industrial Average (supplied as an argument). Dow opening provided will always be accurate to
    2 decimal places, but if it has less than 2 decimal digits, pad 0s on the right (12345 => 12345.00).
    If no dates are provided, use current time instead.

    Pass this string through the MD5 algorithm, and output as a hexademical value.
    Divide the hash value into two 16 character halves, treat each half as base-16 decimal expansions
    (by appending 0. in the front, and convert them back to base 10, rounded to 6 decimal places.
    Return the result coordinates as an array.

An example case straight out from the comic is provided:

Date: 2005-05-26, Dow opening: 10458.68
yyyy-mm-dd-dow: 2005-05-26-10458.68
MD5: db9318c2259923d08b672cb305440f97 => db9318c2259923d0 | 8b672cb305440f97
Coordinates (HEX): [0.db9318c2259923d0, 0.8b672cb305440f97]
Coordinates (DEC): [0.857713, 0.544543]

Note: You don't have to worry about the 30W Time Zone Rule. """

from datetime import datetime
import hashlib

def geohash(dow, date=datetime.now()):
    string = f'{date.date()}-{dow:.2f}'
    encoded = hashlib.md5(string.encode()).hexdigest()
    mid = len(encoded) // 2
    left = round(float.fromhex('0.' + encoded[:mid]), 6)
    right = round(float.fromhex('0.' + encoded[mid:]), 6)
    return [left, right]


q = geohash(10458.68, datetime(2005, 5, 26))
q
#      [0.857713, 0.544543]
