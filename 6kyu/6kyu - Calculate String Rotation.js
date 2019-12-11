// 6kyu - Calculate String Rotation

/* Write a function that receives two strings and returns n, where n is equal to the number of characters we should 
shift the first string forward to match the second.

For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 
5 characters forward to produce the second string, so 5 would be returned.

If the second string isn't a valid rotation of the first string, the method returns -1. */

// function shiftedDiff(first, second) {
//     for (let i = 0; i < first.length; i++)
//         if (second == first.slice(-i) + first.slice(0, -i))
//             return i
//     return -1
// }

const shiftedDiff = (first, second) => first.length == second.length ? (second + second).indexOf(first) : -1

q = shiftedDiff("coffee", "eecoff") // 2
q
q = shiftedDiff("eecoff", "coffee") // 4
q
q = shiftedDiff("Moose", "moose") // -1
q
q = shiftedDiff("isn't", "'tisn") // 2
q
q = shiftedDiff("Esham", "Esham") // 0
q
q = shiftedDiff(" ", " ") // 0
q
q = shiftedDiff("  ", " ") // -1
q