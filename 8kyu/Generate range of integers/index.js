// 8kyu - Generate range of integers

/* Implement a function named generateRange(min, max, step), which takes three arguments and 
generates a range of integers from min to max, with the step. 
The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)

generateRange(2, 10, 2) // should return array of [2,4,6,8,10]
generateRange(1, 10, 3) // should return array of [1,4,7,10]

    min < max
    step > 0
    the range does not HAVE to include max (depending on the step) */

// function generateRange(min, max, step) {
//     for (var res = [], i = min; i <= max; i += step) 
//         res.push(i)
//     return res    
// }

// const generateRange = (min, max, step) => resay.from({length: (max - min) / step + 1}, (_, i) => min + i * step)

const generateRange = (min, max, step) => min > max ? [] : [min, ...generateRange(min + step, max, step)]

q = generateRange(2, 10, 2) // [2,4,6,8,10]
q
q = generateRange(1, 10, 3) // [1, 4, 7, 10]
q