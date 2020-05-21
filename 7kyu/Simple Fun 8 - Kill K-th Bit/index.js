// 7kyu - Simple Fun #8: Kill K-th Bit

/* In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. 
The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky 
blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, 
in the given number n the kth bit from the right was initially set to 0, but its current value might be different. 
It's now up to you to write a function that will change the kth bit of n back to 0.

For n = 37 and k = 3, the output should be 33   // 3710 = 1001012 ~> 1000012 = 3310

For n = 37 and k = 4, the output should be 37
The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.

    [input] integer n    Constraints: 0 ≤ n ≤ 231 - 1.

    [input] integer k    Constraints: 1 ≤ k ≤ 31.
    The 1-based index of the changed bit (counting from the right).

    [output] an integer */

// function killKthBit(n, k) {
//     let bits = [...n.toString(2)]
//     bits[bits.length - k] = '0'
//     return parseInt(bits.join(''), 2)
// }

// const killKthBit = (n, k) => (s = n.toString(2)) && parseInt(s.replace(/./g, (b, i) => s.length - i == k && b == 1 ? 0 : b), 2)
const killKthBit = (n, k) => n & ~(2 ** (k - 1))
// const killKthBit = (n, k) => n & ~(1 << k - 1)

q = killKthBit(37, 3) // 33
q
q = killKthBit(37, 4) // 37
q
q = killKthBit(0, 4) // 0
q
q = killKthBit(2147483647, 16) // 2147450879
q
q = killKthBit(374823748, 13) // 374819652
q
q = killKthBit(1084197039, 15) // 1084197039
q