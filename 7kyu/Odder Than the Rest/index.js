// function oddOne(arr) {
//     for (let i of arr) {
//         if (i % 2 !== 0)
//             return arr.indexOf(i)
//     }
//     return -1
// }

// const oddOne = arr => arr.findIndex(x => x % 2 != 0)
// const oddOne = arr => arr.findIndex(x => x & 1)
const oddOne = arr =>
    arr.reduce(
        (prev, curr, index) =>
        curr % 2 ?
        index : prev, -1)


q = oddOne([2, 4, 6, 7, 10]) //, 3);
q
q = oddOne([2, 16, 98, 10, 13, 78]) // 4);
q
q = oddOne([4, -8, 98, -12, -7, 90, 100]) // 4);
q
q = oddOne([2, 4, 6, 8]) // -1);
q