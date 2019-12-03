// 7kyu - Reverse fibonacci series

/* Write a function to generate 'n' number of fibonacci series (0,1,1,2,3...) in reverse order. 
The output should be a string of fibonacci series in the reverse order upto the given number. */

function reverseFibo(n) {
    let res = [0]
    let [a, b] = [0, 1]
    while (--n) {
        [a, b] = [b, a + b]
        res.push(a)
    }
    return res.reverse().join ``
}

// function reverseFibo(n) {
//     let a = 0, b = 1, r = [];
//     while (n--) {
//         r.unshift(a);
//         [a, b] = [b, a + b];
//     }
//     return r.join ``
// }

q = reverseFibo(3) // => '110'
q
q = reverseFibo(10) // => '3421138532110'
q
q = reverseFibo(15) // => '3421138532110'
q