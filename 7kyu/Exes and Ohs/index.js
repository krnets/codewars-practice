// 7kyu - Exes and Ohs

// function XO (str) { 
//     let xCount = [...str].filter(v => v.toLowerCase() == 'x').length
//     let yCount = [...str].filter(v => v.toLowerCase() == 'o').length
//     return xCount - yCount == 0
// }

const XO = str => (str.match(/x/gi) || []).length == (str.match(/o/gi) || []).length

q = XO('xo') // true
q
q = XO("xxOo") // true
q
q = XO("xxxm") // false
q
q = XO("Oo") // false
q
q = XO("ooom") // false
q