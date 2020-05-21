// function automorphic(n) {
//     let numLength = String(n).length
//     let square = String(n * n)
//     let squareLength = square.length

//     return square.slice(-numLength) == String(n).slice(-numLength) ?
//         'Automorphic' : 'Not!!'
// }

const automorphic = n => String(n * n).endsWith(String(n)) ? 'Automorphic' : 'Not!!';
// const automorphic = n => Math.pow(n, 2).toString().endsWith(n.toString()) ? 'Automorphic' : 'Not!!'

q = automorphic(1) //,"Automorphic"
q
q = automorphic(3) //,"Not!!"
q
q = automorphic(7) //,"Not!!"
q
q = automorphic(6) //,"Automorphic"
q
q = automorphic(9) //,"Not!!"
q
q = automorphic(25) //,"Automorphic"
q
q = automorphic(53) //,"Not!!"
q
q = automorphic(76) //,"Automorphic"
q
q = automorphic(95) //,"Not!!"
q
q = automorphic(625) //,"Automorphic"
q
q = automorphic(225) //,"Not!!"
q