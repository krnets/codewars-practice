// 5kyu - Human Readable Time

/* Write a function, which takes a non-negative integer (seconds) as input and returns 
the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures. */

// function humanReadable(seconds) {
//     let sec = seconds % 60
//     seconds = (seconds - sec) / 60
//     let min = seconds % 60
//     seconds = (seconds - min) / 60
//     let hour = seconds
//     return [String(hour).padStart(2, '0'), String(min).padStart(2, '0'), String(sec).padStart(2, '0')].join(':')
// }

// const humanReadable = s => [(s / (60 * 60) | 0) + '', ((s / 60 | 0) % 60) + '', (s % 60) + ''].map(v => v.padStart(2, '0')).join(':')

const humanReadable = s => [s / (60 * 60), (s / 60) % 60, s % 60].map(v => String(~~v).padStart(2, '0')).join(':')


q = humanReadable(0) // '00:00:00', 'humanReadable(0)'
q
q = humanReadable(5) // '00:00:05', 'humanReadable(5)'
q
q = humanReadable(60) // '00:01:00', 'humanReadable(60)'
q
q = humanReadable(86399) // '23:59:59', 'humanReadable(86399)'
q
q = humanReadable(359999) // '99:59:59', 'humanReadable(359999)'
q