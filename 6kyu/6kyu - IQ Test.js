// 6kyu - IQ Test

// function iqTest(numbers) {
//     let a = numbers.split(' ')
//     let even = a.filter(v => v % 2 == 0)
//     let odd = a.filter(v => v % 2 != 0)
//     let indices = a.map(Number)

//     return odd.length == 1 && even.length > 1 ?
//         indices.indexOf(+odd) + 1 :
//         indices.indexOf(+even) + 1
// }

function iqTest(numbers) {
    let xs = numbers.split(' ')
    let odd = xs.filter(x => x % 2 != 0)
    let even = xs.filter(x => x % 2 == 0)
    let unique = odd.length == 1 ? odd[0] : even[0]

    return xs.indexOf(unique) + 1
}

q = iqTest("2 4 7 8 10") // 3
q
// Third number is odd, while the rest of the numbers are even

q = iqTest("1 2 2") // 1
q
// First number is odd, while the rest of the numbers are even

q = iqTest("1 2 1 1") // 2 
q
// Second number is even, while the rest of the numbers are odd