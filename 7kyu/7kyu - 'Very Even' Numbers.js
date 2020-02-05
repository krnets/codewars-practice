// 7kyu - "Very Even" Numbers

/* Write a function that returns true if the number is a "Very Even" number.
If the number is odd, it is not a "Very Even" number.
If the number is even, return whether the sum of the digits is a "Very Even" number.

input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 
input(222) => returns true
input(5) => returns false

Note: The numbers will always be positive! */

// function isVeryEvenNumber(n) {
//     let str = String(n)
//     while (str.length > 1)
//         str = [...str].reduce((a, b) => a + Number(b), 0).toString()
//     return str % 2 == 0
// }

// const isVeryEvenNumber = (n) => !n-- || n % 9 % 2 == 1

const isVeryEvenNumber = (n) => n < 10 ? n % 2 == 0 : isVeryEvenNumber([...n + ''].reduce((a, v) => a + v * 1, 0))

q = isVeryEvenNumber(0) // true
q
q = isVeryEvenNumber(4) // true
q
q = isVeryEvenNumber(222) // true
q
q = isVeryEvenNumber(400000220) // true
q
q = isVeryEvenNumber(24) // true
q
q = isVeryEvenNumber(12) // false
q
q = isVeryEvenNumber(88) // false
q
q = isVeryEvenNumber(1234) // false
q
q = isVeryEvenNumber(4554) // false
q
q = isVeryEvenNumber(45) // false
q
q = isVeryEvenNumber(5) // false
q