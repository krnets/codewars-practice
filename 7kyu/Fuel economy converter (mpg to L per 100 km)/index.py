""" 7kyu - Fuel economy converter (mpg <-> L/100 km)

While mpg (miles per gallon) is a common unit of measurement for fuel economy in North America, 
for Europe the standard unit of measurement is generally liter per 100 km. 
Conversion between these units is somewhat hard to calculate in your head, 
so your task here is to implement a simple convertor in both directions.

Functions

    mpg2lp100km() converts from miles per gallon to liter per 100 km.
    lp100km2mpg() converts in the opposite direction.

Output

The output of both functions should be a number rounded to 2 decimal places.

Examples

    mpg2lp100km(42) returns 5.6
    lp100km2mpg( 9) returns 26.13

Reference

For this kata, use U.S. gallon, not imperial gallon.

    1 gallon = 3.785411784 liters
    1 mile = 1.609344 kilometers """

LT_G = 3.785411784
KM_M = 1.609344


def mpg2lp100km(mpg):
    return round(LT_G / (mpg * KM_M / 100), 2)


def lp100km2mpg(lp100km):
    return round(100 / KM_M / (lp100km / LT_G), 2)


q = mpg2lp100km(42), 5.6
q

q = lp100km2mpg(9), 26.13
q
