// 6kyu - Find unique number

/* Give you a array arr that contains some numebers. 
Numbers can be positive,negative,integer or float. 
Only one of these numbers is unique. Find and return it.

Some examples:

 findUnique([1,2,3,5,7]) === 2
 Because only 2 is an even number, the other numbers are odd.

 findUnique([2,4,6,8,9]) === 9
 Because only 9 is an odd number

 findUnique([2,-4,6,8]) === -4
 Because only -4 is a negative number

 findUnique([-2,-4,-6,8]) === 8
 Because only 8 is a positive number

 findUnique([2,4.4,6,8]) === 4.4
 Because only 4.4 is a float number

 findUnique([2.2,4.4,6.6,8]) === 8
 Because only 8 is a integer number

 findUnique([2,2,2,4]) === 4
 Because only 4 has a diffrent value

Priority level: float/integer > positive/negative > odd/even > diffrent value

Some edge case:

 findUnique([-2,-4,-6.6,8]) === -6.6  //not 8
 Because Priority level float/integer > positive/negative

 findUnique([-2,-4,-7, 8]) === 8  //not -7
 Because Priority level positive/negative > odd/even

Note: All inputs will be an array. The array contains at least 3 element. 
Only one unique number in it. 0 will not appear, */

// function findUnique(arr) {
//     let floats = arr.filter(v => !Number.isInteger(v)).length
//     let integers = arr.filter(Number.isInteger).length
//     let positive = arr.filter(v => v > 0).length
//     let negative = arr.filter(v => v < 0).length
//     let evens = arr.filter(v => v % 2 == 0).length
//     let odds = arr.filter(v => v % 2 != 0).length

//     return floats == 1 ? arr.find(v => !Number.isInteger(v)) :
//         integers == 1 ? arr.find(Number.isInteger) :
//         positive == 1 ? arr.find(v => v > 0) :
//         negative == 1 ? arr.find(v => v < 0) :
//         odds == 1 ? arr.find(v => v % 2 != 0) :
//         evens == 1 ? arr.find(v => v % 2 == 0) :
//         arr.filter(v => arr.indexOf(v) == arr.lastIndexOf(v))[0]
// }

// function findUnique(arr) {
//     let floats = arr.filter(v => !Number.isInteger(v))
//     if (floats.length == 1)
//         return floats[0]

//     let integers = arr.filter(Number.isInteger)
//     if (integers.length == 1)
//         return integers[0]

//     let positive = arr.filter(v => v > 0)
//     if (positive.length == 1)
//         return positive[0]

//     let negative = arr.filter(v => v < 0)
//     if (negative.length == 1)
//         return negative[0]

//     let evens = arr.filter(v => v % 2 == 0)
//     if (evens.length == 1)
//         return evens[0]

//     let odds = arr.filter(v => v % 2 != 0)
//     if (odds.length == 1)
//         return odds[0]

//     return arr.filter(v => arr.indexOf(v) == arr.lastIndexOf(v))[0]
// }


// function findUnique(arr) {
//     let tests = [
//         n => n % 1 == 0,
//         n => n > 0,
//         n => Math.abs(n) % 2 == 1,
//         n => n == arr[0]
//     ]

//     for (let test of tests) {
//         let matches = arr.filter(test)

//         if (matches.length == 1)
//             return matches[0]

//         if (matches.length == arr.length - 1)
//             return arr.filter(n => !test(n))[0]
//     }
// }

function findUnique(arr) {
    let tests = [
        Number.isInteger,
        n => n > 0,
        n => Math.abs(n) % 2 == 1,
        n => n == arr[0]
    ]

    for (let test of tests) {
        let matches = arr.filter(test)

        if (matches.length == 1)
            return matches[0]

        if (matches.length == arr.length - 1)
            return arr.filter(n => !test(n))[0]
    }
}

q = findUnique([1, 2, 3, 5, 7]) // 2  <-- even number
q
q = findUnique([2, 4, 6, 8, 9]) // 9  <-- odd number
q
q = findUnique([2, -4, 6, 8]) // -4  <-- negative number
q
q = findUnique([-2, -4, -6, 8]) // 8  <-- positive number
q
q = findUnique([2, 4.4, 6, 8]) // 4.4  <-- float number
q
q = findUnique([2.2, 4.4, 6.6, 8]) // 8  <-- integer number
q
q = findUnique([2, 2, 2, 4]) // 4  <-- all same except one (different value)
q
q = findUnique([-2, -4, -6.6, 8]) // -6.6  <-- float number (amongst integers & negative/positive mix)
q
q = findUnique([-2, -4, -7, 8]) // 8  <-- positive number (others are negative)
q