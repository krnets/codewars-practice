// 7kyu - Ordered Count of Characters

// Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

const orderedCount = (text) => [...new Set(text)].map(c => [c, text.split(c).length - 1])

q = orderedCount("abracadabra") // [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]]
q
q = orderedCount("Code Wars") // [['C', 1], ['o', 1], ['d', 1], ['e', 1], [' ', 1], ['W', 1], ['a', 1], ['r', 1], ['s', 1]]
q
q = orderedCount("212") // [['2', 2], ['1', 1 ]]]
q