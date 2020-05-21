// 7kyu - Simple Fun #194: Binary String

/* You are given a binary string (a string consisting of only '1' and '0'). 
The only operation that can be performed on it is a Flip operation.

It flips any binary character ( '0' to '1' and vice versa) and all characters to the right of it.

For example, applying the Flip operation to the 4th character of string "1001010" 
produces the "1000101" string, since all characters from the 4th to the 7th are flipped.

Your task is to find the minimum number of flips required to 
convert the binary string to string consisting of all '0'.

For s = "0101", the output should be 3.
It's possible to convert the string in three steps:

 "0101" -> "0010"
    ^^^
 "0010" -> "0001"
     ^^
 "0001" -> "0000"
      ^
    [input] string s binary string.
    [output] an integer
The minimum number of flips required. */

// let a = s.indexOf('1')
// let b = s.slice(s.indexOf('1'))
// let d = s.slice(0, s.indexOf('1'))
// let flipped = [...s.slice(s.indexOf('1'))].map(v => v == 1 ? 0 : 1).join ``
// s = d + flipped

function binStr(s) {
    let count = 0
    for (let i = 0; i < s.length; i++) {
        if (s.indexOf('1') != -1) {
            s = s.slice(0, s.indexOf('1')) + [...s.slice(s.indexOf('1'))].map(v => v == 1 ? 0 : 1).join ``
            count++
        }
    }
    return count
}

// const binStr = s => (s.split(/1+0+/).length - 1) * 2 + (/1$/.test(s))
// const binStr = s => (s.split(/1+0+/).length - 1) * 2 + (/1$/.test(s) ? 1 : 0)
// const binStr = s => s.replace(/(.)\1+/g, '$1').replace(/^0/, '').length
// const binStr = s => (s.replace(/^0+/, '').match(/0+|1+/g) || []).length
// const binStr = s => /1+/g.test(s) ? 1 + binStr(s.replace(/^0+/, '').replace(/./g, b => (+b + 1) % 2)) : 0

q = binStr("0101") // 3
q
q = binStr("10000") // 2
q
q = binStr("0000000000") // 0
q
q = binStr("1111111111") // 1
q
q = binStr("10101010101010") // 14
q
q = binStr("11111000011111") // 3
q
q = binStr("000001111100000") // 2
q
q = binStr("111000000000") // 2
q
q = binStr("00000000111111111") // 1
q
q = binStr("1010101011111111111111000000000") // 10
q