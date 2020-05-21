// function add(x, y) {
// let carry = x & y
// let result = x ^ y
// while (carry != 0) {
//     let shiftedcarry = carry << 1;
//     carry = result & shiftedcarry;
//     result ^= shiftedcarry
// return result
// }

// function add(x, y) {
//     while (x != 0) {
//         let carry = y & x;
//         y = y ^ x;
//         x = carry << 1;
//     }
//     return y
// }


// class BitMath {
//     static add(a, b) {
//         while (b) {
//             return this.add(a ^ b, (a & b) << 1)
//         }
//         return a;
//     }
// }

const add = (x, y) => y == 0 ? x : add(x ^ y, (x & y) << 1)

// class BitMath {
//     static add(a, b) {
//         return b ? this.add(a ^ b, (a & b) << 1) : a;
//     }
// }

// class BitMath {
//     static add(a, b) {
//         return a ? this.add((a & b) << 1, a ^ b) : b;
//     }
// }


// class BitMath {
//     static add(a, b) {
//         let n = a ^ b
//         let c = (a & b) << 1
//         return n & c ? BitMath.add(n, c) : n ^ c
//     }
// }

// class BitMath {
//     static add(a, b) {
//         if (!b) return a;
//         return this.add(a ^ b, (a & b) << 1)
//     }
// }

q = add(1, 2) // 3
q
q = add(5, 19) // 24
q
q = add(7, 19) // 24
q
q = add(8, 19) // 24
q
q = add(9, 19) // 24
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
q = add(-90, 30) // -60
q