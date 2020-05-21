// 6kyu - Your order, please

/* Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers. */

// function order(words) {
//     let w = words.split(' ')
//     let i = w.map(v => +(v.replace(/\D+/g, '')))
//     let zip = (...rows) => rows[0].map((_, c) => rows.map(row => row[c]))

//     return zip(w, i).sort((a, b) => a[1] - b[1]).map(v => v[0]).join ` `
// }

// const order = words => words.split(' ').sort((a, b) => a[a.search(/\d/)] - b[b.search(/\d/)]).join ` `
// const order = words => words.split(' ').sort((a, b) => a.match(/\d/) - b.match(/\d/)).join ` `
// const order = words => words.split(' ').sort((a, b) => /\d/.exec(a) - /\d/.exec(b)).join ` `

const order = words => words.split ` `.sort((a, b) => /\d/.exec(a) - /\d/.exec(b)).join ` `

q = order("is2 Thi1s T4est 3a") // "Thi1s is2 3a T4est"
q
q = order("4of Fo1r pe6ople g3ood th5e the2") // "Fo1r the2 g3ood 4of th5e pe6ople"
q
q = order("") // ""
q