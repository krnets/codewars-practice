// Beta - Add numbers

/* Simple mission:

add() gets anywhere between 0 and 100 arguments (Integers) and returns their sum.

Examples

add() = 0
add(2) = 2
add(1, 1) = 2
add(1, 2, 3) = 6
add(-3, -2, -1, 1, 2, 3, 4) = 4    */

const add = (...xs) => xs.reduce((a, b) => a + b, 0)

// const add = (...xs) => eval(xs.join('+')) || 0
// const add = (...xs) => eval(xs.join `+`) || 0

q = add() // 0
q
q = add(2) // 2
q
q = add(1, 1) // 2
q
q = add(1, 2, 3) // 6
q
q = add(-3, -2, -1, 1, 2, 3, 4) // 4
q