// 6kyu - Clock in Mirror

/* Peter can see a clock in the mirror from the place he sits in the office. 
When he saw the clock shows 12:22, he knows that the time is 11:38

in the same manner:

05:25 --> 06:35
01:50 --> 10:10
11:58 --> 12:02
12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.
Return the real time as a string.
Consider hours to be between 1 <= hour < 13.
So there is no 00:20, instead it is 12:20.
There is no 13:20, instead it is 01:20. */

// function WhatIsTheTime(timeInMirror) {
//     [hh, mm] = timeInMirror.split(':')
//     let hour = (24 - hh - 1) % 12
//     let minute = 60 - mm
//     let format = arr => arr.map(v => String(v).padStart(2, '0')).join(':')
//     return minute == 60 ? format([hour + 1, 0]) : hour == 0 ? format([12, minute]) : format([hour, minute])
// }

function WhatIsTheTime(timeInMirror) {
    [h, m] = timeInMirror.split(':').map(Number)
    h = (m ? 11 : 12) - h % 12 || 12
    m = (60 - m) % 60
    return [h, m].map(v => String(v).padStart(2, '0')).join(':')
}

q = WhatIsTheTime("06:35") // "05:25"
q
q = WhatIsTheTime("11:59") // "12:01"
q
q = WhatIsTheTime("12:02") // "11:58"
q
q = WhatIsTheTime("04:00") // "08:00"
q
q = WhatIsTheTime("06:00") // "06:00"
q
q = WhatIsTheTime("12:00") // "12:00"
q