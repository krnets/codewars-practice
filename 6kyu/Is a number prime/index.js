// 6kyu - Is a number prime?

// Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.

function isPrime(n) {
    for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++)
        if (n % i == 0) return false
    return n >= 2
}

// const isPrime = n => n < 2 ? false : !/^(11+?)\1+$/.test(Array(n + 1).join('1'))

// function isPrime(num) {
//     let sieve = [2, 3, 5, 7]
//     return num > 2 && sieve.reduce((prev, n) => prev && num % n != 0, true) || sieve.indexOf(num) != -1
// }

q = isPrime(0) //  false, "0 is not prime"
q
q = isPrime(1) //  false, "1 is not prime"
q
q = isPrime(2) //  true, "2 is prime"
q
q = isPrime(73) // true, "73 is prime"
q
q = isPrime(75) // false, "75 is not prime"
q
q = isPrime(-1) // false, "-1 is not prime"
q
q = isPrime(3) //  true, "3 is prime"
q
q = isPrime(5) //  true, "5 is prime"
q
q = isPrime(7) //  true, "7 is prime"
q
q = isPrime(41) // true, "41 is prime"
q
q = isPrime(5099) // true, "5099 is prime"
q
q = isPrime(4) //  false, "4 is not prime"
q
q = isPrime(6) //  false, "6 is not prime"
q
q = isPrime(8) //  false, "8 is not prime"
q
q = isPrime(9) // false, "9 is not prime"
q
q = isPrime(45) // false, "45 is not prime"
q
q = isPrime(-5) // false, "-5 is not prime"
q
q = isPrime(-8) // false, "-8 is not prime"
q
q = isPrime(-41) // false, "-41 is not prime"
q