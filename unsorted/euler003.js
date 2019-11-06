// Problem 3
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

(function euler003() {
    let i = 2;
    let num = 600851475143

    while (num > 2) {
        
        if (num % i == 0) {
            num = num / i;
            num
        }
        i
        i++
    }
    i
}());

// q = euler003(600851475143)
// q
// const primes = num => {                                                                 
//     let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),                       
//       sqroot = Math.floor(Math.sqrt(num)),                                                
//       numsTillSqroot = Array.from({ length: sqroot - 1 }).map((x, i) => i + 2);           
//     numsTillSqroot.forEach(x => (arr = arr.filter(y => y % x !== 0 || y === x)));         
//     return arr;                                                                           
//   };                                                                                      

// q = Math.floor(Math.sqrt(600851475143))
// q

// const factors = (num, primes = false) => {
//     const isPrime = num => {
//       const boundary = Math.floor(Math.sqrt(num));
//       for (var i = 2; i <= boundary; i++) if (num % i === 0) return false;
//       return num >= 2;
//     };
//     const isNeg = num < 0;
//     num = isNeg ? -num : num;
//     w = Number(num)
//     w
//     let array = Array.from({ length: num - 1 })
//     //   .map((val, i) => (num % (i + 2) === 0 ? i + 2 : false))
//     //   .filter(val => val);
//     // if (isNeg)
//     //   array = array.reduce((acc, val) => {
//     //     acc.push(val);
//     //     acc.push(-val);
//     //     return acc;
//     //   }, []);
//     // return primes ? array.filter(isPrime) : array;
//     return typeof num;
//   };

// // q = factors(600851475143n, primes = true)
// q = factors(600851475143n)
// q