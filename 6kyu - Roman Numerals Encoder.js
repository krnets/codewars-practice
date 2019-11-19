// 6kyu - Roman Numerals Encoder

/* Create a function taking a positive integer as its parameter and 
returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately 
starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

solution(1000); // should return 'M'

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Edges

IV
IX
XL
XC
CD
CM
MMMDCD  3,999
2017 = MMXVII

Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals  */

// if (number > 3999 || number < 1)
//     throw new Error('Range Error')


function solution(number) {
    let roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    let numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    let result = ''
    let i = 0

    while (number > 0) {
        if (number - numbers[i] >= 0) {
            result += roman[i]
            number -= numbers[i]
        } else i++
    }
    return result
}

// let roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
// let numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

// function solution(number) {
//     let roman = { M:1000, CM:900, D:500, CD:400, C:100, XC:90, L:50, XL:40, X:10, IX:9, V:5, IV:4, I:1 }
//     let result = ''

//     while (number > 0) {
//         for (n in roman)
//             if (roman[n] <= number) {
//                 result += n
//                 number -= roman[n]
//                 break
//             }
//     }
//     return result
// }

// function solution(number) {
//     let numerals = {
//         M: 1000,
//         CM: 900,
//         D: 500,
//         CD: 400,
//         C: 100,
//         XC: 90,
//         L: 50,
//         XL: 40,
//         X: 10,
//         IX: 9,
//         V: 5,
//         IV: 4,
//         I: 1
//     }
//     let result = ''

//     Object.keys(numerals).forEach(e => {
//         let n = Math.floor(number / numerals[e])
//         number -= n * numerals[e]
//         result += e.repeat(n)
//     })
//     return result
// }

// function solution(number) {
//     let RomanNumerals = [
//         [1000, 'M'],
//         [900, 'CM'],
//         [500, 'D'],
//         [400, 'CD'],
//         [100, 'C'],
//         [90, 'XC'],
//         [50, 'L'],
//         [40, 'XL'],
//         [10, 'X'],
//         [9, 'IX'],
//         [5, 'V'],
//         [4, 'IV'],
//         [1, 'I']
//     ]
//     for (let [num, notation] of RomanNumerals)
//         if (number >= num)
//             return notation + solution(number - num)
//     return ''
// }

// function solution(number) {
//     let romanNumerals = [
//         ['M', 1000],
//         ['CM', 900],
//         ['D', 500],
//         ['CD', 400],
//         ['C', 100],
//         ['XC', 90],
//         ['L', 50],
//         ['XL', 40],
//         ['X', 10],
//         ['IX', 9],
//         ['V', 5],
//         ['IV', 4],
//         ['I', 1]
//     ]
//     let result = ''
//     while (number > 0) {
//         let [character, value] = romanNumerals.shift()
//         result += (new Array(Math.floor(number / value)).fill(character)).join ``
//         number %= value
//     }
//     return result
// }

q = solution(1) // 'I'
q
q = solution(2) // 'II'
q
q = solution(3) // 'III'
q
q = solution(4) // 'IV'
q
q = solution(5) // 'V'
q
q = solution(9) // 'IX'
q
q = solution(10) // 'X'
q
q = solution(11) // 'XI'
q
q = solution(19) // 'XIX'
q
q = solution(22) // 'XXII'
q
q = solution(15) // 'XV'
q
q = solution(49) // 'XLIX'
q
q = solution(1994) // 'MCMXCIV'
q
q = solution(1000) // 'M'
q
q = solution(1001) // 'MI'
q
q = solution(1985) // 'MCMLXXXV'
q
q = solution(1990) // 'MCMXC'
q
q = solution(2007) // 'MMVII'
q
q = solution(2008) // 'MMVIII'
q
q = solution(2020) // 'MMXX'
q
q = solution(2028) // 'MMXXVIII'
q
q = solution(2029) // 'MMXXIX'
q
q = solution(3999) // 'MMMCMXCIX'
q