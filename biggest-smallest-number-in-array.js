function biggestNumberInArray (arr) {
    let highest  = 0;
    for (let i = 0; i < arr.length; i++) {
        if (highest < arr[i])
        highest  = arr[i]
    }
    return highest ;
}

// const biggestNumberInArray = arr => {
//     let highest = 0;
//     // for (el of arr) {
//     //     if (highest < el) highest = el
//     // }
//     // arr.map(el => {
//     //     if (highest < el) highest = el
//     // })
//     return highest;
// }

// const biggestNumberInArray = arr => arr.reduce((prev, curr) => prev > curr ? prev : curr, 0)


q = biggestNumberInArray([2, 9, 3, -29, 1, 86, 5, 7, -187, 22, -2, 4, 2, -7])
q


// function smallestNumberInArray(arr) {
// let smallest = 0;
// for (let i = 0; i < arr.length; i++) {
//     if (smallest > arr[i])
//     smallest = arr[i]
// }
// for (el of arr) {
//     if (smallest > el) smallest = el
// }
// arr.map(el => {
//     if (el < smallest)
//         smallest = el
// })
// return arr.reduce((prev, curr) => prev < curr ? prev : curr, 0)
// arr
// smallest
// return smallest;
// }

const smallestNumberInArray = arr => arr.reduce((prev, curr) => prev < curr ? prev : curr, 0)

// const smallestNumberInArray = arr => {
//     let smallest = 0;
//     arr.map(el => {
//         if (el < smallest) smallest = el
//     });
//     return smallest
// }

q = smallestNumberInArray([2, 9, 3, -29, 1, 486, 5, 7, -187, 22, -2, 4, 2, -7])
q