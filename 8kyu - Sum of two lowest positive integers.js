// 8kyu - Sum of two lowest positive integers

// const sumTwoSmallestNumbers = numbers => numbers.sort((a, b) => a - b).slice(0, 2).reduce((a, b) => a + b, 0)
const sumTwoSmallestNumbers = numbers => { [a, b] = numbers.sort((a, b) => a - b); return a + b }

q = sumTwoSmallestNumbers([5, 8, 12, 19, 22]) // 13 
q
q = sumTwoSmallestNumbers([15, 28, 4, 2, 43]) //  6 
q
q = sumTwoSmallestNumbers([3, 87, 45, 12, 7]) // 10 
q
q = sumTwoSmallestNumbers([23, 71, 33, 82, 1]) // 24 
q
q = sumTwoSmallestNumbers([52, 76, 14, 12, 4]) // 16 
q