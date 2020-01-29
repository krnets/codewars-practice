// 7kyu - Remove consecutive duplicate words

// function removeConsecutiveDuplicates(s) {
//     let arr = s.split(' ')
//     for (var res = '', i = 0; i < arr.length; i++)
//         if (arr[i] != arr[i+1])
//             res += arr[i] + ' '
//     return res.trim()
// }

// const removeConsecutiveDuplicates = (s) => s.split(' ').filter((v, i, arr) => v != arr[i-1]).join(' ')
// const removeConsecutiveDuplicates = (s) => s.replace(/\b(\w+)(?: \1)+\b/g, '$1')
const removeConsecutiveDuplicates = (s) => s.replace(/(\b\w+)( \1\b)+/g, '$1')
// const removeConsecutiveDuplicates = (s) => s.replace(/(?<=(\w+)) \1\b/g, '')



q = removeConsecutiveDuplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')
q
//  'alpha beta gamma delta alpha beta gamma delta'