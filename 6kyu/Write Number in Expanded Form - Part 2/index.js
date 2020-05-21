// 6kyu - Write Number in Expanded Form - Part 2

/* This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(1.24); // should return '1 + 2/10 + 4/100'
expandedForm(7.304); // should return '7 + 3/10 + 4/1000'
expandedForm(0.04); // should return '4/100'         */

// function expandedForm(num) {
//     let arr = String(num).split('.')
//     let int = [...arr[0]].reverse().map((n, i) => n == 0 ? '' : n + '0'.repeat(i)).filter(Boolean).reverse().join(' + ')
//     let dec = [...arr[1]].map((n, i) => n > 0 ? n + '/' + Math.pow(10, i + 1) : '').filter(Boolean).join(' + ')
//     return [int, dec].join(' + ').replace(/^[^0-9]+/, '')
// }

// function expandedForm(num) {
//     let arr = String(num).split('.')
//     let int = [...arr[0]].reverse().map((n, i) => n > 0 ? n + '0'.repeat(i) : '').filter(Boolean).reverse()
//     let dec = [...arr[1]].map((n, i) => n > 0 ? n + '/' + Math.pow(10, i + 1) : '').filter(Boolean)
//     return int.concat(dec).join(' + ')
// }

// function expandedForm(num) {
//     let parts = String(num).split('.')
//     let integer = [...parts[0]].reverse().map((n, i) => n * Math.pow(10, i)).filter(Boolean).reverse()
//     let decimal = [...parts[1]].map((n, i) => n > 0 ? n + '/' + Math.pow(10, i + 1) : '').filter(Boolean)
//     return integer.concat(decimal).join(' + ')
// }


function expandedForm(num) {
    let parts = String(num).split('.')
    let integer = [...parts[0]].reverse().map((n, i) => n * Math.pow(10, i)).reverse()
    let decimal = [...parts[1]].map((n, i) => n > 0 ? n + '/' + Math.pow(10, i + 1) : '')
    return integer.concat(decimal).filter(Boolean).join(' + ')
}


q = expandedForm(1.24) // '1 + 2/10 + 4/100'
q
q = expandedForm(4.28) // '4 + 2/10 + 8/100'
q
q = expandedForm(7.304) // '7 + 3/10 + 4/1000'
q
q = expandedForm(90.304) // '90 + 3/10 + 4/1000'
q
q = expandedForm(91800.304) // '90000 + 1000 + 800 + 3/10 + 4/1000'
q