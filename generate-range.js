// function generateRange(min, max, step) {
//     let z = []

//     while (min <= max) {
//         z.push(min)
//         min += step
//     }
//     return z
// }

function generateRange(min, max, step) {
    let arr = []

    for (let i = min; i <= max; i += step) 
        arr.push(i)

    return arr    
}




// q = generateRange(2, 10, 2) // [2,4,6,8,10]
// q
q = generateRange(2, 19, 2) // [2,4,6,8,10]
q