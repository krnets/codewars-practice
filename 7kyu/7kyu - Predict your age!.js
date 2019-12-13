// 7kyu - Predict your age!

/* Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two. */

// function predictAge(age1, age2, age3, age4, age5, age6, age7, age8) {
//     let args = [...arguments]
//     return ~~(Math.sqrt(args.map(v => v * v).reduce((a, b) => a + b)) / 2)
// }

// function predictAge(age1, age2, age3, age4, age5, age6, age7, age8) {
//     return ~~(Math.hypot(...arguments) / 2)
// }

const predictAge = (...ages) => Math.hypot(...ages) / 2 | 0

q = predictAge(65, 60, 75, 55, 60, 63, 64, 45) // 86
q