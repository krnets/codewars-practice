function strong(n) {
    function iterFactorial(num) {
        let result = 1;
        for (let i = 2; i <= num; i++)
            result *= i;
        return result;
    }

    return n == n.toString().split('')
        .map((v, i) => iterFactorial(v))
        .reduce((accum, val) => accum + val) ? 'STRONG!!!!' : 'Not Strong !!'
}

q = strong(1) // "STRONG!!!!"
q
q = strong(2) // "STRONG!!!!"
q
q = strong(145) // "STRONG!!!!"
q
q = strong(7) // "Not Strong !!"
q
q = strong(93) // "Not Strong !!"
q
q = strong(185) // "Not Strong !!"
q