// 6kyu - Replace With Alphabet Position

// const alphabetPosition = text => [...text.replace(/\s|\'|\./g, '').toLowerCase()].map(c => c.charCodeAt() - 96).join ` `
// const alphabetPosition = text => [...text.replace(/\W/g, '').toLowerCase()].map(c => c.charCodeAt() - 96).join ` `
// const alphabetPosition = text => [...text.replace(/[^a-z]/gi, '').toLowerCase()].map(c => c.charCodeAt() - 96).join``
// const alphabetPosition = text => !!text && text.match(/[a-zA-Z]/g).map(c => c.toLowerCase().charCodeAt() - 96).join ` `
// const alphabetPosition = text => (text.match(/[a-z]/gi) || []).map(c => c.toLowerCase().charCodeAt() - 96).join ` `
const alphabetPosition = text => (text.toLowerCase().match(/[a-z]/g) || []).map(c => c.charCodeAt() - 96).join ` `

q = alphabetPosition("The sunset sets at twelve o' clock.")
q
// "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
q = alphabetPosition("The narwhal bacons at midnight.")
// "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
q