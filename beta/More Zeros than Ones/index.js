// Beta - More Zeros than Ones

/* Create a moreZeros function which will receive a string for input, and return an array containing only 
the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are 
in the same order in the final array as they first appeared in the input string.

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']

All input will be valid strings of length > 0. */

// function moreZeros(s) {
//     let check = c => {
//         let bin = c.charCodeAt().toString(2)
//         let zeros = bin.split('1').join('').length
//         return bin.length - zeros < zeros
//     }
//     return [...s].filter((v, i, a) => check(v) && a.indexOf(v) == i)
// }

// const moreZeros = s => [...new Set([...s].filter(c => (bin = c.charCodeAt().toString(2), bin.replace(/0/g, '').length < bin.replace(/1/g, '').length)))]
// const moreZeros = s => [...new Set([...s])].filter(n => n.charCodeAt().toString(2).split('0').length - (n.charCodeAt().toString(2).split('1').length) > 0);
const moreZeros = s => [...new Set([...s])].filter(c => (bin = c.charCodeAt().toString(2), bin.split('0').length > bin.split('1').length))


q = moreZeros('abcde') // ['a','b','d']
q
q = moreZeros('Great job!') // ['a', ' ', 'b', '!']
q
q = moreZeros('DIGEST') // ['D','I','E','T']
q
q = moreZeros('abcdeabcde') // ['a','b','d'],'Should not return duplicates values'
q