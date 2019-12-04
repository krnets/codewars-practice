// 6kyu - Prefill an Array

/* Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.
You have to validate input:
    v can be anything (primitive or otherwise)
    if v is ommited, fill the array with undefined
    if n is 0, return an empty array
    if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.
    prefill(3,1) --> [1,1,1]
    prefill(2,"abc") --> ['abc','abc']
    prefill("1", 1) --> [1]
    prefill(3, prefill(2,'2d')) --> [['2d','2d'],['2d','2d'],['2d','2d']]
    prefill("xyz", 1) --> throws TypeError with message "xyz is invalid"
Fundamentals | Validation | Algorithms | Basic Language Features | Arrays | Control Flow | Utilities */

// function prefill(n, v) {
//     if (parseInt(n) !== Math.abs(n))
//         throw new TypeError(`${n} is invalid`)
//     return Array(+n).fill(v)
// }

function prefill(n, v) {
    if (!/^\d+$/.test('' + n))
        throw new TypeError(n + " is invalid")
    return Array(+n).fill(v)
}

q = prefill(0, 1) // []
q
q = prefill(3, 1) // [1,1,1]
q
q = prefill(2, 'abc') // ['abc','abc']
q
q = prefill('1', 1) // [1]
q
q = prefill(3, prefill(2, '2d')) // [['2d','2d'],['2d','2d'],['2d','2d']]
q
q = prefill("xyz", 1) // --> throws TypeError with message "xyz is invalid"
q
q = prefill(Infinity, 2)
q
q = prefill(-Infinity, 2)
q
q = prefill(NaN, 2)
q
q = prefill('4.568972280019345', 2)
q
q = prefill('-1', 2)
q
q = prefill('de02r', 2)
q
q = prefill(true, 2)
q
q = prefill(false, 2)
q