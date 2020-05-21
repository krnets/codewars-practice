// 7kyu - Summing a number's digits

/* Write a function named sumDigits which takes a number as input and 
returns the sum of the absolute value of each of the number's decimal digits.

Let's assume that all numbers in the input will be integer values. */

const sumDigits = number => [...String(Math.abs(number))].reduce((a, b) => a + Number(b), 0)
// const sumDigits = number => +(number + '').match(/\d/g).reduce((a, b) => +a + +b)

q = sumDigits(10) // 1
q
q = sumDigits(99) // 18
q
q = sumDigits(-32) // 5
q