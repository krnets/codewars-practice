// 6kyu - Sum of prime-indexed elements

/* In this Kata, you will be trained on array indexing and basic prime number operations. 
Array indices are zero-based; this means that the first element of an array is at index 0.

You will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

To make this interesting, array lengths in random tests will have up to 5000 elements. */

function isPrime(num) {
    for (var i = 2; i <= Math.sqrt(num); i++)
        if (num % i == 0) return false
    return num >= 2
}

function total(arr) {
    for (var sum = 0, i = 0; i < arr.length; i++)
        if (isPrime(i)) sum += arr[i]
    return sum
}

// const isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)
// const isPrime = n => n < 2 ? false : n == 2 ? true : [...Array(~~(Math.sqrt(n))).keys()].every(x => n % (x + 2))
// const total = arr => arr.reduce((sum, v, i) => sum + (isPrime(i) ? v : 0), 0)

q = total([]) // 0
q
q = total([1, 2, 3, 4]) // 7
q
q = total([1, 2, 3, 4, 5, 6]) // 13
q
q = total([1, 2, 3, 4, 5, 6, 7, 8]) // 21
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) // 21
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) // 33
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) // 47
q