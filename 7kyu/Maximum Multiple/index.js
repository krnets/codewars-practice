// 7kyu - Maximum Multiple

/* Given a Divisor and a Bound, Find the largest integer N, Such That,
    N is divisible by divisor
    N is less than or equal to bound
    N is greater than 0.

    The parameters (divisor, bound) passed to the function are only positve values.
    It's guaranteed that a divisor is Found .

    maxMultiple (2,7) ==> return (6)
    (6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .
    
    maxMultiple (10,50)  ==> return (50)
    (50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*
    
    maxMultiple (37,200) ==> return (185)
    (185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 . */


// const maxMultiple = (divisor, bound) => Array(bound).fill().map((_, i) => i + 1).reverse().filter(v => v % divisor == 0)[0] || 0
// const maxMultiple = (divisor, bound) => Array(bound).fill().map((_, i) => i + 1).reduce((a, b) => b % divisor ? a : b, 0)

const maxMultiple = (divisor, bound) => bound - (bound % divisor)


q = maxMultiple(2, 7) // 6
q
q = maxMultiple(3, 10) // 9
q
q = maxMultiple(7, 17) // 14
q
q = maxMultiple(10, 50) // 50
q
q = maxMultiple(37, 200) // 185
q
q = maxMultiple(7, 100) // 98
q
q = maxMultiple(37, 100) // 74
q
q = maxMultiple(1, 13) // 13
q
q = maxMultiple(1, 1) // 1
q
q = maxMultiple(4, 1) // 0
q