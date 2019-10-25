// CHALLENGE 1: ADD ALL NUMBERS
// Return a sum of all parameters entered regardless of the amount of numbers - NO ARRAYS
// ex. addAll(2,5,6,7) === 20

function addAll() {

    // ES5 arguments
    var args = Array.prototype.slice.call(arguments)
    let total = 0;

    // Method 1: CLASSIC FOR LOOP
    // for (let i = 0; i < args.length; i++) {
    //     total += args[i]
    // }

    // Method 2: CLASSIC DO-WHILE LOOP
    // let i = 0
    // do {
    //     total += args[i]
    //     i++
    // } while (i < args.length)

    // Method 3: CLASSIC WHILE LOOP
    // let i = 0
    // while (i < args.length) {
    //     total += args[i]
    //     i++
    // }

    // Method 4: ES6 FOR LOOP
    // for (let num of args) {
    //     total += num
    // }

    // Method 5: ForEach LOOP (not recommended)
    // args.forEach(num => total += num)

    // Method 6: Higher order MAP function
    // args.map(num => total += num)

    // Method 7: Higher order REDUCE function
    return args.reduce((accum, curr) => accum + curr, 0)

    // return total
}

// q = addAll(2, 5, 6, 7) === 20
q = addAll(2, 5, 6, 7)
q
q = addAll(2019, 51, 16, 37)
q
q = addAll(8)
q

// CHALLENGE 2: SUM ALL PRIMES
// Pass in a number to loop up to and add all of the prime numbers. A prime number is a whole number greater than 1 whose only factors are 1 and itself
// ex. sumAllPrimes(10) == 17


function sumAllPrimes(num) {
    let total = 0;

    function isPrime(i) {
        for (let j = 2; j < i; j++) {
            j
            if (i % j === 0) {
                j
                return false
            }
        }
        i
        return true
    }
    for (let i = 2; i <= num; i++) {
        if (isPrime(i)) {
            i
            total += i;
            total
        }
    }
    total
    return total
}

// q = sumAllPrimes(10)
// q
// CHALLENGE 3: SEEK & DESTROY
// Remove from the array whatever is in the following arguments. Return the leftover numbers in an array
// ex. seekAndDestroy([2, 3, 4, 6, 6, 'hello'], 2, 6) == [3, 4, 'hello']

// function seekAndDestroy(arr) {
//     const args = Array.from(arguments)

//     function filterArr(arr) {
//         // Return true if NOT in array 
//         return args.indexOf(arr) === -1
//     }

//     return arr.filter(filterArr)
// }
// q = seekAndDestroy([2, 3, 4, 6, 6, 'hello'], 2, 6) == [3, 4, 'hello']

function seekAndDestroy(arr, ...rest) {
    return arr.filter(val => !rest.includes(val))
}

q = seekAndDestroy([2, 3, 4, 6, 6, 'hello'], 2, 6, )
q

// CHALLENGE 4: SORT BY HEIGHT
// Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
// ex.
// a = [-1, 150, 190, 170, -1, -1, 160, 180]
// sortByHeight(a) == [-1, 150, 160, 170, -1, -1, 180, 190]

function sortByHeight(a) {
    const arr1 = []
    const arr2 = []

    a.forEach((val, i) =>
        (val === -1 ?
            arr1.push(i) :
            arr2.push(val)))

    arr1
    arr2

    const sortedArr = arr2.sort((prev, next) => prev - next)
    sortedArr

    arr1.forEach((val, i) =>
        sortedArr.splice(arr1[i], 0, -1))

    sortedArr
    
    return sortedArr.toString()
}

a = [-1, 150, 190, 170, -1, -1, 160, 180]
// q = sortByHeight(a) == [-1, 150, 160, 170, -1, -1, 180, 190]
// q
q = sortByHeight(a)
q


// CHALLENGE 5: MISSING LETTERS
// Find the missing letter in the passed letter range and return it. If all letters are present, return undefined
// ex.
// missingLetters("abce") == "d"
// missingLetters("abcdefghjklmno") == "i"
// missingLetters("abcdefghijklmnopqrstuvwxyz") == undefined


function missingLetters(str) {

    let compare = str.charCodeAt(0)
    let missing;

    str.split('').map((char, i) => {
        if(str.charCodeAt(i) == compare) {
            ++compare
        } else {
            missing = String.fromCharCode(compare)
        }
    })

    return missing;
}

q = missingLetters("abcdefghijm")
q
q = missingLetters("abce") == "d"
q
q = missingLetters("abcdefghjklmno")
q = missingLetters("abcdefghjklmno") == "i"
q
q = missingLetters("abcdefghijklmnopqrstuvwxyz") 
q = missingLetters("abcdefghijklmnopqrstuvwxyz") == undefined
q

// CHALLENGE 6: EVEN & ODD SUMS
// Take in an array and return an array of the sums of even and odd numbers
// ex.
// evenOddSums([50, 60, 60, 45, 71]) == [170, 116]

function evenOddSums(arr) {

    // let sumOdds = arr
    //         .filter(n => n % 2 == 0)
    //         .reduce((prev, curr) => prev + curr)

    // let sumEvens = arr
    //         .filter(n => n % 2 !== 0)
    //         .reduce((prev, curr) => prev + curr)
    let sumOdds = 0
    let sumEvens = 0

    // arr.forEach(n => {
    //     if (n % 2 == 0) {
    //         sumOdds += n
    //     } else {
    //         sumEvens +=n
    //     }
    // })

    arr.forEach(num =>
        (num % 2 == 0 ? 
            (sumEvens += num) : 
            (sumOdds += num)))

    return [sumEvens, sumOdds]
    
}

// q = evenOddSums([50, 60, 60, 45, 71]) == [170, 116]
q = evenOddSums([50, 60, 60, 45, 71])
q