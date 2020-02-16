// 4kyu - Human readable duration format

/* Your task in order to complete this Kata is to write a function which formats a duration, 
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

formatDuration(62)    // returns "1 minute and 2 seconds"
formatDuration(3662)  // returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, 
which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time. */


function formatDuration(seconds) {
    let time = {
        year: (365 * 24 * 60 * 60),
        day: (24 * 60 * 60),
        hour: (60 * 60),
        minute: 60,
        second: 1,
    }
    let result = []
    if (seconds == 0) return 'now'
    for (let key in time) {
        if (seconds >= time[key]) {
            let val = Math.floor(seconds / time[key])
            result.push(val += val > 1 ? ' ' + key + 's' : ' ' + key)
            seconds = seconds % time[key]
        }
    }
    return result.length == 1 ? result[0] :
        result.join(', ').replace(/,([^,]*)$/, ' and' + '$1')
}

// function formatDuration(seconds) {
//     if (!seconds) return 'now'
//     let sec = seconds % 60
//     seconds = (seconds - sec) / 60
//     let min = seconds % 60
//     seconds = (seconds - min) / 60
//     let hour = seconds % 24
//     seconds = (seconds - hour) / 24
//     let day = seconds % 365
//     seconds = (seconds - day) / 365
//     let year = seconds
//     let res = []
//     if (year) res.push(year + ' year'   + (year > 1 ? 's' : ''))
//     if (day)  res.push(day  + ' day'    + (day  > 1 ? 's' : ''))
//     if (hour) res.push(hour + ' hour'   + (hour > 1 ? 's' : ''))
//     if (min)  res.push(min  + ' minute' + (min  > 1 ? 's' : ''))
//     if (sec)  res.push(sec  + ' second' + (sec  > 1 ? 's' : ''))
//     return res.join(', ').replace(/,([^,]*)$/, ' and$1')
// }

// const formatDuration = s => s == 0 ? 'now' : [~~(s / 60 / 60 / 24 / 365), ~~(s / 60 / 60 / 24) % 365, ~~(s / 60 / 60) % 24, ~~(s / 60) % 60, s % 60]
//     .map((v, i) => v + ' ' + ['year', 'day', 'hour', 'minute', 'second'][i] + (v > 1 ? 's' : ''))
//     .filter(v => !/^0/.test(v))
//     .join(', ').replace(/,(?=[\s\d\w]*$)/, ' and')

// .join(', ').replace(/,([^,]*$)/, ' and$1')
// .replace(/,\s(?=[\d\s\w]*$)/, ' and ')
// .replace(/,\s(?=[\d\s\w]*$)/, ' and ')


q = formatDuration(0) // "now"
q
q = formatDuration(1) // "1 second"
q
q = formatDuration(62) // "1 minute and 2 seconds"
q
q = formatDuration(120) // "2 minutes"
q
q = formatDuration(3600) // "1 hour"
q
q = formatDuration(3662) // "1 hour, 1 minute and 2 seconds"
q
q = formatDuration(33662) //  9 hours, 21 minutes and 2 seconds
q
q = formatDuration(77733662) //  2 years, 169 days, 16 hours, 41 minutes and 2 seconds
q