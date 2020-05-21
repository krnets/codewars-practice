// 7kyu - Simple Fun #179: Fraction

/* Given two integers a and b, return the sum of the numerator and the denominator of the reduced fraction a/b.

For a = 2, b = 4, the result should be 3
Since 2/4 = 1/2 => 1 + 2 = 3.

For a = 10, b = 100, the result should be 11
Since 10/100 = 1/10 => 1 + 10 = 11.

For a = 5, b = 5, the result should be 2
Since 5/5 = 1/1 => 1 + 1 = 2.

    [input] integer a
    The numerator, 1 ≤ a ≤ 2000.

    [input] integer b
    The denominator, 1 ≤ b ≤ 2000.

    [output] an integer
    The sum of the numerator and the denominator of the reduces fraction. */

const gcd = (a, b) => b ? gcd(b, a % b) : a

// const lcm = (a, b) => a * b / gcd(a, b)

// const fraction = (a, b) => lcm(a, b) / a + lcm(a, b) / b

const fraction = (a, b) => (a + b) / gcd(a, b)

q = gcd(18, 6)
q
q = gcd(6, 18)
q
// q = lcm(6, 18)
// q
q = fraction(90, 120) // 7
q
q = fraction(2, 4) // 3
q
q = fraction(100, 1000) // 11
q
q = fraction(3, 15) // 6
q
q = fraction(114, 200) // 157
q
q = fraction(3, 118) // 121
q