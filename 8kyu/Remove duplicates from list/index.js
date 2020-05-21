// 8kyu - Remove duplicates from list

// const distinct = a => a.filter((v, i) => a.indexOf(v) == i)

const distinct = a => [...new Set(a)]

// const {uniq: distinct} = require('lodash')

// const distinct = a => a.reduce((a, c) => a.includes(c) ? a : [...a, c], [])

// const distinct = a => a.reduce((uniq, curr) => uniq.includes(curr) ? uniq : [...uniq, curr], [])

// const distinct = a => a.reduce((m, x) => {
//     if (m.indexOf(x) === -1) m.push(x);
//     return m
// }, [])


q = distinct([1]) // [1]
q
q = distinct([1, 2]) // [1,2]
q
q = distinct([1, 1, 2]) // [1,2]
q