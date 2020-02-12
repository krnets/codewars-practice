// 7kyu - Next Prime

/* Get the next prime number!

You will get a numbern (>= 0) and your task is to find the next prime number.

Make sure to optimize your code: there will numbers tested up to about 10^12 */

function isPrime(n) {
    for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
        if (n % i == 0) return false
    }
    return n >= 2
}

function nextPrime(n) {
    if (n == 0) return 2
    while (n++) {
        if (isPrime(n)) return n
    }
}

q = nextPrime(0) // 2
q
q = nextPrime(1) // 2
q
q = nextPrime(2) // 3
q
q = nextPrime(3) // 5
q
q = nextPrime(5) // 7
q
q = nextPrime(11) // 13
q
q = nextPrime(17) // 19
q
q = nextPrime(2971) // 2999
q
q = nextPrime(2971932341) // 2971932343
q
q = nextPrime(98234102739824) // 98234102739847
q
