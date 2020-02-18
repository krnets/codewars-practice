// 6kyu - String average

/* You are given a string of numbers between 0-9. 
Find the average of these numbers and return it as a floored whole number (no decimal places) written out as a string.

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a" */

// function averageString(str) {
//     let numsMap = { zero:0, one:1, two:2, three:3, four:4, five:5, six:6, seven:7, eight:8, nine:9 }
//     let nums = str.split(' ')
//     let keyMissing = false
//     let average = nums.map(v => (numsMap.hasOwnProperty(v) ? numsMap[v] : keyMissing = true))
//         .reduce((a, b) => a + b, 0) / nums.length | 0
//     return str.length && !keyMissing ? Object.keys(numsMap).find(key => numsMap[key] == average) : 'n/a'
// }

function averageString(str) {
    let numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    let nums = str.split(' ').map(v => numbers.indexOf(v))
    if (nums.includes(-1)) return 'n/a'
    let average = nums.reduce((a, b) => a + b, 0) / nums.length | 0
    return numbers[average]
}

q = averageString("zero nine five two") // "four"
q
q = averageString("four six two three") // "three"
q
q = averageString("one two three four five") // "three"
q
q = averageString("five four") // "four"
q
q = averageString("zero zero zero zero zero") // "zero"
q
q = averageString("one one eight one") // "two"
q
q = averageString("") // "n/a"
q