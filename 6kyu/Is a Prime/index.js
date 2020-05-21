// 6kyu - Is a Prime?

// const checkPrime = n => n < 2 ? false : !/^(11+?)\1+$/.test(Array(n + 1).join('1'))

// const isPrime = str => (str.match(/prime/gi) || []).length > 0 ? true :
//     (str.match(/\d+/g) || [])
//     .map(v => !/^(11+?)\1+$/
//         .test(Array(+v + 1).join('1')))
//     .filter(v => v).length > 0

// const isPrime = str => /prime/i.test(str) || (str.match(/\d+/g) || []).some(n =>
//     n > 1 && [...Array(n - 2)].every((_, i) => n % (i + 2)))

// const isPrime = str => /prime/i.test(str) || (str.match(/\d+/g) || []).some(x =>
//     +x > 1 && [...Array(+x)].every((_, p) => p < 2 || x % p))

const isPrime = str => /prime/i.test(str) || (str.match(/\d+/g) || [])
    .map(v => !/^(11+?)\1+$/
        .test(Array(+v + 1).join('1')))
    .filter(v => v).length > 0


q = isPrime('optimusprime') // true,'A prime is present'
q
q = isPrime('11') // true,'A prime is present'
q
q = isPrime('4') // false,'No prime has been found'
q
q = isPrime('starPrime') // true,'A prime is present'
q
q = isPrime('11aagghh4') // true,'A prime is present'
q