// 6kyu - Clocky Mc Clock-Face

/* Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
And because the local council has lost most of our tax money to a Nigerian email scam 
there are no funds to fix the clock properly.

Instead, they are asking for volunteer programmers to write some code that tell the time 
by only looking at the remaining hour-hand!

Given the angle (in degrees) of the hour-hand, return the time in HH:MM format. 
Round down to the nearest minute.

    12:00 = 0 degrees
    03:00 = 90 degrees
    06:00 = 180 degrees
    09:00 = 270 degrees
    12:00 = 360 degrees

Notes

    0 <= angle <= 360 */

// function whatTimeIsIt(angle) {
//     let hourAngle = 360 / 12
//     let minuteAngle = hourAngle / 60
//     let hours = angle / hourAngle | 0
//     let minutes = (angle / minuteAngle) % 60 | 0
//     return String(hours == 0 ? 12 : hours).padStart(2, '0') + ':' + String(minutes).padStart(2, '0')
// }

// const whatTimeIsIt = angle => [angle / 30 | 0 || 12, angle % 30 * 2 | 0].map(v => String(v).padStart(2, 0)).join(':')
// const whatTimeIsIt = angle => [angle / 30 | 0 || 12, angle % 30 * 2 | 0].map(v => (v < 10 ? '0' : v) + v).join(':')
// const whatTimeIsIt = angle => [~~(angle / 30) || 12, ~~(angle % 30 * 2)].map(v => ('0' + v).slice(-2)).join(':')
const whatTimeIsIt = angle => [Math.floor(angle / 30) || 12, Math.floor(angle % 30 * 2)].map(v => ('0' + v).slice(-2)).join(':')

q = whatTimeIsIt(0) // "12:00"
q
q = whatTimeIsIt(90) // "03:00"
q
q = whatTimeIsIt(180) // "06:00"
q
q = whatTimeIsIt(270) // "09:00"
q
q = whatTimeIsIt(279) // "09:00"
q
q = whatTimeIsIt(360) // "12:00"
q