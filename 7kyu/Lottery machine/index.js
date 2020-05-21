// 7kyu - Lottery machine

/* Your task is to write an update for a lottery machine. 
Its current version produces a sequence of random letters and integers (passed as a string to the function). 
Your code must filter out all letters and return unique integers as a string, in their order of first appearance. 
If there are no integers in the string return "One more run!"

"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5" */

// const lottery = (str) => [...str].filter((v, i, a) => /\d/.test(v) && a.indexOf(v) == i).join('') || 'One more run!'
// const lottery = (str) => [...str].filter((v, i, a) => /\d/.test(v) && a.indexOf(v) == i).join('') || 'One more run!'
// const lottery = str => (str.match(/(\d)/g) || []).filter((v, i, a) => a.indexOf(v) == i).join('') || 'One more run!'

// const lottery = (str) => [...new Set(str.replace(/\D/g, ''))].join('') || 'One more run!'

const lottery = str => [...new Set(str.match(/\d/g))].join('') || 'One more run!'

q = lottery("wQ8Hy0y5m5oshQPeRCkG") // "805", "should return unique integer(s) or a string"
q
q = lottery("ffaQtaRFKeGIIBIcSJtg") // "One more run!", "should return unique integer(s) or a string"
q