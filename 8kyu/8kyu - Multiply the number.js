// 8kyu - Multiply the number

/* Jack really likes his number five: the trick here is that you have to multiply each number by 5 
raised to the number of digits of each numbers */

const multiply = (n) => n * 5 ** String(Math.abs(n)).length
// const multiply = (n) => n * Math.pow(5, String(Math.abs(n)).length)

q = multiply(3) // 15
q
q = multiply(10) // 250
q
q = multiply(5) // 25
q
q = multiply(200) // 25000
q
q = multiply(0) // 0
q
q = multiply(-2) // -10
q
q = multiply(-3) // -15
q