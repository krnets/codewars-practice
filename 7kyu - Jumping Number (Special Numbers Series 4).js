function jumpingNumber(n) {
    // let s = String(n).split('')
    // s
    const isJumping = [...`${n}`]
        .map((num, i, self) => i === 0 ? 1 : num - self[i - 1])
        .every(num => num === 1 || num === -1)
        
        isJumping

    return isJumping ? 'Jumping!!' : 'Not!!'
}

q = jumpingNumber(98789876) // "Jumping!!"
q
q = jumpingNumber(79) // "Not!!"
q

// function jumpingNumber(n) {
//     let s = String(n).split('')
//     for (let i = 1; i < s.length; i++) {
//         if (Math.abs(s[i] - s[i - 1]) != 1)
//             return "Not!!"
//     }
//     return "Jumping!!"
// }

// q = jumpingNumber(1) // "Jumping!!"
// q
// q = jumpingNumber(7) // "Jumping!!"
// q
// q = jumpingNumber(9) // "Jumping!!"
// q
// q = jumpingNumber(23) // "Jumping!!"
// q
// q = jumpingNumber(32) // "Jumping!!"
// q
// q = jumpingNumber(98) // "Jumping!!"
// q
// q = jumpingNumber(8987) // "Jumping!!"
// q
// q = jumpingNumber(4343456) // "Jumping!!"
// q
// q = jumpingNumber(7710) // "Not!!""
// q
// q = jumpingNumber(9845) // "Not!!"
// q
// q = jumpingNumber(83) // "Not!!"
// q
// q = jumpingNumber(43433) // "Not!!"
// q