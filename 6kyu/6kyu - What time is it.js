// 6kyu - What time is it

// function toHumanTime(timestring) {
//     [hours, mins] = timestring.match(/\d+/g)

//     let dict = {
//         45: 'quarter to',
//         15: 'quarter past',
//         30: 'half past',
//         '00': 'twelve',
//         '01': 'one',
//         '02': 'two',
//         '03': 'three',
//         '04': 'four',
//         '05': 'five',
//         '06': 'six',
//         '07': 'seven',
//         '08': 'eight',
//         '09': 'nine',
//         10: 'ten',
//         11: 'eleven',
//         12: 'twelve',
//         13: 'thirteen',
//         14: 'fourteen',
//         15: 'quarter past',
//         16: 'sixteen',
//         17: 'seventeen',
//         18: 'eighteen',
//         19: 'nineteen',
//         20: 'twenty',
//         21: 'twenty-one',
//         22: 'twenty-two',
//         23: 'twenty-three',
//         24: 'twenty-four',
//         25: 'twenty-five',
//         26: 'twenty-six',
//         27: 'twenty-seven',
//         28: 'twenty-eight',
//         29: 'twenty-nine',
//         31: 'thirty-one',
//         32: 'thirty-two',
//         33: 'thirty-three',
//         34: 'thirty-four',
//         35: 'thirty-five',
//         36: 'thirty-six',
//         37: 'thirty-seven',
//         38: 'thirty-eight',
//         39: 'thirty-nine',
//         40: 'twenty to',
//         50: 'ten to',
//         55: 'five to',
//     }
//     if (mins == '00') {
//         let mod = (Number(hours) % 12).toString().padStart(2, 0)
//         return dict[mod] + " o\'clock"
//     }
//     if (Number(mins) == 1) {
//         let mod = (Number(hours) % 12).toString().padStart(2, 0)
//         return dict[mins] + ' minute past ' + dict[mod]
//     }
//     if (mins == '15') {
//         let mod = (Number(hours) % 12).toString().padStart(2, 0)
//         return dict[mins] + ' ' + dict[mod]
//     }
//     if (mins == '45') {
//         let mod = (Number(hours) % 12 + 1).toString().padStart(2, 0)
//         return dict[mins] + ' ' + dict[mod]
//     }
//     if (Number(mins) < 30) {
//         let mod = (Number(hours) % 12).toString().padStart(2, 0)
//         return dict[mins] + ' minutes past ' + dict[mod]
//     }
//     if (Number(mins) > 30) {
//         let mod = (Number(hours) % 12 + 1).toString().padStart(2, 0)
//         let modMinus = (60 - Number(mins)).toString().padStart(2, 0)
//         if (modMinus == 1) {
//             return dict[modMinus] + ' minute to ' + dict[mod]
//         }
//         return dict[modMinus] + ' minutes to ' + dict[mod]
//     }
//     let mod = (Number(hours) % 12).toString().padStart(2, 0)
//     return dict[mins] + ' ' + dict[mod]

// }

function toHumanTime(timestring) {
    [hours, mins] = timestring.match(/\d+/g)

    let dict = { '00': 'twelve', '01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six', 
        '07': 'seven', '08': 'eight', '09': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
        '14': 'fourteen', '15': 'quarter', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
        '20': 'twenty', '21': 'twenty-one', '22': 'twenty-two', '23': 'twenty-three', '24': 'twenty-four',
        '25': 'twenty-five', '26': 'twenty-six', '27': 'twenty-seven', '28': 'twenty-eight', '29': 'twenty-nine',
        '30': 'half past', '45': 'quarter to'
    }

    let mod = (Number(hours) % 12).toString().padStart(2, 0)
    let modMinus = (60 - Number(mins)).toString().padStart(2, 0)
    let modPlus = (Number(hours) % 12 + 1).toString().padStart(2, 0)

    if (mins == '00')
        return dict[mod] + " o\'clock"
    if (Number(mins) == 1)
        return dict[mins] + ' minute past ' + dict[mod]
    if (mins == '15')
        return dict[mins] + ' past ' + dict[mod]
    if (Number(mins) < 30)
        return dict[mins] + ' minutes past ' + dict[mod]
    if (mins == '45')
        return dict[mins] + ' ' + dict[modPlus]

    if (Number(mins) > 30) {
        if (modMinus == 1) {
            return dict[modMinus] + ' minute to ' + dict[modPlus]
        }
        return dict[modMinus] + ' minutes to ' + dict[modPlus]
    }
    return dict[mins] + ' ' + dict[mod]
}

q = toHumanTime('05:28 pm') // twenty-eight minutes past five
q
q = toHumanTime('12:00') // twelve o\'clock
q
q = toHumanTime('03:45am') // quarter to four
q
q = toHumanTime('07:15') // quarter past seven
q
q = toHumanTime('23:30') // half past eleven
q
q = toHumanTime('00:01') // one minute past twelve
q
q = toHumanTime('05:38 pm') // twenty-eight minutes past five
q
q = toHumanTime('05:59 pm') // twenty-eight minutes past five
q