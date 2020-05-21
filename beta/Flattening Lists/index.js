// Beta - Flattening Lists

/* In this Kata you will create a function that takes a list of lists as an input and returns a flattened list.

Note that if there are more lists inside these lists, they should not be flattened. */

// const flatten = (l) => l.reduce((a, b) => a.concat(b), [])

const flatten = (l) => [].concat(...l)

q = flatten([[1,2],[3,4]]) // [1,2,3,4]
q
q = flatten([[1],[2],[3],[4]]) // [1,2,3,4]
q