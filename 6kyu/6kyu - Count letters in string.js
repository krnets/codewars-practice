// 6kyu - Count letters in string

const letterCount = s => [...s].reduce((dict, v) => (dict[v] = ++dict[v] || 1, dict), {})
// const letterCount = require('lodash/countBy');

q = letterCount("codewars")
// {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}
q
q = letterCount("activity")
// {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1}
q
q = letterCount("arithmetics")
// {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
q
q = letterCount("traveller")
// {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1}
q
q = letterCount("daydreamer")
// {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1}
q