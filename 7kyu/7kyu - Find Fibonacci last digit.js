// 7kyu - Find Fibonacci last digit

// const fib = n => n == 0 || n == 1 ? 1 : fib(n - 1) + fib(n - 2)

// 1 1 2 3 5 8 13 21 34 55 89
// ^ ^   | :
//   ^ ^ | :
//     ^ ^ :
//       ^ ^
//  [3, 5] = [1 + 2, 2 + 3]
//  [c, d] = [a + b, b + c]
//  [a, b] = [1, 2]

//  [c, d] = [a + b, b + c]
//  [a, b] = [c, d]  

// 0 1 1 2 3 5 8 21 34 55 89 144 233 377 610
// 1 2 3 4 5 6 7  8  9 10 11  12  13  14  15

// function getLastDigit(index) {
//     [a, b] = [0, 1]
//     for (let i = 1; i < index; i++) {
//         [temp, a] = [a, b]
//         b = (b + temp) % 10
//     }
//     return b
// }

function getLastDigit(index) {
    [a, b] = [0, 1]
    for (let i = 0; i < index; i++) {
        [a, b] = [b, (a + b) % 10]
    }
    return a
}

q = getLastDigit(5) // 0 
q
q = getLastDigit(15) // 0 
q
q = getLastDigit(25) // 0 
q
q = getLastDigit(95) // 0 
q
q = getLastDigit(193150) // 5
q
q = getLastDigit(300) // 0
q
q = getLastDigit(20001) // 6
q