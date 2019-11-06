/* Checks if the provided integer is a prime number.

Check numbers from `2` to the square root of the given number.
Return `false` if any of them divides the given number, else return `true`, unless the number is less than `2`.

```js
const isPrime =
  const boundary = Math.floor(Math.sqrt(num));
  for (var i = 2; i <= boundary; i++) if (num % i === 0) return false;
  return num >= 2;
};
``` */

// const isPrime = n => ![...Array(n).keys()].slice(2).map(i => !(n % i)).includes(true) && ![0, 1].includes(n)

const isPrime = num => {
    num
    let a = Math.sqrt(num)
    a
    let boundary = Math.floor(Math.sqrt(num))
    boundary
    let temp
    for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
        num
        i
        temp = num % i
        temp
        if (num % i === 0) 
            return false
    }
    temp
    return num >= 2 }

const listPrimesUpTo = n => Array.from({length: n}).fill().map((_,k) => k++).filter(isPrime)

q = listPrimesUpTo(200)
q
p = q.toString()
p

// q = isPrime(1) 
// q
// q = isPrime(2) 
// q
// q = isPrime(3) 
// q
// q = isPrime(4) 
// q
// q = isPrime(5) 
// q
// q = isPrime(6) 
// q
// q = isPrime(7) 
// q
// q = isPrime(8) 
// q
// q = isPrime(9) 
// q
// q = isPrime(10)
// q
// q = isPrime(11)
// q
// q = isPrime(12)
// q
// q = isPrime(13)
// q
// q = isPrime(14)
// q
// q = isPrime(15)
// q
// q = isPrime(16)
// q
// q = isPrime(17)
// q
// q = isPrime(18)
// q
// q = isPrime(19)
// q
// q = isPrime(20)
// q
// q = isPrime(21)
// q
// q = isPrime(22)
// q
// q = isPrime(23)
// q
// q = isPrime(24)
// q
