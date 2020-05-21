// const solve = s => +s.split(/\D/).sort((a, b) => a - b).slice(-1)
// const solve = s => Math.max(s.split(/\D/))
// const solve = s => s.split(/\D/).sort((a, b) => b - a)[0]
// const solve = s => Math.max(...s.match(/\d+/g))
const solve = s => Math.max(...s.match(/\d+|$/g))

q = solve('gh12cdy695m1') // 695
q
q = solve('2ti9iei7qhr5') // 9
q
q = solve('vih61w8oohj5') // 61
q
q = solve('f7g42g16hcu5') // 42
q
q = solve('lu1j8qbbb85') // 85
q