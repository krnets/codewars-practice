// 7kyu - Put a Letter in a Column

/* Create a function that takes index [0, 8] and a character. 
It returns a string with columns. Put character in column marked with index.
Ex.: index = 2, character = 'B'

| | |B| | | | | | |
 0 1 2 3 4 5 6 7 8

Assume that argument index is integer [0, 8]. Assume that argument character is string with one character.
Hint: http://devdocs.io/javascript/global_objects/string/substr
Fundamentals | Strings */

// function buildRowText(index, character) {
//     let res = ''
//     for (let i = 0; i < 9; i++) {
//         res += '|'
//         if (i == index) res += character
//         else res += ' '
//     }
//     return res + '|'
// }

// function buildRowText(index, character) {
//     let s = Array(9).fill(' ')
//     s[index] = character
//     return '|' + s.join('|') + '|'
// }

// const buildRowText = (index, character) => {
//     let str = '| | | | | | | | | | |';
//     return str.substr(0, 2 * (index + 2) - 3) + character + str.substr(2 * (index + 2))
// }

// function buildRowText(index, character) {
//     let row = "| | | | | | | | | |"
//     // return row.substring(0, index * 2 + 1) + character + row.substring((index + 1) * 2)
//     return row.slice(0, index * 2 + 1) + character + row.slice((index + 1) * 2)
// }

// const buildRowText = (index, character) => Array(index + 1).join('| ') + '|' + character + '|' + Array(9 - index).join(' |')
// const buildRowText = (index, character) => Array(10).fill().map((_, i) => i == index ? `|${character}` : '| ').join('').trim()
// const buildRowText = (index, character) => '| '.repeat(index) + '|' + character + '|' + ' |'.repeat(9 - index - 1)
// const buildRowText = (index, character) => '| '.repeat(index)+`|${character}|`+' |'.repeat(9-index-1)

q = buildRowText(2, 'A') // '| | |A| | | | | | |'
q