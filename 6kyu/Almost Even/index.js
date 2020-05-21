// 6kyu - Almost Even

// function splitInteger(num, parts) {
//     let n = Math.floor(num / parts)
//     let array = Array(parts).fill(n)
//     if (array.reduce((a, b) => a + b, 0) == num)
//         return array
//     for (let i = array.length - 1, temp = 0; temp != num; i--) {
//         array[i]++
//         temp = array.reduce((a, b) => a + b, 0)
//     }
//     return array
// }

// function splitInteger(n, p) {
//     return Array.apply(null, new Array(p)).map(function (v, i) {
//         return (n / p | 0) + (n % p - i > 0 ? 1 : 0);
//     });
// }

// const splitInteger = (num, parts) => Array(parts).fill().map((_, i) => (num / parts | 0) + (num % parts - i > 0 ? 1 : 0))
// const splitInteger = (num, parts) => Array(parts).fill().map((_, i) => ~~(num / parts) + (parts - 1 - i < num % parts))
// const splitInteger = (num, parts) => Array(parts).fill().map((_, i) => ~~(num / parts) + (num % parts - i > 0 ? 1 : 0))
// const splitInteger = (num, parts, r = num / parts | 0) => [...Array(parts).fill(r), ...Array(num % parts).fill(r + 1)].slice(-parts)

// function splitInteger(num, parts) {
//     const remainder = num % parts
//     const int = Math.floor(num / parts)

//     return [
//         ...new Array(parts - remainder).fill(int),
//         ...new Array(remainder).fill(int + 1)
//     ];
// }

// function splitInteger(num, parts) {
//     let arr = Array(parts).fill(Math.floor(num / parts))
//     let total = arr.reduce((a, b) => a + b)

//     for (let i = 0; i < arr.length; i++) {
//         if (total == num) break
//         arr[i]++
//         total++
//     }
//     return arr
// }

function splitInteger(num, parts) {
    let n = Math.floor(num / parts)
    let array = Array(parts).fill(n)
    let total = array.reduce((a, b) => a + b, 0)

    for (let i = array.length-1; total != num; i--) {
        array[i]++
        total++
    }
    return array
}


q = splitInteger(10, 1) //  [10]
q
q = splitInteger(2, 2) // [1,1]
q
q = splitInteger(20, 5) // [4,4,4,4,4]
q
q = splitInteger(20, 6) // [3,3,3,3,4,4]
q
q = splitInteger(11, 3) // [3,4,4]
q
q = splitInteger(4000, 37) // [108,108,108,108,108,108,108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 109, 109, 109, 109]
q
q = splitInteger(101, 8) // [12, 12, 12, 13, 13, 13, 13, 13]
q