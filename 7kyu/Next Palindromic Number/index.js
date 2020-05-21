// 7kyu - Next Palindromic Number

// function nextPal(val) {
//     for (var i = val + 1; i < Number.MAX_SAFE_INTEGER; i++)
//         if (i == [...String(i)].reverse().join ``) return i
// }

// function nextPal(val) {
//     while (true) {
//         val++
//         if (val == [...String(val)].reverse().join ``)
//             return val
//     }
// }

function nextPal(val) {
    do val++
    while (val != [...String(val)].reverse().join ``)
    return val
}

q = nextPal(18) // 22
q
q = nextPal(188) // 191
q
q = nextPal(191) // 202
q
q = nextPal(2541) // 2552
q