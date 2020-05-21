// 8kyu - Squash the bugs

/* Simple challenge - eliminate all bugs from the supplied code so that the code runs 
and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word. */

// function findLongest(str) {
//     let spl = str.split(" ")
//     let longest = 0
//     for (let i = 0; i < spl.length; i++)
//         if (spl[i].length > longest)
//             longest = spl[i].length
//     return longest
// }

// function findLongest(str) {
//     let spl = str.split(' ')
//     let longest = 0
//     for (i in spl)
//         if (spl[i].length > longest)
//             longest = spl[i].length
//     return longest
// }

const findLongest = (str) => Math.max(...str.split(' ').map(v => v.length))

q = findLongest("The quick white fox jumped around the massive dog") //  7
q
q = findLongest("Take me to tinseltown with you") // 10
q
q = findLongest("Sausage chops") // 7
q
q = findLongest("Wind your body and wiggle your belly") // 6
q
q = findLongest("Lets all go on holiday") // 7
q