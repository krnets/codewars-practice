// 6kyu - Simple Simple Simple String Expansion

/* Given a string that includes alphanumeric characters ('3a4B2d') return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string. Empty strings should return an empty string.

The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.

stringExpansion('3D2a5d2f') === 'DDDaadddddff'

stringExpansion('3abc') === 'aaabbbccc'      // correct
stringExpansion('3abc') !== 'aaabc'          // wrong
stringExpansion('3abc') !== 'abcabcabc'      // wrong

If there are two consecutive numeric characters the first one is ignored.

stringExpansion('3d332f2a') === 'dddffaa'

If there are two consecutive alphabetic characters then the first character has no effect on the one after it.

stringExpansion('abcde') === 'abcde'

Your code should be able to work for both lower and capital case letters.

stringExpansion('') === '' */


// const stringExpansion = s => s.replace(/\d\D+/gi, m => {
//     let digit = m.replace(/\D/gi, '').slice(-1)
//     let letters = m.match(/([a-z])/gi)
//     return letters.map(v => v.repeat(digit)).join('')
// }).replace(/\d+/g, '')

const stringExpansion = s => s.replace(/\d\D*/g, m => m.slice(1).replace(/./g, c => c.repeat(m[0])))

q = stringExpansion('3abc') //'aaabbbccc'
q
q = stringExpansion('3D2a5d2f') // 'DDDaadddddff'
q
q = stringExpansion('0d0a0v0t0y') // ''
q
q = stringExpansion('3d332f2a') // 'dddffaa'
q
q = stringExpansion('abcde') // 'abcde'
q
q = stringExpansion('a2bcde') // 'abbccddee'
q