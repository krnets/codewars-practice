// 7kyu - Sort array by string length

const sortByLength = array => array.sort((a, b) => a.length - b.length)


q = sortByLength(["Beg", "Life", "I", "To"])
// ["I", "To", "Beg", "Life"]
q
q = sortByLength(["", "Moderately", "Brains", "Pizza"])
// ["", "Pizza", "Brains", "Moderately"]
q
q = sortByLength(["Longer", "Longest", "Short"])
// ["Short", "Longer", "Longest"]
q