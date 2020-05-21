// 7kyu - Tail Swap

// function tailSwap(arr) {
//     let [a, b] = arr.map(v => v.split(':'))

//     return [ a[0] + ':' + b[1],
//              b[0] + ':' + a[1] ]
// }

// function tailSwap(arr) {
//     let [aa, ab] = arr[0].split(':')
//     let [ba, bb] = arr[1].split(':')

//     let a = aa + ':' + bb
//     let b = ba + ':' + ab

//     return [a, b]
// }


// function tailSwap(arr) {
//     let [aa, ab] = arr[0].split(':')
//     let [ba, bb] = arr[1].split(':')

//     return [aa +':'+ bb, ba +':'+ ab]
// }

// function tailSwap(arr) {
//     const [[a, b],[c, d]] = arr.map(x => x.split(':'))
//     return [`${a}:${d}`, `${c}:${b}`]
// }

function tailSwap(arr) {
    const [[a, b], [c, d]] = arr.map(v => v.split(':'))
    return [a +':'+ d, c +':'+ b]
}

// function tailSwap(arr) {
//     return [
//         /.*:/.exec(arr[0])[0] + /:.*/.exec(arr[1])[0].replace(':', ''),
//         /.*:/.exec(arr[1])[0] + /:.*/.exec(arr[0])[0].replace(':', '')
//     ]
// }

// const tailSwap = ([a, b], [c, d] = a.split `:`, [e, f] = b.split `:`) => [
//                   [c, f].join `:`, [e, d].join `:`
// ]


// const tailSwap = a => (a + '').replace(/(.+:)(.+),(.+:)(.+)/, '$1$4,$3$2').split(',')

// function tailSwap(arr) {
//     const [aa, ab] = arr[0].split(':')
//     const [ba, bb] = arr[1].split(':')
//     return [aa + ':' + bb, ba + ':' + ab]
// }

q = tailSwap(['abc:123', 'cde:456']) // ['abc:456', 'cde:123']
q
q = tailSwap(['a:12345', '777:xyz']) // ['a:xyz', '777:12345']
q