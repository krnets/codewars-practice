// Given an integer, write a function to return its
// roman numeral representation

// IV
// IX
// XL
// XC
// CD
// CM
// MMMDCD  3,999
// 2017 = MMXVII

const roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
const numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

function integerToRoman(number) {
    if (number > 3999 || number < 1) {
        throw new Error('Range Error')
    }

    let RomanNumeralString = '';

    let i = 0;
    while (number > 0) {
        if (number - numbers[i] >= 0) {
            // console.log(number)
            // console.log(roman[i])
            RomanNumeralString += roman[i]
            number -= numbers[i]
        } else {
            i++
        }
    }
    // console.log(RomanNumeralString)
    return RomanNumeralString
}

q = integerToRoman(1) === 'I'
q
q = integerToRoman(4) === 'IV'
q
q = integerToRoman(49) === 'XLIX'
q
q = integerToRoman(1985) === 'MCMLXXXV'
q
q = integerToRoman(2020) === 'MMXX'
q
q = integerToRoman(2028) === 'MMXXVIII'
q
q = integerToRoman(2029) === 'MMXXIX'
q
q = integerToRoman(1994) === 'MCMXCIV'
q
q = integerToRoman(3999) === 'MMMCMXCIX'
q