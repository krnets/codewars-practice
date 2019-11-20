// 6kyu - Check if number is prime without loops

// const isPrime = str => /prime/i.test(str) || (str.match(/\d+/g) || []).some(n =>
//     n > 1 && [...Array(n - 2)].every((_, i) => n % (i + 2)))

// const isPrime = str => /prime/i.test(str) || (str.match(/\d+/g) || []).some(x =>
//     +x > 1 && [...Array(+x)].every((_, p) => p < 2 || x % p))

// const isPrime = n => Array.from({length: Math.abs(n)}, (_, i) => i).every((_, p) => p < 2 || n % p)
// const isPrime = n => Array(Math.abs(n)).fill().map((_, i) => i + 2).every((_, p) => p < 2 || n % p)
// const isPrime = n => Math.abs(n) == 2 || Array(Math.abs(n)).fill().map((_, i) => i + 2).every((_, p) => p < 2 || n % p)

// const isPrime = n => ![...Array(Math.abs(n)).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)
// const isPrime = n => ![...Array(Math.abs(n)).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)

// const isPrime = n => (n = Math.abs(n)) > 1 && Array.from({length: n - 2}, (_, i) => n % (i + 2) != 0).every(Boolean);
// const isPrime = n => (n = Math.abs(n)) > 1 && Array.from({ length: Math.sqrt(n) - 1 | 0 }, (x, i) => i + 2).every(x => n % x);
const isPrime = n => (n = Math.abs(n)) > 1 && Array(n).fill().map((_, i) => i + 2).every((_, p) => p < 2 || n % p)



q = isPrime(9) // false
q
q = isPrime(-7) // true
q
q = isPrime(7) // true
q