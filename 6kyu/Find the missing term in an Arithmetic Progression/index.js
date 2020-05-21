// 6kyu - Find the missing term in an Arithmetic Progression

/* An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. You are provided with 
consecutive elements of an Arithmetic Progression. There is however one hitch: 
exactly one term from the original series is missing from the set of numbers which have been given to you. 
The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. 
The missing term will never be the first or last one.

findMissing([1, 3, 5, 9, 11]) == 7

PS: This is a sample question of the facebook engineer challenge on interviewstreet. 
I found it quite fun to solve on paper using math, derive the algo that way. Have fun! */


// function findMissing(list) {
//     let range = list[list.length - 1] - list[0]
//     let step = range / list.length
//     return list.filter((v, i) => v != (list[0] + i * step))[0] - step
// }

// function findMissing(list) {
//     let step = (list[list.length - 1] - list[0]) / (list.length)
//     return list.filter((val, index) => val != (list[0] + index * step))[0] - step
// }

function findMissing(list) {
    let range = list[list.length - 1] - list[0]
    let step = range / list.length
    return list.find((v, i) => v != (step * i) + list[0]) - step
}

// const findMissing = list => (list[0] + list[list.length - 1]) * (list.length + 1) / 2 - list.reduce((a, b) => a + b)

q = findMissing([1, 3, 4]) // 2
q
q = findMissing([1, 3, 5, 9, 11]) // 7
q
