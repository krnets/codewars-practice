// 6kyu - Irreducible Sum of Rationals

/* You will have a list of rationals in the form

lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]
or
lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]

where all numbers are positive integers. 
You have to produce their sum N / D in an irreducible form: 
this means that N and D have only 1 as a common divisor.

Return the result in the form: [N, D] 

If the result is an integer (D evenly divides N) return an integer 
If the input list is empty, return null

[ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]
    1/2  +  1/3  +  1/4     =      13/12    */

function sumFracts(list) {
    if (!list.length) return null
    let gcd = (a, b) => b ? gcd(b, a % b) : a
    let [num, denom] = list.reduce(([a, x], [b, y]) => [a * y + b * x, x * y], [0, 1])
    let g = gcd(num, denom)
    return g == denom ? num / denom : [num / g, denom / g]
}

q = sumFracts([[1, 2], [1, 3], [1, 4]]) // [13, 12]
q
q = sumFracts([[1, 3], [5, 3]]) // 2
q
q = sumFracts([[12, 3], [15, 3]]) // 9
q
q = sumFracts([[2, 7], [1, 3], [1, 12]]) // [59, 84]
q