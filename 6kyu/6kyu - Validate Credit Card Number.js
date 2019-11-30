// 6kyu - Validate Credit Card Number

/* In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.
Here is the algorithm:
    Double every other digit, scanning from right to left, starting from the second digit (from the right).
    Another way to think about it is: if there are an even number of digits, double every other digit 
    starting with the first; if there are an odd number of digits, double every other digit starting with the second:
    1714 ==> [1*, 7, 1*, 4] ==> [2, 7, 2, 4]
    12345 ==> [1, 2*, 3, 4*, 5] ==> [1, 4, 3, 8, 5]
    891 ==> [8, 9*, 1] ==> [8, 18, 1]
    If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it):
    [8, 18*, 1] ==> [8, (1+8), 1] ==> [8, 9, 1]
    or:
    [8, 18*, 1] ==> [8, (18-9), 1] ==> [8, 9, 1]
    Sum all of the final digits:
    [8, 9, 1] ==> 8 + 9 + 1 = 18
    Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.
      18 (modulus) 10 ==> 8 , which is not equal to 0, so this is not a valid credit card number
Algorithms | Validation */

function validate(n) {
    return [...String(n)].reverse()
        .map((v, i) => i % 2 ? v * 2 : +v)
        .map((v, i) => v > 9 ? v - 9 : v)
        .reduce((a, b) => a + b) % 10 == 0
}

// const validate = n => [...String(n)].reverse()
//     .map((v, i) => i % 2 ? v * 2 : v)
//     .map((v, i) => v > 9 ? v - 9 : v)
//     .reduce((a, b) => a + b) % 10 == 0

// const validate = n => (n + '').split ``
//     .map((_, i) => (~~Math.log10(n) - i) % 2 ? _ * 2 : +_)
//     .map(n => n > 9 ? n - 9 : n)
//     .reduce((s, n) => s + n, 0) % 10 === 0;

q = validate(123) // false
q
q = validate(1) // false
q
q = validate(2121) // true
q
q = validate(1230) // true
q