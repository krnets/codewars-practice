/* ************************* */
/* Codewars 7kyu - Factorial */
/* ************************* */
// function factorial(n) {
//     if (n < 2) {
//         return 1;
//     } else {
//         return n * factorial(n-1);
//     }
// }
// function factorial(n) {
//     return n == 0 ? 1 : n * factorial(n - 1)
// }
// function factorial(n) {
//     return n ? n * factorial(n - 1) : 1
// }
// function factorial(n) {
//     for(var acc = 1; n > 0; acc *= n, n--);
//     return acc
// }
// function factorial(n) {
//     var r = 1;
//     while (n > 1) r *= n--;
//     return r;
// }
// function factorial(n) {
//     return n ? n * factorial(n - 1) : 1
// }
const factorial = n => (n == 0) ? 1 : n * factorial(n - 1);
   // factorial(0) =   (n == 0) ? 1 
   // factorial(1) =   (n == 0) ?   : 1 * (factorial(1 - 1) = 0) == 1 * 0 == 0 == factorial(0) == 1.
   // factorial(2) =   (n == 0) ?   : 2 * (factorial(2 - 1) = 1) == 2 * 1 == 2.
   // factorial(3) =   (n == 0) ?   : 3 * (factorial(3 - 1) = 2) == 3 * 2 == 6. 
   // factorial(4) =   (n == 0) ?   : 4 * (factorial(4 - 1) = 3) == 4 * 3 == 24. 
   // factorial(5) =   (n == 0) ?   : 5 * (factorial(5 - 1) = 4) == 5 * 24 == 120.
   // factorial(6) =   (n == 0) ?   : 6 * (factorial(6 - 1) = 5) == 6 * 120 == 720. 
   // factorial(7) =   (n == 0) ?   : 7 * (factorial(7 - 1) = 6) == 7 * 720 == 4900 + 140 = 5040.
   // factorial(8) =   (n == 0) ?   : 8 * (factorial(8 - 1) = 7) == 8 * 5040 == 40000 + 320 = 40320.
   // factorial(9) =   (n == 0) ?   : 9 * (factorial(9 - 1) = 8) == 9 * 40320 == 360,000 + 2,700 + 180 = 362,880.
   // factorial(10) =  (n == 0) ?   : 10* (factorial(10 -1) = 9) == 10 * 362,880 = 3,628,800.
//   const factorial = n => n > 1 ? n*factorial(n-1) : 1

q = factorial(0) //  1
q
q = factorial(1) //  1
q
q = factorial(2) //  2
q
q = factorial(3) //  6
q
q = factorial(4)
q
q = factorial(5)
q
q = factorial(6)
q
q = factorial(7)
q
q = factorial(8)
q
q = factorial(9)
q
q = factorial(10)
q