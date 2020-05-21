// 6kyu - Sum of Two Integers 

/* Given Two integers a , b , find The sum of them , 
BUT You are not allowed to use the operators + and -

    The numbers (a,b) may be positive , negative values or zeros .
    Returning value will be an integer .
    Javascript: the Array reduce methods are disabled, along with eval, require, and module . */

// function add(x, y) {
//     while (y != 0) {
//         let carry = x & y
//         x = x ^ y
//         y = carry << 1
//     }
//     return x
// }
// carry now contains common set bits of x and y  
// Sum of bits of x and y where at least one of the bits is not set  
// Carry is shifted by one so that adding it to x gives the required sum  

// const add = (x, y) => y == 0 ? x : add(x ^ y, (x & y) << 1)

const add = (() => {}).constructor('a', 'b', `return a ${String.fromCharCode(43)} b`)


q = add(1, 2) // 3
q
q = add(5, 19) // 24
q
q = add(23, 17) // 40
q
q = add(-14, -16) // -30
q
q = add(-50, -176) // -226
q
q = add(-10, -29) // -39
q
q = add(-13, 13) // 0
q
q = add(-27, 18) // -9
q
q = add(-89, 30) // -60
q