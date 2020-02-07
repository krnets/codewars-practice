// 7kyu - Color of the moment

/* Imagine you have a digital clock which paints the whole screen with a color instead of showing you what time it is. 
While it looks good on your wall and you get to impress your guests, you also want to be able to tell what time it is. 
Luckily, the clock also prints the hex code in the bottom right of the screen. Using that, you should be able to tell the time.

The hex code will come to you in this format: #0d242c
And you will return the time in this format: hh:mm:ss

Note: The hexCode you will be provided will always be in the correct format. 
However, it might not point to a correct time. So make sure to throw an error if the time you have calculated is invalid.  */

// function hexToTime(hexCode) {
//     let hours = parseInt(hexCode.slice(1, 3), 16).toString()
//     let minutes = parseInt(hexCode.slice(3, 5), 16).toString()
//     let seconds = parseInt(hexCode.slice(5), 16).toString()
//     if (hours > 23 || minutes > 59 || seconds > 59)
//         throw new Error("That's not a valid time!")
//     return hours.padStart(2, 0) + ':' + minutes.padStart(2, 0) + ':' + seconds.padStart(2, 0)
// }

// function hexToTime(hexCode) {
//     [hrs, min, sec] = hexCode.match(/[a-f\d]{2}/g).map(v => parseInt(v, 16).toString().padStart(2, 0))
//     if (hrs > 23 || min > 59 || sec > 59)
//         throw new Error("That's not a valid time!")
//     return hrs + ':' + min + ':' + sec
// }

function hexToTime(hexCode) {
    [hh, mm, ss] = hexCode.match(/[a-f\d]{2}/g).map(v => parseInt(v, 16).toString().padStart(2, 0))
    if (hh > 23 || mm > 59 || ss > 59)
        throw Error("That's not a valid time!")
    return hh + ':' + mm + ':' + ss
}

q = hexToTime('#0d3737') // '13:55:55'
q
q = hexToTime('#2c3721') // Test.expectError('Thats not a valid time!')
q