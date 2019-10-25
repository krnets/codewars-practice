function sumOrProduct(array, n) {
    array.sort((a, b) => a - b)
    let sumOfLargest = array.slice(-n).reduce((a, b) => a + b, 0)
    let productOfSmallest = array.slice(0, n).reduce((a, b) => a * b, 1)

    return sumOfLargest > productOfSmallest ? 'sum' :
           sumOfLargest < productOfSmallest ? 'product' : 'same'
}

q = sumOrProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) // "sum"
q
q = sumOrProduct([10, 41, 8, 16, 20, 36, 9, 13, 20], 3) // "product"
q
q = sumOrProduct([10, 20, 3, 30, 5, 4], 3) //  "same"
q