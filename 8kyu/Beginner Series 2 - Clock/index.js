// 8kyu - Beginner Series #2 Clock

/* Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

#####Example:

past(0, 1, 1) == 61000

Note! h, m and s will be only Natural numbers! */

// function past(h, m, s) {
//     let secsInHour = 3600
//     let secsInMinute = 60
//     let milliSecsInSec = 1000
//     return (secsInHour * h + secsInMinute * m + s) * milliSecsInSec
// }

function past(h, m, s) {
    let total = 0
    let minsInHour = 60
    let secsInMinute = 60
    let milliSecsInSec = 1000

    total += s * milliSecsInSec
    total += m * (secsInMinute * milliSecsInSec)
    total += h * (minsInHour * secsInMinute * milliSecsInSec)

    return total
}


q = past(0, 1, 1) // 61000
q
q = past(1, 1, 1) // 3661000
q
q = past(0, 0, 0) // 0
q
q = past(1, 0, 1) // 3601000
q
q = past(1, 0, 0) // 3600000
q