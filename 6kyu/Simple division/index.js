// 6kyu - Simple division

/* In this Kata, you will be given two numbers, a and b, and your task is 
to determine if the first number a is divisible by all the prime factors of the second number b. 

For example: solve(15,12) = False because 15 is not divisible by all the prime factors of 12 (which include 2). */


// function solve(a, b) {
//     if (a <= 2) return b % a == 0
//     let strA = String(a)
//     if (strA == String(b).slice(0, strA.length) && [...strA].reverse()[0] != 0)
//         return false
//     if ((a % 2 == 0 && b % 2 == 0) || (a % 2 != 0 && b % 2 != 0))
//         return true
//     return false
// }

function solve(a, b) {
    function gcd(a, b) {
        while (b)
            [a, b] = [b, a % b];
        return a;
    }
    for (let c;
        (c = gcd(a, b)) > 1;)
        b /= c;
    return b == 1;
}

// function solve(a, b) {
//     for (let i = 2; i <= a && i <= b && b !== 1; i++) {
//         if (a % i || b % i)
//             continue;
//         while (a % i === 0)
//             a = a / i;
//         while (b % i === 0)
//             b = b / i;
//     }
//     return b === 1;
// }

// function isPrime(num) {
//     for (let i = 2; i <= Math.sqrt(num); i++)
//         if (num % i == 0) return false
//     return num >= 2
// }

// function findPrimeFactors(num) {
//     let primes = []
//     if (isPrime(num)) primes.push(num)
//     for (let i = 0; i <= Math.sqrt(num); i++)
//         if (isPrime(i) && num % i == 0) primes.push(i)
//     return primes
// }

// function solve(a, b) {
//     let primes = findPrimeFactors(b)
//     for (let i = 0; i < primes.length; i++)
//         if (a % primes[i] !== 0)
//             return false
//     return true
// }

q = solve(2, 256) // true
q
q = solve(2, 253) // false
q
q = solve(9, 243) // true
q
q = solve(15, 12) // false
q
q = solve(21, 2893401) // true
q
q = solve(21, 2893406) // false
q
q = solve(54, 2834352) // true
q
q = solve(54, 2834359) // false
q
q = solve(1000013, 7187761) // true
q
q = solve(1000013, 7187762) // false
q