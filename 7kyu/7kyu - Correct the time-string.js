// 7kyu - Correct the time-string

/* Create a method, that corrects a given time string. There was a problem in addition, so many of the time strings are broken. Time-Format is european. So from "00:00:00" to "23:59:59".

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"

If the input-string is null or empty return exactly this value.
If the time-string-format is invalid, return null.  */

// function timeCorrect(timestring) {
//     if (timestring == '') return ''
//     if (!/^\d{2}:\d{2}:\d{2}$/.test(timestring)) return null

//     let date = new Date()
//     date.setUTCHours(...timestring.split(':'))

//     return date.toLocaleTimeString('en', { hour12: false })
// }

function timeCorrect(timestring) {
    if (timestring == '') return ''
    if (!/^\d{2}:\d{2}:\d{2}$/.test(timestring)) return null
    return new Date(0, 0, 0, ...timestring.split(':')).toLocaleTimeString('en', { hour12: false })
}

// Correction Tests
q = timeCorrect("09:10:01") // "09:10:01"
q
q = timeCorrect("11:70:10") // "12:10:10"
q
q = timeCorrect("19:99:09") // "20:39:09"
q
q = timeCorrect("19:99:99") // "20:40:39"
q
q = timeCorrect("24:01:01") // "00:01:01"
q
q = timeCorrect("52:01:01") // "04:01:01"
q

// Null or Empty
q = timeCorrect(null) // null
q
q = timeCorrect("") // ""
q

// Invalid Format
q = timeCorrect("001122") // null
q
q = timeCorrect("00;11;22") // null
q
q = timeCorrect("0a:1c:22") // null
q