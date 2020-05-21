// 7kyu - Operations With Sets

/* We need a function that receives two arrays arr1 and arr2, each of them, with elements that occur only once. We need to know:

(1) Number of elements that are present in both arrays
(2) Number of elements that are present in only one array
(3) Number of remaining elements after extracting to arr1, the elements that are present in arr2.
(4) Number of remaining elements after extracting to arr2, the elements that are present in arr1.

Explaining the features of this function, let's name it  process2Arrays(), we show graphically how it should operate:

process_2arrays(arr1, arr2) == [(1), (2), (3), (4)]  # (data required above)

Let's see some cases:

arr1 = [1, 2 ,3,4, 5 ,6 ,7 ,8 ,9]
arr2 = [2, 4, 6, 8, 10, 12, 14]
process_2arrays(arr1, arr2) --------> [4, 8, 5, 3]

(1) ---> 4 # because the elements present in both arryas are: 2, 4, 6 and 8 (4 values)
(2) ---> 8 # beacause elements present in only one array are: 1, 3, 5, 7, 9, 10, 12, and 14 (8 values)
(3) ---> 5 # elements remaning of arr1 are: 1, 3, 5, 7, 9
(4) ---> 3 # elements remaning of arr2 are: 10, 12, 14

No doubt, an easy kata to warm up before doing the more complex ones. Enjoy it! */

// function process2Arrays(arr1, arr2) {
//     let res = []
//     // (1) Number of elements that are present in both arrays - intersection
//     // let common = []
//     if (arr1.length < arr2.length) {
//         // common = arr1.filter(v => arr2.includes(v))
//         // res.push(common.length)

//         res.push(([...arr1].filter(v => arr2.includes(v))).length)
//     } else {
//         res.push(([...arr2].filter(v => arr1.includes(v))).length)
//         // common = arr2.filter(v => arr1.includes(v))
//         // res.push(common.length)
//     }
//     // (2) Number of elements that are present in only one array - symDiff
//     res.push([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v)).length)
//     // (3) Number of remaining elements after extracting to arr1, the elements that are present in arr2 - diff(A,B) 
//     res.push([...arr1].filter(v => !arr2.includes(v)).length)
//     // (4) Number of remaining elements after extracting to arr2, the elements that are present in arr1 - diff(B,A)
//     res.push([...arr2].filter(v => !arr1.includes(v)).length)

//     return res
// }

// function process2Arrays(arr1, arr2) {
//     let res = []
//     if (arr1.length < arr2.length) {
//         res.push(([...arr1].filter(v => arr2.includes(v))).length)
//     } else {
//         res.push(([...arr2].filter(v => arr1.includes(v))).length)
//     }
//     res.push([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v)).length)
//     res.push([...arr1].filter(v => !arr2.includes(v)).length)
//     res.push([...arr2].filter(v => !arr1.includes(v)).length)
//     return res
// }

// function process2Arrays(arr1, arr2) {
//     let res = []
//     // let s1 = new Set(arr1)
//     // s1
//     // let s2 = new Set(arr2)
//     if (arr1.length < arr2.length) {
//         // res.push(([...arr1].filter(v => arr2.includes(v))).length)
//         res.push(new Set(([...arr1].filter(v => arr2.includes(v)))).size)
//     } else {
//         // res.push(([...arr2].filter(v => arr1.includes(v))).length)
//         res.push(new Set([...arr2].filter(v => arr1.includes(v))).size)
//     }
//     res.push(new Set([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v))).size)
//     // res.push([...arr1].filter(v => !arr2.includes(v)).length)
//     res.push(new Set([...arr1].filter(v => !arr2.includes(v))).size)
//     // res.push([...arr2].filter(v => !arr1.includes(v)).length)
//     res.push(new Set([...arr2].filter(v => !arr1.includes(v))).size)
//     return res
// }

// function process2Arrays(arr1, arr2) {
//     let res = []
//     if (arr1.length < arr2.length) {
//         res.push(new Set(([...arr1].filter(v => arr2.includes(v)))).size)
//     } else {
//         res.push(new Set([...arr2].filter(v => arr1.includes(v))).size)
//     }
//     res.push(new Set([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v))).size)
//     res.push(new Set([...arr1].filter(v => !arr2.includes(v))).size)
//     res.push(new Set([...arr2].filter(v => !arr1.includes(v))).size)
//     return res
// }

