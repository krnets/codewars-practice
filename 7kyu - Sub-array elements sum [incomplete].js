// 7kyu - Sub-array elements sum

const elementsSum = (arr, d) =>  {
    let l = arr.length
    l
    // let aa = arr.reverse()
    let a = arr[0][0]
    a
    let b = arr[1][3]
    b
    let c = arr[2][0]
    c
    // return b + c + d
    return [a,b,c].reduce((a,b) => a + b, 0)
}

// q = elementsSum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]]) // 16
// q
q = elementsSum([[3], [4, 6, 5, 3, 2], [9, 8, 7, 4]]) // 15
q
// q = elementsSum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []]) /  7
// q
// q = elementsSum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []], 5) // 12
// q
// q = elementsSum([[3, 2], [4], []]) /  0
// q