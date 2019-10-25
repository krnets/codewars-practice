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
function factorial(n) {
    var r = 1;
    while (n > 1) r *= n--;
    return r;
}

q = factorial(0)
q
q = factorial(1)
q
q = factorial(2)
q
q = factorial(3)
q
q = factorial(4)
q
q = factorial(5)
q
q = factorial(6)
q
q = factorial(17)
q