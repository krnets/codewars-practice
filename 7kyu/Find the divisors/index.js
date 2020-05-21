// function divisors(n) {
//     let array = []
//     let isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)

//     for (let i = 2; i < n; i++) {
//         let quotient = n / i
//         if (quotient === Math.floor(quotient))
//             array.push(i)
//     }
//     return isPrime(n) ? n + " is prime" : array
// }

// function divisors(integer) {
//     let array = []

//     for (let i = 2; i <= Math.floor(integer / 2); ++i) {
//         if (integer % i == 0)
//             array.push(i)
//     }
//     return array.length == 0 ? integer + ' is prime' : array
// }

function divisors(integer) {
    for (var array = [], i = 2; i < integer; i++)
        if (integer % i == 0)
            array.push(i)
    return array.length == 0 ? integer + ' is prime' : array
}

// function divisors(integer) {
//     let res = []
//     for (let i = 2; i <= Math.floor(integer / 2); ++i)
//         if (integer % i == 0) res.push(i)
//     return res.length ? res : integer + ' is prime'
// }

q = divisors(15), [3, 5]
q
q = divisors(12), [2, 3, 4, 6]
q
q = divisors(13), "13 is prime"
q

// const isPrime = num => {
//     for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
//         if (num % i === 0)
//             return false
//     }
//     return num >= 2
// }

// const isPrime = num => num >= 2 &&

// const isPrime = num => Array.from({
//         length: (Math.floor(Math.sqrt(num)))
//     })
//     .reduce((_,curr,index) => num % index)

// const isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n % i)).includes(true)  && ![0, 1].includes(n)

// q = isPrime(13)
// q
// q = isPrime(29)
// q
// q = isPrime(19)
// q
// q = isPrime(18)
// q
// q = isPrime(2)
// q
// q = isPrime(3)
// q
// q = isPrime(4)
// q
// q = isPrime(5)
// q
// q = isPrime(11)
// q
// q = isPrime(10)
// q
// q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29].every(isPrime)
// q