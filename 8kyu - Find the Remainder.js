// 8kyu - Find the Remainder

// const remainder = (a, b) => (a == 0 || b == 0) ? 'NaN' : (a > b) ? a % b : b % a
const remainder = (a, b) => (a > b) ? a % b : b % a

q = remainder(0, 92)
q
q = remainder(3, 92)
q
q = remainder(13, 72)
q
q = remainder(72, 13)
q
q = isNaN(remainder(1, 0)) // 'Divide by zero should return NaN'
q
q = isNaN(remainder(0, 0)) // 'Divide by zero should return NaN'
q