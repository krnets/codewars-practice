// 6kyu - WeIrD StRiNg CaSe

/* Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, 
and returns the same string with all even indexed characters in each word upper cased, 
and all odd indexed characters in each word lower cased. The indexing just explained is 
zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). 
Spaces will only be present if there are multiple words. 
Words will be separated by a single space(' '). */

function toWeirdCase(string) {
    return string.split(' ').map(v => [...v].map((w, i, a) => i % 2 ? w.toLowerCase() : w.toUpperCase()).join ``).join ` `
}

// const toWeirdCase = string => string.split(' ').map(w => [...w].map((v, i) => i % 2 ? v.toLowerCase() : v.toUpperCase()).join ``).join ` `
// const toWeirdCase = string => string.split ` `.map(w => [...w].map((v, i) => v['to' + (i % 2 ? 'Lower' : 'Upper') + 'Case']()).join ``).join ` `

// const toWeirdCase = string => string.replace(/(\w{1,2})/g, v => v[0].toUpperCase() + v.slice(1))
// const toWeirdCase = string => string.replace(/(\w{1,2})/g, v => v.length == 1 ? v[0].toUpperCase() : v[0].toUpperCase() + v[1].toLowerCase())


q = toWeirdCase('This') // 'ThIs'
q
q = toWeirdCase('is') // 'Is'
q
q = toWeirdCase('This is a test') // 'ThIs Is A TeSt'
q