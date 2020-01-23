// 7kyu - Excessively Abundant Numbers

/* An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.
The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
Derive function abundantNumber(num)/abundant_number(num) which returns true if num is abundant, false if not. */

function abundantNumber(num) {
    for (var sum = 0, i = 1; i <= Math.floor(num / 2); i++)
        if (num % i == 0)
            sum += i
    return sum > num
}


q = abundantNumber(12) // true
q
q = abundantNumber(18) // true
q
q = abundantNumber(37) // false
q
q = abundantNumber(120) // true
q
q = abundantNumber(77) // false
q