// function unluckyDays(year) {
//     // return Array.from({length: 12}).filter((_,index) => new Date(year, index, 13).getDay() == 5).length
//     // let a = new Date(2015,0,13)//.getDay()
//     let array = [...Array(12).keys()]
//     // array
//     // let b = array.filter((_, month) => new Date(year, month, 13).getDay() == 5)
//     // b
//     // return b
//     return [...Array(12).keys()]
//             .filter((_, month) => new Date(year, month, 13).getDay() == 5)
//             .length
// }


function unluckyDays(year) {
    return [...Array(12)]
            .reduce((total, _, month) => 
                total + (new Date(year, month, 13).getDay() == 5), 0)
            // .reduce((count, _, month) => count + +(new Date(year, month, 13).getDay() === 5), 0)
}

q = unluckyDays(2015) // 3, "should be: 3"
q
q = unluckyDays(1586) // 1, "should be: 1"
q
q = unluckyDays(1001) // 3, "should be: 3"
q
q = unluckyDays(2819) // 2, "should be: 2"
q
q = unluckyDays(2792) // 2, "should be: 2"
q
q = unluckyDays(2723) // 2, "should be: 2"
q
q = unluckyDays(1909) // 1, "should be: 1"
q
q = unluckyDays(1812) // 2, "should be: 2"
q
q = unluckyDays(1618) // 2, "should be: 2"
q
q = unluckyDays(2132) // 1, "should be: 1"
q
q = unluckyDays(2065) // 3, "should be: 3"
q