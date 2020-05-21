// 7kyu - Swap the head and the tail

// const swapHeadAndTail = arr =>
//     arr.length % 2 ?
//         arr.slice((arr.length / 2) + 1)
//            .concat(arr.slice((arr.length / 2), (arr.length / 2 + 1)))
//            .concat(arr.slice(0, arr.length / 2)) :
//         arr.slice((arr.length / 2))
//            .concat(arr.slice(0, arr.length / 2))


// const swapHeadAndTail = (arr, mid = arr.length / 2) => [
//     ...arr.slice(-mid),
//     ...arr.slice(mid, -mid),
//     ...arr.slice(0, mid)
// ];

const swapHeadAndTail = arr => [
    ...arr.slice(arr.length + 1 >> 1),
    ...arr.slice(arr.length >> 1, arr.length + 1 >> 1),
    ...arr.slice(0, arr.length >> 1)
]


q = swapHeadAndTail([1, 2, 3, 4, 5]) // [ 4, 5, 3, 1, 2 ]
q
q = swapHeadAndTail([-1, 2]) // [ 2, -1 ]
q
q = swapHeadAndTail([1, 2, -3, 4, 5, 6, -7, 8]) // [ 5, 6, -7, 8, 1, 2, -3, 4 ]
q