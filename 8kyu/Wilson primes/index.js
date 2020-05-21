/* CODEWARS: 8 kyu - Wilson primes
Wilson primes satisfy the following condition. 
Let P represent a prime number.

Then ((P-1)! + 1) / (P * P) should give a whole number.

Your task is to create a function that returns true if the given number is a Wilson prime. */

// const isPrime = num => {
//   const boundary = Math.floor(Math.sqrt(num));
//   for (var i = 2; i <= boundary; i++) if (num % i === 0) return false;
//   return num >= 2;
// }

function amIWilson(p) {
    // const isPrime = n => { 
    //     let boundary = Math.floor(Math.sqrt(n));
    //     for (let i = 2; i < boundary; i++) 
    //         if (n % i == 0) return false
    //     return n >= 2 }

    const factorial = n => n <= 0 ? 1 : n * factorial(n - 1)

    // return isPrime(p) ? Number.isInteger((factorial(p -1) + 1) / (p * p)) : false
    return  Number.isInteger((factorial(p -1) + 1) / (p * p)) 
}

// const = (fn, bool) // => fn == bool

q = amIWilson(5) //, true)
q
q = amIWilson(9) //, false)
q
q = amIWilson(6) //, false)
q
q = amIWilson(8) //, false)
q