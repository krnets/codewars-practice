// 7kyu - Consecutive letters

// const solve = s => [...s].sort().filter((v, i, a) => a.indexOf(v) != i).length > 0 ? false : 
//                    [...s].sort().map(v => v.charCodeAt()).map((v, i, a) => v + 1 == a[i + 1]).filter(v => !v).length < 2

const solve = s => [...s].sort().every((v, i, a) => i == 0 || v.charCodeAt() - a[i-1].charCodeAt() == 1)

// const solve = s => 'abcdefghijklmnopqrstuvwxyz'.includes([...s].sort().join(''))

q = solve("abc") // true
q
q = solve("abd") // false
q
q = solve("dabc") // true
q
q = solve("abbc") // false
q