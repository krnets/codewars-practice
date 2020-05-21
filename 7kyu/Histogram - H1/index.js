var expected =
    `6|##### 5
    5|
    4|# 1
    3|########## 10
    2|### 3
    1|####### 7
  `

// function histogram(results) {
//     let output = ''
//     let a = results.length

//     while (a > 0) {
//         output += `${a}|`
//         for (let j = 0; j < results[a - 1]; j++) {
//             output += '#'
//         }
//         if (results[a - 1] != 0) {
//             output += ` ${results[a-1]}`
//         }
//         output += '\n'
//         a--
//     }
//     return output;
// }

// function histogram(results) {
//     let output = ''
//     for (let i = results.length; i > 0; --i) {
//         output += i + '|' + '#'.repeat(results[i - 1]) + (results[i - 1] > 0 ? ' ' + results[i - 1] : '') + '\n'
//     }
//     return output
// }

// function histogram(results) {
//     let output = ''
//     for (let i = results.length; i > 0; i--)
//         output += i + '|' + '#'.repeat(results[i - 1]) +
//             (results[i - 1] > 0 ? ' ' + results[i - 1] : '') + '\n'
//     return output
// }

// const histogram = r => r.reduce((r, x, i) => (i+1)+'|'+(x ? '#'.repeat(x)+' '+x : '')+'\n'+r, '')

const histogram = results => results
    .reduce((accum, current, index) =>
        (index + 1) + '|' + (current ? '#'.repeat(current) + ' ' + current : '') + '\n' + accum, '')

// const histogram = results => results
//         .reduceRight((accum, x, index) =>
//             `${accum}${index + 1}|${'#'.repeat(x)}${x ?
//             ` ${x}` : ''}\n`, '');



q = histogram([7, 3, 10, 1, 0, 5])
q