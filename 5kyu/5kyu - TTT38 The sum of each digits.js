// 5 kyu - T.T.T .38: The sum of each digits
/* 
In this kata, the problem is: Give you a range of number, Calculate the sum of the each digits. For example:

range:1-10
all numbers in the range is:12345678910
the sum of each digits is:1+2+3+4+5+6+7+8+9+1+0=46

range:1-20
all numbers in the range is:1234567891011121314151617181920
the sum of each digits is:
1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0=102

Task

Complete function sumOfDigits() that accepts two arguments from and to. This is a range of a number sequence(from < to). Please return the sum of all digits between from and to(both include).

You should find a better algorithm, because the range may be very large(1 <= from < to <= 10^7) ;-)
Examples

sumOfDigits(1,10) === 46
sumOfDigits(1,20) === 102
sumOfDigits(1,100) === 901
sumOfDigits(1,1000) === 13501

Hint

You might be confused by a very large range . Here is an example of the calculation of 1 to 100:

sumOfDigits(1,100) 
solve process:
Divide these numbers into 51 groups
(1,98) (2,97) (3,96) (4 95)....(48,51) (49,50) --- 1-49th group
99  ---50th group
100 ---51th group
We can find that the value of 1 to 50 groups all are 18
So the whole calculation should be:
18 * 50 + (1+0+0) = 900 + 1 = 901

1 to 10, 1 to 100, 1 to 1000... can calculate by this way. But you should think about irregular situations, such as: 2 to 100 , 1 to 20, 34 to 101... */

// function sumOfDigits(from, to) {
//     for (var s = 0, i = from; i <= to; i++)
//     return s
// }
//   let a = Array.from({length: to - from + 1}, (_,i) => from + i).join('').split('').join('+')
// return eval(a)
// return eval(s.split('').join('+'))


function sumOfDigits(from, to) {
    return digitSum(to + 1) - digitSum(from);
}

var m = [
    [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
];
for (let t = 1; t < 9; t++) m.push(m[0].map((n, i) => m[t - 1][9] * (i + 1) + Math.pow(10, t) * n))

function digitSum(n) {
    var ds = n.toString(),
        t = 0,
        s = 0;
    for (let i = 0; i < ds.length; i++) {
        s += (m[ds.length - 1 - i][ds[i] - 1] || 0) + t * ds[i] * Math.pow(10, ds.length - 1 - i);
        t += +ds[i];
    };
    return s;
}
////////////////////////
// M=[...Array(1+1E7)].map((S,Q,R)=>{for(R=0,S=Q;S;R+=S=S/10|0);return L+=Q-9*R},L=0)
// sumOfDigits=(Q,S)=>M[S]-M[--Q]
////////////////////////
// function sumOfDigits(from, to) {
//     let sumDigitsThis = n => [...'' + n].reduce((s, v) => s + +v, 0)
//     let sumDigitsTo = n => {
//         if (n == 0) return 0
//         let one = n % 10,
//             ten = n / 10 | 0
//         let ones = 45 * ten + one * (one + 1) / 2
//         let tens = sumDigitsTo(ten) * 10 - sumDigitsThis(ten) * (9 - one)
//         return ones + tens
//     }
//     return sumDigitsTo(to) - sumDigitsTo(from - 1)
// }


q = sumOfDigits(1, 5) // 15
q
q = sumOfDigits(2, 8) // 35
q
q = sumOfDigits(5, 12) // 41
q
q = sumOfDigits(1, 10) // 46
q
q = sumOfDigits(1, 20) // 102
q
q = sumOfDigits(1, 100) // 901
q
q = sumOfDigits(14, 112) // 909
q
q = sumOfDigits(3, 1000) // 13498
q
// //Your solution should passed this quickly ;-)
q = sumOfDigits(1, 10000000) // 315000001
q