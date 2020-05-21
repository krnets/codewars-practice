// 7kyu - Digits explosion

// Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

// const explode = (s) => [...s].filter(Number).map(v => v.repeat(v)).join('')
// const explode = (s) => [...s].map(v => v.repeat(v)).join('')
const explode = (s) => s.replace(/\d/g, n => n.repeat(n))

q = explode("312") // "333122"
q
q = explode("102269") // "12222666666999999999"
q
q = explode("0") // ""
q
q = explode("000") // ""
q
q = explode("123") // "122333"
q