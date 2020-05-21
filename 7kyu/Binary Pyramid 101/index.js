// 7kyu - Binary Pyramid 101

/* Given two numbers (m and n) :

    convert all numbers from m to n to binary
    sum them as if they were in base 10
    convert the result to binary
    return as string

Eg: with the numbers 1 and 4

   1 // 1 to binary is 1
+ 10 // 2 to binary is 10
+ 11 // 3 to binary is 11
+100 // 4 to binary is 100
----
 122 // 122 in Base 10 to Binary is 1111010

So BinaryPyramid ( 1 , 4 ) should return "1111010"

    range should be ascending in order */


// const BinaryPyramid = (m, n) => Array.from({
//     length: n - m + 1
// }, (_, i) => i + 1).map(v => v.toString(2)).reduce((a, b) => a + Number(b), 0).toString(2)

const BinaryPyramid = (m, n) => Array(n - m + 1).fill().map((_, i) => (m + i).toString(2)).reduce((a, b) => +b + a, 0).toString(2)
// const BinaryPyramid = (m, n) => Array(n-m+1).fill().map((_, i) => +(m+i).toString(2)).reduce((a, b) => a + b, 0).toString(2)
// const BinaryPyramid = (m, n) => [...Array(n-m+1)].reduce((a, _, i) => a + +(m + i).toString(2), 0).toString(2)

// function BinaryPyramid(m, n) {
//     let sm = 0;
//     for (let i = m; i <= n; i++)
//         sm += parseInt(i.toString(2));
//     return sm.toString(2);
// }

q = BinaryPyramid(1, 4) // "1111010"
q