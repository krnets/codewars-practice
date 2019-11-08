// 7kyu - Sum of digits

// const sum = (digits) => digits == '0' ? '0 = 0' : !digits ? '' : 
//             [...String(digits)].join(' + ') + ' = ' + [...String(digits)].reduce((a, b) => a + Number(b), 0)

const sum = (digits) => digits == undefined ? '' : [...String(digits)].join(' + ') + ' = ' + [...String(digits)].reduce((a, b) => a + Number(b), 0)

// const sum = d => d === undefined ? '' : `${[...String(d)].join(' + ')} = ${[...String(d)].reduce((a, c) => a + +c, 0)}`

q = sum("3433") // "3 + 4 + 3 + 3 = 13"
q
q = sum("64323") // "6 + 4 + 3 + 2 + 3 = 18"
q
q = sum("8") // "8 = 8"
q