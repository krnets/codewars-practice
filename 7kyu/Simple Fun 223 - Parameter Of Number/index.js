// 7kyu - Simple Fun #223: Parameter Of Number

/* Let's define a parameter of number n as the least common multiple (LCM) of the sum of its digits and their product.
Calculate the parameter of the given number n.

[input] integer n
A positive integer. It is guaranteed that no zero appears in n.

[output] an integer
The parameter of the given number.

For n = 22, the output should be 4.
Both the sum and the product of digits equal 4, and LCM(4, 4) = 4.

For n = 1234, the output should be 120.
1+2+3+4=10 and 1*2*3*4=24, LCM(10,24)=120 */


// function parameter(n) {
//     let arr = [...String(n)]
//     let sum = arr.reduce((a, b) => a + Number(b), 0)
//     let product = arr.reduce((a, b) => a * b, 1)
//     let gcd = (a, b) => b ? gcd(b, a % b) : a
//     let lcm = (a, b) => a * b / gcd(a, b)
//     return lcm(sum, product)
// }

// const lcm = (a, b) => a / gcd(a, b) * b
// const gcd = (a, b) => b == 0 ? a : gcd(b, a % b)
// const parameter = n => (n => lcm(n.reduce((a, b) => a + +b, 0), n.reduce((a, b) => a * +b, 1)))((n + '').split(''))

function parameter(n) {
    const gcd = (a, b) => b ? gcd(b, a % b) : a
    const lcm = (a, b) => a * b / gcd(a, b)
    let [sum, product] = [...String(n)].reduce(([s, p], d) => [+d + s, p * d], [0, 1])
    return lcm(sum, product)
}

q = parameter(22) // 4
q
q = parameter(1234) // 120
q
q = parameter(123) // 6
q
q = parameter(11) // 2
q
q = parameter(239) // 378
q
q = parameter(999999999) // 387420489
q
q = parameter(91) // 90
q
q = parameter(344) // 528
q
q = parameter(123456789) // 362880
q