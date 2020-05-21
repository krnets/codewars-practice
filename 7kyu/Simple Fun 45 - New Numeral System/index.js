// 7kyu - Simple Fun #45: New Numeral System

/* Your Informatics teacher at school likes coming up with new ways to help you understand the material. 
When you started studying numeral systems, he introduced his own numeral system, which he's convinced 
will help clarify things. His numeral system has base 26, and its digits are represented by 
English capital letters - A for 0, B for 1, and so on.

The teacher assigned you the following numeral system exercise: given a one-digit number, you should find all unordered pairs of one-digit numbers whose values add up to the number.

For number = 'G', the output should be ["A + G", "B + F", "C + E", "D + D"]

Translating this into the decimal numeral system we get: number = 6, so it is ["0 + 6", "1 + 5", "2 + 4", "3 + 3"].

    [input] string(char in C#) number
    A character representing a correct one-digit number in the new numeral system.

    Constraints: 'A' ≤ number ≤ 'Z'.

    [output] a string array
    An array of strings in the format "letter1 + letter2", where "letter1" and "letter2" are correct 
    one-digit numbers in the new numeral system. The strings should be sorted by "letter1".

    Note that "letter1 + letter2" and "letter2 + letter1" are equal pairs and we don't consider them to be different. */

// function newNumeralSystem(number) {
//     let charA = 'A'.charCodeAt()
//     let index = charA + number.charCodeAt()
//     let len = Math.ceil((number.charCodeAt() - charA + 1) / 2)
//     return [...Array(len).keys()].map(v => String.fromCharCode(charA + v) + ' + ' + String.fromCharCode(index - v - charA))
// }

function newNumeralSystem(number) {
    let charA = 'A'.charCodeAt()
    let len = Math.ceil((number.charCodeAt() - charA + 1) / 2)
    return [...Array(len).keys()].map(v => String.fromCharCode(charA + v) + ' + ' + String.fromCharCode(number.charCodeAt() - v))
}

// const newNumeralSystem = (num) => [...Array(Math.ceil((num.charCodeAt() - 'A'.charCodeAt() + 1) / 2)).keys()]
//     .map(v => String.fromCharCode('A'.charCodeAt() + v) + ' + ' + String.fromCharCode(num.charCodeAt() - v))

// const newNumeralSystem = (num) => [...Array(Math.ceil((num.charCodeAt() - 64) / 2)).keys()].map(v => String.fromCharCode(65 + v) + ' + ' + String.fromCharCode(num.charCodeAt() - v))

// const newNumeralSystem = n => (alpha => Array.from({
//     length: ~~((alpha.indexOf(n) + 2) / 2)
// }, (a, i) => `${alpha[i]} + ${alpha[alpha.indexOf(n)-i]}`))("ABCDEFGHIJKLMNOPQRSTUVWXYZ");

q = newNumeralSystem("G") // ["A + G",  "B + F",  "C + E",  "D + D"]
q
q = newNumeralSystem("A") // ["A + A"]
q
q = newNumeralSystem("D") // ["A + D",  "B + C"]
q
q = newNumeralSystem("E") // ["A + E",  "B + D",  "C + C"]
q
q = newNumeralSystem("O") // ["A + O",  "B + N",  "C + M",  "D + L",  "E + K",  "F + J",  "G + I",  "H + H"]
q