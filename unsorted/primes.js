// const isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)

const primes = num => {
    let arr = Array.from({
            length: num - 1
        })
        .map((value, index) => index + 2);

    let sqroot = Math.floor(Math.sqrt(num));

    let numsTillSqroot = Array.from({
            length: sqroot - 1
        })
        .map((value, index) => index + 2);

    numsTillSqroot.forEach(x =>
        (arr = arr.filter(y => y % x !== 0 || y === x)))

    return arr
}

q = primes(10)
q