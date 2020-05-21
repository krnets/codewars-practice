// 7kyu - Number of Decimal Digits

/* Determine number of decimal digits in an unsiged integer. 
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
Be careful to avoid overflows/underflows.   */

const digits = (n) => String(n).length

q = digits(5) // 1
q
q = digits(12345) // 5
q
q = digits(9876543210) // 10
q