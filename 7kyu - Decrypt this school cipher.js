// 7kyu - Decrypt this school cipher

// const decrypt = str => str.match(/''/) ? 
//                 str.split('\'').filter(v=> v).map((v=> String.fromCharCode(v))).reverse().join ``: 
//                 str.split(' ').reverse().map((v=>v.split('').reverse().join``)).join` `

// const decrypt = str => [...str.replace(/'(\d+)'/g, (_,d) => String.fromCharCode(d))].reverse().join``
// const decrypt = str => str.replace(/'(\d+)'/g, (_, x) => String.fromCharCode(x)).split ``.reverse ``.join ``
const decrypt = str => str.replace(/'(.+?)'/g, (_, x) => String.fromCharCode(x)).split ``.reverse ``.join ``

q = decrypt("'101''99''105''108''65'") // "Alice"
q
q = decrypt("'98''111''66'") // "Bob"
q
q = decrypt("30 71") // "17 03"
q