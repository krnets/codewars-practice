// 5kyu - Common Bit Twiddles

/* In this kata, we are throwing readablity to the wind and are refactoring simple functions to use Bit Twiddling.

###Specifications

The functions we will make are:

    isEven
    isOdd
    halfAndFloor
    isPowerOfTwo
    nthPowerOfTwo
    truncate (note: not in Haskell)
    abs

You are only allowed to use bitwise / boolean operators (and corresponding assignment operators): !, &&, ||, &, |, ^, ~, <<, >>, >>>, +, and -.

You should not use ?, :, *, /, %, if, else, for, while, do, switch, case, or the object Math.

###Code Examples

//All inputs are between + or - 2147483647

//Only receives whole numbers
isEven(2) // true
isEven(1) // false

//Only receives whole numbers
isOdd(2) // false
isOdd(1) // true

//Only receives positive whole numbers
halfAndFloor(10) // 5
halfAndFloor(11) // 5

//Only receives positive whole numbers
isPowerOfTwo(256) // true
nthPowerOfTwo(4) // 16

//Receives decimal numbers
truncate(1.1) // 1

//Receives negative / positive whole numbers
abs(-1) // 1

Refactoring | Utilities | Advanced Language Features | Fundamentals | Arithmetic | Mathematics | Algorithms | Numbers | Binary | Bits */

const isEven        = n => !(n & 1)
const isOdd         = n => !!(n & 1)
const halfAndFloor  = n => n >> 1
const isPowerOfTwo  = n => n > 0 && !(n & (n - 1))
const nthPowerOfTwo = n => 1 << n
const truncate      = n => ~~n
const abs           = n => (n ^ (n >> 31)) - (n >> 31)

function isEven(n) {
    // return n % 2 === 0
    return !(n & 1)
}
q = isEven(2) // true
q
q = isEven(1) // false
q
q = isEven(19) // false
q
q = isEven(8) // true
q
q = isEven(0) // true
q

function isOdd(n) {
    // return n % 2 !== 0
    return !!(n & 1)
}
q = isOdd(2) // false
q
q = isOdd(1) // true
q
q = isEven(19) // false
q
q = isEven(8) // true
q
q = isEven(0) // true
q

function halfAndFloor(n) {
    // return Math.floor(n / 2)
    // return ~~(n / 2)
    // return ~~(n >> 1)
    return n >> 1
}
q = halfAndFloor(10) // 5
q
q = halfAndFloor(11) // 5
q
q = halfAndFloor(33) // 16
q

function isPowerOfTwo(n) {
    // while (n >= 1 && n % 2 == 0)
    //     n = n / 2;
    // if (n == 1) return true
    // else return false
    // return n && !(n & (n - 1))
    return n > 0 && (n & (n - 1)) == 0
    // return !(n & (n - 1))
}
q = isPowerOfTwo(256) // true
q
q = isPowerOfTwo(3) // false
q
q = isPowerOfTwo(0) // 0
q

function nthPowerOfTwo(n) {
    // return Math.pow(2, n)
    return 1 << n
}
q = nthPowerOfTwo(2) // 4
q
q = nthPowerOfTwo(8) // 256
q
q = nthPowerOfTwo(11) // 2048
q

function truncate(n) {
    // if (n >= 0) return Math.floor(n)
    // else return Math.ceil(n)
    // return ~~n
    // return  n >> 0
    return n | 0
}
q = truncate(1.1) // 1
q
q = truncate(5.5) // 5
q
q = truncate(-5.5) // -5
q

function abs(n) {
    // return Math.abs(n)
    // return n < 0 ? -n : n
    return (n ^ (n >> 31)) - (n >> 31)
}
q = abs(-1) // 1
q
q = abs(1) // 1
q
q = abs(442014227)
q