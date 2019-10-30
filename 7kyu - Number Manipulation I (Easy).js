// 7kyu - Number Manipulation I (Easy)

// function manipulate(num) {
//     let s = String(num)
//     let firstHalf = s.slice(0, Math.floor(s.length / 2))
//     let secondHalf = '0'.repeat(Math.ceil(s.length / 2))

//     return Number(firstHalf + secondHalf)
// }

function manipulate(num) {
    let s = String(num)
    let half = Math.floor(s.length / 2)
    return Number(s.slice(0, half) + '0'.repeat(s.length - half))
}

// function manipulate(num) {
//     let s = String(num)
//     let half = s.length >> 1
//     return Number(s.slice(0, half) + '0'.repeat(s.length - half))
// }

// function manipulate(num) {
//     let s = String(num)
//     return Number(s.slice(0, s.length >> 1) + '0'.repeat(s.length - (s.length >> 1)))
// }

function manipulate(num) {
    let str = `${num}`
    return +str.slice(0, str.length >> 1).padEnd(str.length, '0')
}

// const manipulate = n => +(n += '').slice(0, n.length >> 1).padEnd(n.length, '0')
// const manipulate = num => +([...String(num)].map((v, i, a) => i < (a.length-1) / 2 ? v : 0).join ``)
// const manipulate = num => +([...String(num)].map((v, i, a) => i < a.length >> 1 ? v : 0).join ``)

q = manipulate(192827764920) // 192827000000
q
q = manipulate(838473) // 838000
q
q = manipulate(8173648710293847) // 8173648700000000
q