// function process2Arrays(arr1, arr2) {
//     let intersection = new Set([...arr1].filter(v => arr2.includes(v)))
//     let symDiff = new Set([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v)))
//     let diffAB = new Set([...arr1].filter(v => !arr2.includes(v)))
//     let diffBA = new Set([...arr2].filter(v => !arr1.includes(v)))

//     return [intersection.size, symDiff.size, diffAB.size, diffBA.size]
// }

function process2Arrays(arr1, arr2) {
    let intersection = new Set([...arr1].filter(v => arr2.includes(v)))
    let symDiff = new Set([...arr1, ...arr2].filter(v => arr1.includes(v) ^ arr2.includes(v)))
    let diffAB = new Set([...arr1].filter(v => !arr2.includes(v)))
    let diffBA = new Set([...arr2].filter(v => !arr1.includes(v)))

    return [intersection, symDiff, diffAB, diffBA].map(v => v.size)
}

// function process2Arrays(arr1, arr2) {
//     const x = arr1.filter(x => arr2.includes(x)).length
//     const a = new Set(arr1).size
//     const b = new Set(arr2).size
//     return [x, a + b - 2 * x, a - x, b - x];
// }

// function process2Arrays(a, b) {
//     let both = new Set(a.filter(new Set().has, new Set(b)));
//     [rem1, rem2, one] = [a, b, a.concat(b)].map(v => new Set(v.filter(v => !both.has(v))));

//     return [both, one, rem1, rem2].map(({
//         size: l
//     }) => l);
// }

// function process2Arrays(a, b) {
//     let both = new Set(a.filter(new Set().has, new Set(b)));
//     [rem1, rem2, one] = [a, b, a.concat(b)].map(v => new Set(v.filter(v => !both.has(v))));
//     return [both, one, rem1, rem2].map(v => v.size)
// }

// function process2Arrays(arr1, arr2) {
//     [arr1, arr2] = [arr1, arr2].map(e => [...new Set(e)]);
//     [a, b, c] = [arr1, arr2, arr1.filter(n => arr2.includes(n))].map(e => e.length)
//     return [c, a + b - 2 * c, a - c, b - c]
// }

// const R = require("ramda");

// function process2Arrays(arr1, arr2) {
//     const n1 = R.intersection(arr1, arr2);
//     const n2 = R.symmetricDifference(arr1, arr2);
//     const n3 = R.difference(arr1, n1);
//     const n4 = R.difference(arr2, n1);
//     return [n1, n2, n3, n4].map(n => n.length);
// }

// function process2Arrays(arr1, arr2) {
//     let intersection = new Set([...arr1].filter(v => arr2.includes(v)))
//     let diffAB = new Set([...arr1].filter(v => !arr2.includes(v)))
//     let diffBA = new Set([...arr2].filter(v => !arr1.includes(v)))

//     return [intersection.size, diffAB.size + diffBA.size, diffAB.size, diffBA.size]
// }

var arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var arr2 = [2, 4, 6, 8, 10, 12, 14];
q = process2Arrays(arr1, arr2) // [4, 8, 5, 3])
q

arr1 = [33, 2, 3, 37, 38, 40, 12, 10, 43, 44, 47, 49, 8, 19, 22, 24, 26, 28, 29, 30]
arr2 = [1, 34, 17, 7, 9, 10, 43, 49, 22, 27, 28]
q = process2Arrays(arr1, arr2) // [5, 21, 15, 6]
q

arr1 = [32, 34, 3, 4, 39, 10, 43, 13, 11, 18, 21, 22, 7, 25, 26, 36];
arr2 = [32, 5, 38, 8, 41, 42, 12, 48, 40, 21, 22, 26, 10, 30];
q = process2Arrays(arr1, arr2) // [5, 20, 11, 9]
q

arr1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25];
arr2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25];
q = process2Arrays(arr1, arr2) // [3, 19, 9, 10]
q

arr1 = [0, 19, 34, 35, 5, 7, 45, 13, 3, 20, 26, 29, 30];
arr2 = [33, 4, 38, 1, 8, 13, 47, 23, 28, 30, 31];
q = process2Arrays(arr1, arr2) // [2, 20, 11, 9]
q

arr1 = [0, 35, 17, 6, 7, 10, 11, 46, 47, 16, 49, 20, 14, 23, 25, 26, 29];
arr2 = [0, 6, 17, 42, 43, 47, 16, 49, 50, 21, 28, 30];
q = process2Arrays(arr1, arr2) // [6, 17, 11, 6]
q