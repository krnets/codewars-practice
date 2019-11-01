// function capitalize(str) {
//     let evenCaps = str.split('').map((value, index) => index % 2 ? value : value.toUpperCase()).join ``
//     let oddCaps = str.split('').map((value, index) => index % 2 ? value.toUpperCase() : value).join ``

//     return [evenCaps, oddCaps]
// }

// const capitalize = s => [0, 1].map(r => [...s].map((v, i) => i % 2 == r ? v.toUpperCase() : v).join ``)

function capitalize(str) {
    return [[...str].map((char, i) => i % 2 == 0 ? char.toUpperCase() : char).join(''),
            [...str].map((char, i) => i % 2 != 0 ? char.toUpperCase() : char).join('')]
}

q = capitalize("abcdef") // ['AbCdEf', 'aBcDeF']
q
q = capitalize("codewars") // ['CoDeWaRs', 'cOdEwArS']
q
q = capitalize("abracadabra") // ['AbRaCaDaBrA', 'aBrAcAdAbRa']
q
q = capitalize("codewarriors") // ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
q