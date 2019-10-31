// 6kyu - Adding Binary Numbers

// function add(a, b) {
//     a = a.split('').reverse()
//     b = b.split('').reverse()
//     let result = ''
//     let temp = 0

//     while (a.length || b.length || temp) {
//         temp += (~~a.shift()) + (~~b.shift())
//         let mod = temp % 2
//         result = mod + result
//         temp = temp > 1
//     }
//     return +result ? result.replace(/^0+/, '') : '0'
// }

function add(a, b) {
    a = [...a]
    b = [...b]
    let result = ''
    let temp = 0
    while (a.length || b.length || temp) {
        temp += ~~a.pop() + ~~b.pop()
        result = temp % 2 + result
        temp = temp > 1
    }
    return +result ? result.replace(/^0+/, '') : '0'
}

q = add('111', '10') // '1001'
q
q = add('1101', '101') // '10010'
q
q = add('1101', '10111') // '100100'
q