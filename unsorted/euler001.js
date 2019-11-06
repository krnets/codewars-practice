// Project Euler P1
// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

function multiples3and5(m, n, limit) {
    let min = Math.min(m, n)
    console.log(min)
    let sum = 0
    for (let i = min; i < limit; i++) {
        if (i % m === 0 || i % n === 0) {
            sum += i;
        }
    }
    return sum
}

q = multiples3and5(3,5,1000)
q

const multiples3and5func = (m, n , limit) => {
    let min = Math.min(m, n);
    return Array(limit).fill()
        .map((_,i) => i)
        .splice(min)
        .filter(w => w % m == 0 || w % n == 0)
        .reduce((curr, prev) => curr + prev)
    }


p = multiples3and5func(3,5,1000)
p

s = p == q
s