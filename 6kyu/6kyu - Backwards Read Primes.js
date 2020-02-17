// 6kyu - Backwards Read Primes

/* Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime. 
(This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes

13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

Find all Backwards Read Primes between two positive given numbers (both inclusive), 
the second one always being greater than or equal to the first one. 
The resulting array or the resulting string will be ordered following the natural order of the prime numbers. */


const isPrime = num => {
    for (let i = 2; i <= ~~(Math.sqrt(num)); i++)
        if (num % i === 0) return false
    return num >= 2
}

const isBackwardsReadPrime = num => isPrime([...String(num)].reverse().join('') * 1)

const isPalindrome = x => [...String(x)].reverse().join('') == x

const backwardsPrime = (start, stop) => Array(stop - start + 1).fill()
    .map((_, i) => i + start)
    .filter(v => isPrime(v) && isBackwardsReadPrime(v) && !isPalindrome(v))

q = backwardsPrime(1, 20) // []
q
q = backwardsPrime(501, 599) // []
q
q = backwardsPrime(2, 100) // [13, 17, 31, 37, 71, 73, 79, 97] 
q
q = backwardsPrime(9900, 10000) // [9923, 9931, 9941, 9967] 
q