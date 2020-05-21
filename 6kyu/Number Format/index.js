// 6kyu - Number Format

// Format any integer provided into a string with "," (commas) in the correct places.

// const numberFormat = n => new Intl.NumberFormat('en-US' ).format(n)

const numberFormat = number => number.toLocaleString()

q = numberFormat(100000) // '100,000'
q
q = numberFormat(5678545) // '5,678,545'
q
q = numberFormat(-420902) // '-420,902'
q
q = numberFormat(-5678545) // '-5,678,545'
q