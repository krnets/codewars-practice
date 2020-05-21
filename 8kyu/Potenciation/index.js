// 8kyu - Potenciation

/* The function takes in 2 inputs x and y, and should return x to the power of y

Simple, right? But you're NOT allowed to use Math.pow();

Obs: x and y will be naturals, so DON'T take fractions into consideration;
Note : zero to the power of zero equals one in this kata */

function power(x, y) {
    for (var res = 1, i = 0; i < y; i++)
        res *= x
    return res
}

// const power = (x, y) => x ** y

q = power(1, 701270) // 1
q
q = power(2, 2) // 4
q
q = power(3, 2) // 9
q
q = power(-1, 40) // 1
q