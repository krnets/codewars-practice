// 7kyu - Initialize my name

/* Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).
Examples

'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis' */

// function initializeNames(name) {
//     let res = []
//     let arr = name.split(' ')
//     if (arr.length > 2) {
//         res.push(arr[0])
//         res.push(arr.map(v => v[0] + '.').slice(1, -1))
//         res.push(arr.slice(-1))
//     } else {
//         return name
//     }
//     return [].concat(...res).join(' ')
// }

// function initializeNames(name) {
//     let arr = name.split(' ')
//     for (let i = 1; i < arr.length - 1; i++)
//         arr[i] = arr[i].charAt() + '.'
//     return arr.join(' ')
// }

const initializeNames = (name) => name.replace(/ (\w)\w*(?= )/g, ' $1.')

q = initializeNames('Jack Ryan') // 'Jack Ryan'
q
q = initializeNames('Lois Mary Lane') // 'Lois M. Lane'
q
q = initializeNames('Dimitri') //  'Dimitri'
q
q = initializeNames('Alice Betty Catherine Davis') // 'Alice B. C. Davis'
q