// 4kyu - Twice linear

/* Consider a sequence u where u is defined as follows:

    The number u(0) = 1 is the first one in u.
    For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    There are no other numbers in u.

u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Given parameter n the function dblLinear returns the element u(n) of the ordered 
(with <) sequence u (so, there are no duplicates).

Example:  dbl_linear(10) should return 22
Note: Focus attention on efficiency */

function dblLinear(n) {
    let x = 1
    let y = []
    let z = []
    for (let i = 0; i < n; i++) {
        y.push(2 * x + 1)
        z.push(3 * x + 1)
        let min = Math.min(y[0], z[0])
        if (min == y[0]) x = y.shift()
        if (min == z[0]) x = z.shift()
    }
    return x
}

q = dblLinear(10) // 22
q
q = dblLinear(20) // 57
q
q = dblLinear(30) // 91
q
q = dblLinear(50) // 175
q
q = dblLinear(100) // 447
q