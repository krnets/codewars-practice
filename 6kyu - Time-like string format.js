// 6kyu - Time-like string format

/* Build up a method that takes an integer and formats it to a 'time - like' format.
The method must raise an exception if its hour length is less than 3 digits and greater than 4. */

// function solution(hour) {
//     let s = String(hour)

//     if (s.length < 3 || s.length > 4)
//         throw Error()
//     if (s.length == 4)
//         return s.slice(0, 2) + ':' + s.slice(2)
//     if (s.length == 3)
//         return s.slice(0, 1) + ':' + s.slice(1)
// }

function solution(hour) {
    let s = String(hour)
    if (s.length < 3 || s.length > 4) throw Error()
    return s.slice(0, -2) + ':' + s.slice(-2)
}


q = solution(800) // should return '8:00'
q
q = solution(1000) // should return '10:00'
q
q = solution(1451) // should return '14:51'
q
q = solution(3351) // should return '33:51'
q
q = solution(10000) // should raise an exception
q