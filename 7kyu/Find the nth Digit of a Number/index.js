// 7kyu - Find the nth Digit of a Number

/* Complete the function that takes two numbers as input, 
num and nth and return the nth digit of num (counting from right to left).

If num is negative, ignore its sign and treat it as a positive value
If nth is not positive, return -1
Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0 */

function findDigit(num, nth) {
    if (nth <= 0) return -1
    let str = String(Math.abs(num))
    return str.slice(str.length - nth, str.length - nth + 1) * 1
}

// const findDigit = (num, nth) => --nth < 0 ? -1 : +('' + Math.abs(num)).split('').reverse()[nth] || 0
// const findDigit = (num, nth) => --nth < 0 ? -1 : 0 | Math.abs(num / 10 ** nth % 10)
// const findDigit = (num, nth) => nth <= 0 ? -1 : +([...('' + Math.abs(num))].reverse()[nth - 1] || 0)
// const findDigit = (num, nth) => nth > 0 ? parseInt([...Math.abs(num) + ''].reverse()[nth - 1]) || 0 : -1

q = findDigit(5673, 4) // 5
q
q = findDigit(129, 2) // 2
q
q = findDigit(-2825, 3) // 8
q
q = findDigit(-456, 4) // 0
q
q = findDigit(0, 20) // 0
q
q = findDigit(65, 0) // -1
q
q = findDigit(24, -8) // -1
q