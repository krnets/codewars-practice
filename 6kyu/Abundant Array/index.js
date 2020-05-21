// 6kyu - Abundant Array

/* Your task is to return an array of the first n abundant numbers, sorted by their abundance. 
If the abundance is the same for multiple numbers, sort them numbers from smallest to largest.

"An abundant number or excessive number is a number for which the sum of its proper divisors 
is greater than the number itself. The integer 12 is the first abundant number. 
Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16. The amount by which the sum 
exceeds the number is the abundance. The number 12 has an abundance of 4, for example."

    10 is not an abundant because the sum of its proper divisors is 8; 1+2+5=8.
    12 is an abundant number with an abundance of 4; 1+2+3+4+6=16, 16-12=4.
    18 is an abundant number with an abundance of 3; 1+2+3+6+9=21, 21-18=3.

The first 5 abundant numbers sorted by their abundance are [20, 18, 12, 24, 30]

| Number | Sum of Divisors | Abundance | 
|---|---|---|---|---| | 20 | 22 | 2 | | 18 | 21 | 3 | | 12 | 16 | 4 | | 24 | 36 | 12 | | 30 | 42 | 12 |

You will be given n, a number between 0 and 300 and must return an array of that length, and must do so within the test's time limit. */


function abundantNumber(num) {
    for (var sum = 0, i = 1; i <= Math.floor(num / 2); i++)
        if (num % i == 0)
            sum += i
    return [sum > num, num, sum - num]
}

function abundance(n) {
    let res = []
    for (let i = 1; res.length < n; i++) {
        let cmp = abundantNumber(i)
        if (cmp[0])
            res.push([cmp[1], cmp[2]])
    }
    return res.sort((a, b) => (a[1] - b[1]) || a[0] - b[0]).map(v => v[0])
}

q = abundance(0) //  []
q
q = abundance(1) //  [12]
q
q = abundance(2) // [18, 12]
q
q = abundance(5) //  [20, 18, 12, 24, 30]
q
q = abundance(12) //  [20, 18, 12, 56, 40, 24, 30, 42, 54, 36, 48, 60]
q