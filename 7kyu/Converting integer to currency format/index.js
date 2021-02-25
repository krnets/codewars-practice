// 7kyu - Converting integer to currency format

/* Write a function that takes an integer in input and outputs a string with currency format.
Integer in currency format is expressed by a string of number where every three characters are separated by comma.

123456 --> "123,456"

Input will always be an positive integer, so don't worry about type checking or negative/float values. */

// let formatter = Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'})
// return formatter.format(price)

const toCurrency = price => price.toLocaleString()

price1 = 123456
price2 = 1234
price3 = 123
price4 = 123456789012
q = toCurrency(price1) // '123,456'
q
q = toCurrency(price2) // '1,234'
q
q = toCurrency(price3) // '123'
q
q = toCurrency(price4) // '123,456,789,012'
q
