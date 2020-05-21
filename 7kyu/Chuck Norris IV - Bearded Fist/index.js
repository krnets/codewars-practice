// 7kyu - Chuck Norris IV - Bearded Fist

// const fistBeard = (arr) => arr.reduce((a, b) => a.concat(b)).map(v => String.fromCharCode(v)).join('')
// const fistBeard = arr => String.fromCharCode(...arr.reduce((a, b) => a.concat(b)));
const fistBeard = arr => String.fromCharCode(...[].concat(...arr))

q = fistBeard([[78], [117, 110, 99], [104, 117], [107, 115]]), 'Nunchuks'
q
q = fistBeard([[70, 97, 99], [101, 45, 75, 105, 99, 107]]), 'Face-Kick'
q