// 7kyu - Maximum Adjacent Elements Product 


// const adjacentElementsProduct = (array) => array.length == 2 ? array[0] * array[1] :
//             array.reduce((maxProduct, curr, i) => 
//                         curr * array[i+1] > maxProduct ? 
//                         curr * array[i+1] : maxProduct)

// function adjacentElementsProduct(array) {
//     let maxProduct = -Infinity
//     for (let i = array.length; i > 1; i--) {
//         let v = array.splice(-1) * array.slice(-1)
//         if (v > maxProduct) {
//             maxProduct = v
//         }
//     }
//     return maxProduct
// }

// function adjacentElementsProduct(array) {
//     let newArr = []
//     for (i = 0; i < array.length - 1; i++) {
//         newArr.push(array[i] * array[i + 1])
//         newArr
//     }
//     let b = [...newArr]
//     b
//     return Math.max(...newArr)
// }

// const adjacentElementsProduct = (array) => Math.max(...array.map((n, i) => n * array[i + 1]).slice(0, -1))

// const adjacentElementsProduct = (array) => Math.max(...array.map((n, i) => n * array[i - 1]).slice(1))

const adjacentElementsProduct = (array) => {
    // let a = array.map((v, i) => v * array[i-1]).slice(1)
    // return a
    return Math.max(...array.map((n, i) => n * array[i - 1]).slice(1))
}

// const adjacentElementsProduct = (array) => array.slice(1).reduce((max, curr, i) => Math.max(array[i] * curr, max), -Infinity)



q = adjacentElementsProduct([])
q
q = adjacentElementsProduct([-23, 4, -5, 99, -27, 329, -2, 7, -921]) // -14
q
q = adjacentElementsProduct([5, 8]) // 40
q
q = adjacentElementsProduct([1, 2, 3]) // 6
q
q = adjacentElementsProduct([1, 5, 10, 9]) // 90
q
q = adjacentElementsProduct([4, 12, 3, 1, 5]) // 48
q
q = adjacentElementsProduct([5, 1, 2, 3, 1, 4]) // 6
q
q = adjacentElementsProduct([3, 6, -2, -5, 7, 3]) // 21
q
q = adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]) // 50
q
q = adjacentElementsProduct([5, 6, -4, 2, 3, 2, -23]) // 30
q
q = adjacentElementsProduct([5, 1, 2, 3, 1, 4]) // 6
q
q = adjacentElementsProduct([1, 0, 1, 0, 1000]) // 0
q
q = adjacentElementsProduct([1, 2, 3, 0]) // 6
q