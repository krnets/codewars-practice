// 7kyu - Podcast Speed Listening Calculator 

/* Calculate the time it takes to listen to the audio when the play speed is varied. 
The time should be rounded down to whole seconds. */

function speedListen(audioLength, playSpeed) {
    [hours, mins, seconds] = audioLength.split(':')
    let audioSeconds = hours * (60 * 60) + mins * 60 + seconds * 1

    let newLength = audioSeconds / playSpeed
    let newLenHrs = ~~(newLength / (60 * 60))
    let newLenMins = ~~(newLength % (60 * 60) / 60)
    let newLenSecs = ~~(newLength % 60)

    return [newLenHrs, newLenMins, newLenSecs].map(v => String(v).padStart(2, 0)).join(':')
}

// function speedListen(audioLength, playSpeed) {
//     [hours, mins, seconds] = audioLength.split(':')
//     let newLength = (hours * (60 * 60) + mins * 60 + seconds * 1) / playSpeed
//     return [newLength / 3600 | 0, (newLength / 60 | 0) % 60, newLength % 60].map(v => String(v).padStart(2, 0)).join(':')
// }

// function speedListen(audioLength, playSpeed) {
//     let newLength = audioLength.split(':').reduce((acc, cur) => acc * 60 + Number(cur), 0) / playSpeed
//     return [newLength / 3600 | 0, (newLength / 60 | 0) % 60, newLength % 60].map(v => String(v).padStart(2, 0)).join(':')
// }

q = speedListen("00:30:00", 2) // "00:15:00"
q
q = speedListen("01:20:00", 1.5) // "00:53:20"
q