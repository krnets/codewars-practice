// 7kyu - Odd-Even String Sort

// const sortMyString = S => [...S].filter((_, i) => i % 2 == 0).join `` + ` ` + [...S].filter((_, i) => i % 2).join ``
// const sortMyString = S => [...S].filter((_, i) => i % 2 == 0).concat(' ', [...S].filter((_, i) => i % 2)).join ``
// const sortMyString = S => [...S.split ``.filter((_, i) => !(i % 2)), ` `, ...S.split ``.filter((_, i) => i % 2)].join ``
const sortMyString = S => S.replace(/(.)./g, '$1') + ' ' + S.replace(/.(.)?/g, '$1')

// function sortMyString(s) {
//     [a, b] = [...s].reduce((acc, c, i) => (i % 2 ? acc[1].push(c) : acc[0].push(c), acc), [[],[]])
//     return a.join`` + ` ` + b.join``
// }

q = sortMyString("CodeWars") // "CdWr oeas"
q
q = sortMyString("YCOLUE'VREER") // "YOU'RE CLEVER"); 
q