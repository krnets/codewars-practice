// 7kyu - Numbers with this digit inside

/* You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.
The value of d will always be 0 - 9.
The value of x will always be greater than 0.

You have to return as an array the count of these numbers, their sum and their product.

For example:
x = 11   d = 1   ->   Numbers: 1, 10, 11    Return: [3, 22, 110] 

If there are no numbers, which include the digit, return [0,0,0].  */


function numbersWithDigitInside(x, d) {
    let arr = [...Array(x + 1).keys()].map(String).slice(1).filter(v => v.includes(d))
    let count = arr.length
    let sum = arr.reduce((a, b) => a + Number(b), 0)
    let product = count > 0 ? arr.reduce((a, b) => a * b, 1) : 0
    return [count, sum, product]
}


q = numbersWithDigitInside(5, 6) // [ 0, 0, 0]
q
q = numbersWithDigitInside(7, 6) // [ 1, 6, 6]
q
q = numbersWithDigitInside(11, 1) // [ 3, 22, 110]
q
q = numbersWithDigitInside(20, 0) // [ 2, 30, 200]
q
q = numbersWithDigitInside(44, 4) // [ 9, 286, 5955146588160]
q