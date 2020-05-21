// 7kyu - Measuring Average Speed

/* Speed is a crucial measure of success for any aspiring warrior, so let's write a function to calculate it.

Average Speed is calculated by dividing distance by time. Given two strings as input the first of which indicates 
a codewarrior's distance travelled (in metres or kilometres) and the second indicating the time it takes them to travel 
(in seconds or minutes), return a string indicating their speed in miles per hour rounded to the nearest integer.

For the purposes of this kata one metre per second is defined as 2.23694 miles per hour.

So for example given the input values of distance & time "3km" and "5min" we should return a speed value of "22mph". */

// function calculateSpeed(distance, time) {
//     let metrePerSec = 2.23694
//     let metres = /\d+km$/.test(distance) ? distance.slice(0, -2) * 1000 : distance.slice(0, -1)
//     let seconds = /\d+min$/.test(time) ? time.slice(0, -3) * 60 : time.slice(0, -1)
//     return Math.round(metres / seconds * metrePerSec) + 'mph'
// }

// function calculateSpeed(distance, time) {
//     let metrePerSec = 2.23694
//     let metres = parseInt(distance, 10) * (distance.match('km') ? 1000 : 1)
//     let seconds = parseInt(time, 10) * (time.match('min') ? 60 : 1)
//     return Math.round(metres / seconds * metrePerSec) + 'mph'
// }

function calculateSpeed(distance, time) {
    let metres = parseInt(distance, 10) * (distance.match('km') ? 1000 : 1)
    let seconds = parseInt(time, 10) * (time.match('min') ? 60 : 1)
    return Math.round(metres / seconds * 2.23694) + 'mph'
}

q = calculateSpeed("100m", "10s") // "22mph"
q
q = calculateSpeed("3km", "5min") // "22mph"
q
q = calculateSpeed("35m", "293s") // "0mph"
q
q = calculateSpeed("573km", "39min") // "548mph"
q