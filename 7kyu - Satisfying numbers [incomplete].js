// 7kyu - Satisfying numbers

/* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Write smallest(n) that will find the smallest positive number that is evenly divisible by all of the numbers from 1 to n (n <= 40).
smallest(5) == 60 // 1 to 5 can all divide evenly into 60
smallest(10) == 2520 */

function smallest(n) {
    let a = Array(40).fill().map((_, i) => i + 1)
    a
    let b = n % a[4]
    b
    let found = 0
    let temp = 0

    // number to be divided by each array n from 1..N
    // as soon as number no longer divides without remainder
    // return last max number
    // i = 1 2 3 4 5 6 7 8 9 10
    //     ^
    // j = 1 2 3 4 5 6 7 8 9 10
    //     ^

    for (var i = 1; i > 0; i++) {
        i
        for (var j = 1; j < i; j++) {
            j
            temp = i % j
            temp
            if (temp != 0) {
                i
                return i
            }
        }
    }
}
// 58 59 60 61
// P

// q = smallest(1) // 1
// q
// q = smallest(2) // 2
// q
// q = smallest(3) // 6
// q
// q = smallest(4) // 12
// q
// q = smallest(5) // 60
// q
q = smallest(6) // 60
q
// q = smallest(7) // 420
// q
// q = smallest(8) // 840
// q
// q = smallest(9) // 2520
// q