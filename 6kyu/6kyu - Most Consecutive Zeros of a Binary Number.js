// 6kyu - Most Consecutive Zeros of a Binary Number

/* Given a string (str) containing a base-10 integer between 0 and 10000, 
convert the integer to its binary representation. 
At that point, obtain a count of the maximum amount of consecutive 0s. 
From there, return the count in written form with a capital letter.

max_consec_zeros("9") => "Two"
max_consec_zeros("13") => "One"
max_consec_zeros("15") => "Zero"
max_consec_zeros("42") => "One"

In the very first example, we have an argument of "9" which is being passed to the method. 
The binary representation of 9 is 1001 which can be read as: one, zero, zero, one. 
There are, at most, two consecutive 0s, resulting in the integer 2 as the value of the count. 
The output in the block of code above reflects the final step of taking 2 from standard form to the written form "Two" as prompted.

max_consec_zeros("550") => "Three"

In this example, we have an argument of "550" which is being passed to the method. 
The binary representation of 550 is 1000100110 which can be read as: 
one, zero, zero, zero, one, zero, zero, one, one, zero. 
There are, at most, three consecutive 0s, resulting in the integer 3 as the value of the count. 
The output in the block of code above reflects the final step of 
taking 3 from standard form to the written form of "Three" as prompted.

One way, among many, to visualize the end of each step might look like:

max_consec_zeros("777")
1: "777"
2: 777
3: 1100001001
4: 4
5: "Four"

max_consec_zeros("777") => "Four" */

// function maxConsecZeros(n) {
//     let numberWords = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen'}
//     let binaryString = ''
//     while (n > 0) {
//         binaryString = n % 2 + binaryString
//         n = Math.floor(n / 2)
//     }
//     let res = binaryString.split('1').map(v => v == 0 ? v.length : v)
//     let out = numberWords[Math.max(0, ...res)]

//     return out[0].toUpperCase() + out.slice(1)
// }

// function maxConsecZeros(n) {
//     let numberWords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']
//     let binaryString = ''
//     while (n > 0) {
//         binaryString = n % 2 + binaryString
//         n = Math.floor(n / 2)
//     }
//     return numberWords[Math.max(0, ...binaryString.split('1').map(v => v == 0 ? v.length : v))]
// }

function maxConsecZeros(n) {
    let numberWords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']
    return numberWords[Math.max(...(+n).toString(2).split('1').map(v => v.length))]
}

// const maxConsecZeros = n => ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']
//                             [Math.max(...((+n).toString(2).match(/0+/g) || ['']).map(v => v.length))]

q = ('7' * 1).toString(2)
q
q = Number('7').toString(2)
q
q = maxConsecZeros("7") // "Zero"
q
q = maxConsecZeros("33") // "Four"
q
q = maxConsecZeros("77") // "Two"
q
q = maxConsecZeros("100") // "Two"
q
q = maxConsecZeros("105") // "Two"
q
q = maxConsecZeros("113") // "Three"
q
q = maxConsecZeros("160") // "Five"
q
q = maxConsecZeros("180") // "Two"
q
q = maxConsecZeros("223") // "One"
q
q = maxConsecZeros("256") // "Eight"
q
q = maxConsecZeros("777") // "Four"
q
q = maxConsecZeros("992") // "Five"
q
q = maxConsecZeros("1024") // "Ten"
q
q = maxConsecZeros("1037") // "Six"
q
q = maxConsecZeros("1088") // "Six"
q
q = maxConsecZeros("2017") // "Four"
q
q = maxConsecZeros("2048") // "Eleven"
q
q = maxConsecZeros("3050") // "One"
q
q = maxConsecZeros("4096") // "Twelve"
q
q = maxConsecZeros("6144") // "Eleven"
q
q = maxConsecZeros("6656") // "Nine"
q
q = maxConsecZeros("7188") // "Five"
q
q = maxConsecZeros("8192") // "Thirteen"
q
q = maxConsecZeros("9999") // "Four"
q
q = maxConsecZeros("10000") // "Four"
q