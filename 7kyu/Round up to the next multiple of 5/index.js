// 7kyu - Round to the next multiple of 5


// const roundToNext5 = n => n < 1 ? 0 :
//     (Math.round(n % 5) == 0 ? n :
//         Math.round(n % 5) == 1 ? n + 4 :
//         Math.round(n % 5) == 2 ? n + 3 :
//         Math.round(n % 5) == 3 ? n + 2 :
//         Math.round(n % 5) == 4 ? n + 1 : 0)

// function roundToNext5(n) {
//     if (n == 0 || n == -1) return 0
//     if (Math.round(n % 5) == 0) return n
//     for (let i = 0, j = 5; i < 6; i++, j--) {
//         if (n > 0 && Math.round(n % 5) == i)
//             return n + j
//         if (n < 0 && Math.round(n % 5) == -i)
//             return n + i
//     }
// }


// function roundToNext5(n) {
//     while (n % 5 !== 0) n++;
//     return n;
// }

// function roundToNext5(n) {
//     while (n % 5) n++
//     return n
// }

const roundToNext5 = n => Math.ceil(n / 5) * 5
// const roundToNext5 = n => n % 5 ? roundToNext5(n + 1) : n
// const roundToNext5=ﾠ=>ﾠ% - ~ - ~ - ~ - ~ ! !ﾠ? - ~ (ﾠ/ - ~ - ~ - ~ - ~ ! !ﾠ- (ﾠ< ! !ﾠ) ) * - ~ - ~ - ~ - ~ ! !ﾠ:ﾠ
// const roundToNext5 = ﾠ => ﾠ % -~-~-~-~!!ﾠ ? -~(ﾠ / -~-~-~-~!!ﾠ - (ﾠ < !!ﾠ)) * -~-~-~-~!!ﾠ : ﾠ
// const roundToNext5 = n => n - n % 5 + (n % 5 > 0 ? 5 : 0)
// const roundToNext5 = n => (Math.ceil((n / 10) * 2) * 10) / 2
// const roundToNext5 = n => n > 0 ? n + 5 - (n % 5 || 5) : n - n % 5

q = roundToNext5(0) // 0
q
q = roundToNext5(1) // 5 
q
q = roundToNext5(3) // 5
q
q = roundToNext5(5) // 5
q
q = roundToNext5(7) // 10
q
q = roundToNext5(39) // 40
q
q = roundToNext5(-5) // -5
q
q = roundToNext5(20) // 20
q
q = roundToNext5(-1139908) // -1139905
q
q = roundToNext5(-2339217) // -2339215
q