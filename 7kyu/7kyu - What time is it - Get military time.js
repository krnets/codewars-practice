// 7kyu - What time is it - Get military time

// function getMilitaryTime(input) {
//     let dayHalf = input.slice(-2)
//     let newStr = [...input].slice(0, -2).join ``
//     let time = '';

//     [hours, minutes, seconds] = newStr.split(':')

//     if (dayHalf == 'AM') {
//         time += (12 + Number(hours)) % 12 + ':'
//         time += minutes + ':'
//         time += seconds
//     } else {
//         time += 12 + (Number(hours) % 12) + ':'
//         time += minutes + ':'
//         time += seconds
//     }
//     return time.padStart(8, '0')
// }

function getMilitaryTime(input) {

    [hours, minutes, seconds, period] = input.match(/\d+|[A-Z]+/g)
    let time = ''

    if (period == 'AM')
        time += (12 + Number(hours)) % 12 + ':' + minutes + ':' + seconds
    else
        time += 12 + (Number(hours) % 12) + ':' + minutes + ':' + seconds

    return time.padStart(8, 0)
}

// const getMilitaryTime = input => input.replace(/^../, h => (h % 12 + input.endsWith('PM') * 12).toString().padStart(2, '0')).slice(0, -2)


q = getMilitaryTime('12:00:01AM') // '00:00:01'
q
q = getMilitaryTime('11:46:47PM') // '23:46:47'
q