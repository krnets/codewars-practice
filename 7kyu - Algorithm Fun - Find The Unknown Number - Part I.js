// 7kyu - Algorithm Fun: Find The Unknown Number - Part I

// function findUnknowNumber(x, y, z) {
//     let n = 0
//     while (n > -1) {
//         n++
//         if ((n % 3 == x) && (n % 5 == y) && (n % 7 == z))
//             return n
//     }
// }

// function findUnknowNumber(x, y, z) {
//     let n = 0
//     do {
//         n++;
//     } while ((n % 3 != x) || (n % 5 != y) || (n % 7 != z))

//     return n
// }

function findUnknowNumber(x, y, z) {
    let n = 0
    while (++n)
        if ((n % 3 == x) && (n % 5 == y) && (n % 7 == z))
            return n
}


q = findUnknowNumber(2, 3, 2) // 23
q
q = findUnknowNumber(1, 2, 3) // 52
q
q = findUnknowNumber(1, 3, 5) // 103
q
q = findUnknowNumber(0, 0, 0) // 105
q
q = findUnknowNumber(1, 1, 1) // 1
q