// 6kyu - Format a string of names like 'Bart, Lisa & Maggie'

// const list = names => {
//     return names.length == 0 ? '' :
//         names.length == 1 ? names[0].name :
//         names.length == 2 ? names[0].name + ' & ' + names[1].name :
//         names.length == 3 ? names[0].name + ', ' + names[1].name + ' & ' + names[2].name :
//         names.length == 5 ? names[0].name + ', ' + names[1].name + ', ' + names[2].name + ', ' + names[3].name + ' & ' + names[4].name :
//         '_'
// }

// function list(names) {
//     switch (names.length) {
//         case 0:
//             return ''
//         case 1:
//             return names[0].name
//         case 2:
//             return names[0].name + ' & ' + names[1].name
//         case 3:
//             return names[0].name + ', ' + names[1].name + ', ' + names[2].name
//         default:
//             return names[0].name + ', ' + names[1].name + ', ' + names[2].name + ', ' + names[3].name + ' & ' + names[4].name
//     }
// }

// function list(names) {
//     if (names == '') return ''
//     let ns = names.map(v => v.name)

//     return names.length == 1 ? ns + '' :
//         ns.slice(0, -1).join(', ') + ' & ' + ns.slice(-1)
// }

// function list(names) {
//     return names.reduce((prev, curr, i) => {
//         if (i == 0) return curr.name
//         else if (i == names.length - 1)
//             return prev + ' & ' + curr.name
//         else return prev + ', ' + curr.name
//     }, '')
// }

// const list = names => names.reduce((prev, curr, i) => {
//     if (i == 0) return curr.name
//     else if (i == names.length - 1)
//         return prev + ' & ' + curr.name
//     else return prev + ', ' + curr.name
// }, '')

// function list(names) {
//     let xs = names.map(p => p.name)
//     let x = xs.pop()
//     return xs.length ? xs.join(', ') + ' & ' + x : x || '' 
// }

// const list = (names) => names.map(v => v.name).join(', ').replace(/(.*),(.*)$/, "$1 &$2")
// const list = (names) => names.map(v => v.name).join(', ').replace(/^(.*)(, )(.*)$/, '$1 & $3')
// const list = (names) => names.map(v => v.name).join(', ').replace(/,\s([^,]+)$/, ' & $1')
// const list = (names) => names.map(e => e.name).join(', ').replace(/,(?=[^,]*$)/, ' &')
// const list = (names) => (ns = names.map(v => v.name), ns.concat(names.splice(-2).join(' & ')).join(', '))

q = list([{
    name: 'Bart'
}, {
    name: 'Lisa'
}, {
    name: 'Maggie'
}, {
    name: 'Homer'
}, {
    name: 'Marge'
}])
// 'Bart, Lisa, Maggie, Homer & Marge'
q
q = list([{
    name: 'Bart'
}, {
    name: 'Lisa'
}, {
    name: 'Maggie'
}])
// 'Bart, Lisa & Maggie'
q
q = list([{
    name: 'Bart'
}, {
    name: 'Lisa'
}])
// 'Bart & Lisa'
q
q = list([{
    name: 'Bart'
}])
// 'Bart'
q
q = list([])
// ''
q