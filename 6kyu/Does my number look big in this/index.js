// 6 kyu - Does my number look big in this ?

/*   A Narcissistic Number is a number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).

  For example, take 153 (3 digits):
      1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
  and 1634 (4 digits):
      1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function. */


// function narcissistic(value) {
//     let digits = [...String(value)]
//     let len = digits.length
//     return value == digits.map(v => Math.pow(v, len)).reduce((a, b) => a + b)
// }

// const narcissistic = value => [...String(value)].reduce((a, b) => a + Math.pow(b, ('' + value).length), 0) == value
// const narcissistic = value => [...String(value)].reduce((a, b) => a + Math.pow(b, String(value).length), 0) == value
const narcissistic = value => [...String(value)].reduce((s, n, _, a) => s + Math.pow(n, a.length), 0) == value
// const narcissistic = value => ('' + value).split('').reduce((s, n, _, a) => s + Math.pow(n, a.length), 0) == value

q = narcissistic(7) // true
q
q = narcissistic(371) // true
q
q = narcissistic(153) // true
q
q = narcissistic(1634) // true
q