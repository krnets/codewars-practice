# 7kyu - 254 shades of grey

""" Why would we want to stop to only 50 shades of grey? Let's see to how many we can go.

Write a function that takes a number n as a parameter and return an array containing 
n shades of grey in hexadecimal code (#aaaaaa for example). 
The array should be sorted in ascending order starting with 
#010101, #020202, etc. (using lower case letters).

def shades_of_grey(n):
  return '''n shades of grey in an array'''

As a reminder, the grey color is composed by the same number of red, green and blue: 
#010101, #aeaeae, #555555, etc. 
# Also, #000000 and #ffffff are not accepted values.

When n is negative, just return an empty array. 
If n is higher than 254, just return an array of 254 elements. """


# def shades_of_grey(n):
#     return ['#' + hex(i)[2:].zfill(2) * 3 for i in range(1, (min(n, 254)+1))] if n else []

# def shades_of_grey(n):
#     return ['#' + format(i, '02x') * 3 for i in range(1, min(n+1, 255))] if n else []

def shades_of_grey(n):
    return ['#' + format(i, '02x') * 3 for i in range(1, min(n+1, 255))]


q = shades_of_grey(1), ['#010101']
q
q = shades_of_grey(0), ['']
q
q = shades_of_grey(254)
q
