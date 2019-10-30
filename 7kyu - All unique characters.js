// 7kyu - All unique characters

// const hasUniqueChars = str => [...str].filter((v, i) => str.indexOf(v) == i).length == str.length
// const hasUniqueChars = str => new Set(str).size == str.length
// const hasUniqueChars = str => [...str].every((v, i, a) => a.indexOf(v) == i)
const hasUniqueChars = str => !str.match(/([^])[^]*\1/)
// const hasUniqueChars = str => !/(.).*\1/.test(str)
// const hasUniqueChars = str => !/(.)\1/.test(str.split``.sort().join``)

q = hasUniqueChars("  nAa") // false
q
q = hasUniqueChars("abcdef") // true
q
q = hasUniqueChars("++-") // false
q