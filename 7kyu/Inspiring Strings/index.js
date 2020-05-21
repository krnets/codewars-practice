// 7kyu - Inspiring Strings

// function longestWord(str) {
//     let longestFound = ''
//     let array = str.split(' ')
//     for (let i = 0; i < array.length; i++)
//         if (array[i].length >= longestFound.length)
//             longestFound = array[i]
//     return longestFound
// }

// const longestWord = str => str.split(' ').reverse().sort((a, b) => b.length - a.length)[0]
const longestWord = str => str.split(' ').sort((b, a) => b.length - a.length).pop()
// 
// const longestWord = str => str.split(' ').reduce((acc, i) => acc = (acc.length > i.length) ? acc : i, '')
// const longestWord = str => str.split(' ').reduceRight((acc, i) => (i.length > acc.length) ? i : acc)


q = longestWord('a b c d e fgh') //  "fgh"
q
q = longestWord('one two three') //  "three"
q
q = longestWord('red blue grey') // "grey"
q