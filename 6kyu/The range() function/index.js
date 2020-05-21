// 6kyu - The range() function

/* Let's implement the range function:   range([start], stop, [step])

range(1, 11) => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range(1, 4, 0) => [1, 1, 1]   /!\ note that the step is 0  
range(0) => []
range(10, 0) => []  /!\ note that the end is before the start
range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(0, 30, 5) => [0, 5, 10, 15, 20, 25]

start, if omitted, defaults to 0; step defaults to 1.
Returns a list of integers from start to stop, incremented (or decremented) by step, exclusive.

Note that ranges that stop before they start are considered to be zero-length instead of negative.
Fundamentals | Ranges | Basic Language Features | Numbers | Integers */

// function range(start, end, step) {
//     let args = [...arguments]
//     switch (args.length) {
//         case 3: [start, end, step] = args; break;
//         case 2: var start = args[0], end = args[1], step = 1; break;
//         case 1: var start = 0, end = args[0], step = 1; break;
//     }
//     return Array.from({ length: Math.ceil((end - start) / (step || 1)) }, (_, i) => start + (i * step))
// }

function range(start, end, step) {
    if (arguments.length == 1)
        [start, end, step] = [0, start,  1]
    if (arguments.length == 2)
        [start, end, step] = [start, end, 1]
    return Array.from({ length: Math.ceil((end - start) / (step || 1)) }, (_, i) => start + (i * step))
}

range(10) //?
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
range(4, 17, 10) //?
//  [4, 14], 
range(1, 11) //?
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range(0, 30, 5) //? 
// [0, 5, 10, 15, 20, 25]
range(1, 4, 0) //?
// [1, 1, 1]
range(0) //?
// []
range(10, 0) //? 
// []
range() //?