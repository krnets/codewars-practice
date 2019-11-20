// 6kyu - Palindromic Numbers

// function palindromize(number) {
//     for (let i = 0;; i++) {
//         if (!('' + number == [...String(number)].reverse().join ``)) {
//             number += +[...String(number)].reverse().join ``
//         } else {
//             return i + ' ' + number
//         }
//     }
// }

// function palindromize(number) {
//     for (let i = 0;; i++) {
//         if (number + '' != [...number + ''].reverse().join ``) {
//             number += +[...number + ''].reverse().join ``
//         } else {
//             return i + ' ' + number
//         }
//     }
// }

// function palindromize(number) {
//     for (var x = 0, i = 0; number != (x = +[...number + ''].reverse().join ``); ++i)
//         number += x
//     return i + ' ' + number
// }

function palindromize(number) {
    for (let x = i = 0;; ++i)
        if (number != (x = +[...number + ''].reverse().join ``)) {
            number += x
        } else return i + ' ' + number
}

// function palindromize(number) {
//     let x, i = 0
//     while (number != (x = +[...'' + number].reverse().join(''))) ++i, number += x
//     return i + ' ' + number
// };

q = palindromize(195) // "4 9339"
q
q = palindromize(265) // "5 45254"
q
q = palindromize(750) // "3 6666"
q
q = palindromize(757) // "0 757"
q