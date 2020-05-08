// 8kyu - Training JS #32: methods of Math---round() ceil() and floor()

// function roundIt(n) {
//     let s = String(n).split('.')
//     return s[0].length < s[1].length ? Math.ceil(n) : 
//            s[0].length > s[1].length ? Math.floor(n) :
//            Math.round(n)
// }

// function roundIt(n) {
//     [integer, fraction] = String(n).split('.')

//     return integer.length < fraction.length ? Math.ceil(n) :
//            integer.length > fraction.length ? Math.floor(n) :
//            Math.round(n)
// }

// const roundIt = n => Math[String(n).split('.')
//     .map(el => el.length)
//     .reduce((p, c, i, a) => a[i + 1] ? ((c < a[i + 1]) ?
//         'ceil' : (c > a[i + 1]) ? 'floor' : p) : p, 'round')](n)

// const roundIt = n => Math[['ceil', 'round', 'floor']
//     [String(n).split('.').map(x => x.length)
//         .reduce((a, v) => 1 + Math.sign(a - v))
//     ]](n)

const roundIt = n => Math[['ceil', 'round', 'floor'][String(n).split('.').map(x => x.length).reduce((a, v) => 1 + Math.sign(a - v))]](n)

q = roundIt(3.45) // 4
q
q = roundIt(34.5) // 34
q
q = roundIt(34.56) // 35
q