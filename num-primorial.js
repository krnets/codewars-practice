function numPrimorial(n) {
    let primes = Array.from({
            length: n * n
        }).fill()
        .map((_, i) => i++)
        .filter(num => {
            const boundary = Math.floor(Math.sqrt(num));
            for (let i = 2; i <= boundary; i++)
                if (num % i === 0) return false;
            return num >= 2;
        })
    let result = primes.slice(0, n).reduce((a, b) => a * b, 1)
    return result == 1 ? 2 : result
}

// const isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n%i)).includes(true) && ![0,1].includes(n)

// const isPrime = num => {
//     const boundary = Math.floor(Math.sqrt(num));
//     for (var i = 2; i <= boundary; i++)
//         if (num % i === 0) return false;
//     return num >= 2;
// }

function getNprimes(n) {
    //   var arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    // let arr = [...Array(n * n).keys()].slice(2)

    let arr = Array.from({
            length: n * n
        }, (_, i) => i + 1)
        .filter(num => {
            if (num < 2) return false;
            for (let i = 2; i < num; i++) {
                if (num % i == 0) return false;
            }
            return true
        })
    arr
    let b = arr.length
    b
    return arr.slice(0, n)
}

q = getNprimes(6) //,223092870
q

q = numPrimorial(3) //,30
q
q = numPrimorial(4) //,210
q
q = numPrimorial(5) //,2310
q
q = numPrimorial(8) //,9699690
q
q = numPrimorial(9) //,223092870
q