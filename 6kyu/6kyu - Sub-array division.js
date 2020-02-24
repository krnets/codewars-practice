// 6kyu - Sub-array division

/* In this Kata, you will be given an array of numbers and a number n, and your task will be to determine 
if any array elements, when summed (or taken individually), are divisible by n.

For example:

    solve([1,3,4,7,6],9) == true, because 3 + 6 is divisible by 9
    solve([1,2,3,4,5],10) == true for similar reasons.
    solve([8,5,3,9],7) == true, because 7 evenly divides 5 + 9
    but solve([8,5,3],7) == false.

All numbers in the array will be greater than 0.  */

function solve(arr, n) {
    let subset = [0]
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0, len = subset.length; j < len; j++) {
            if ((subset[j] + arr[i]) % n == 0) {
                return true
            }
            subset.push(subset[j] + arr[i])
        }
    }
    return false
}

// function solve(xs, n) {
//     const rs = new Set();
//     for (const x of xs) {
//         for (const r of Array.from(rs))
//             rs.add((r + x) % n);
//         rs.add(x % n);
//     }
//     return rs.has(0);
// }

q = solve([1, 2, 3, 4, 5], 8) // true
q
q = solve([7, 2, 8, 5], 16) // false
q
q = solve([1, 2, 3, 4, 5], 10) // true
q
q = solve([3, 1, 5, 7], 14) // false
q
q = solve([1, 2, 3, 4, 5], 15) // true
q
q = solve([8, 5, 3, 9], 7) // true
q
q = solve([8, 5, 3], 7) // false
q
q = solve([8, 1, 2, 7], 12) // false
q
q = solve([2, 6, 3], 9) // true
q
q = solve([7, 2, 3, 1, 6, 5], 11) // true
q
q = solve([5, 6, 4, 8, 1], 12) // true
q