// 7kyu - All Inclusive?

/* Input:

    a string strng
    an array of strings arr

Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

    a boolean true if all rotations of strng are included in arr (C returns 1)
    false otherwise (C returns 0)

Examples:

contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)

Note:

Though not correct in a mathematical sense

    we will consider that there are no rotations of strng == ""
    and for any array arr: contain_all_rots("", arr) --> true

Ref: https://en.wikipedia.org/wiki/String_(computer_science)#Rotations */

// function containAllRots(strng, arr) {
//     let rotate = (s, n) => s.slice(n) + s.slice(0, n)
//     return Array(strng.length).fill().map((_, i) => rotate(strng, i)).every(v => arr.includes(v))
// }

// const containAllRots = (s, a) => [...s].map((_, i) => s.slice(i) + s.slice(0, i)).every(v => a.includes(v))
const containAllRots = (s, a) => [...s].every((_, i) => a.includes((s + s).substr(i, s.length)))

q = containAllRots("", []) // true
q
q = containAllRots("", ["bsjq", "qbsj"]) // true
q
q = containAllRots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) // true
q
q = containAllRots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]) // false
q