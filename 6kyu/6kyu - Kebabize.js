// 6kyu - Kebabize

/* Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

    the returned string should only contain lowercase letters

Fundamentals | Strings */

// function kebabize(str) {
//     str = str.replace(/\d/g, '')
//     let res = str[0] || ''
//     for (let i = 1; i < str.length; i++) {
//         if (str[i].toUpperCase() == str[i])
//             res += '-'
//         res += str[i]
//     }
//     return res.toLowerCase()
// }

// function kebabize(str) {
//     return str.replace(/[^a-z]/ig, '').
//     replace(/^[A-Z]/, c => c.toLowerCase()).
//     replace(/[A-Z]/g, c => `-${c.toLowerCase()}`);
// }

// const kebabize = (str) => str.replace(/\d/g, '').replace(/(.)(?=[A-Z])/g, '\$1-').toLowerCase()
// const kebabize = (str) => str.replace(/\d/g, '').replace(/\B[A-Z]/g, (x) => '-' + x).toLowerCase()
const kebabize = str => str.replace(/\d/g, '').replace(/(\B[A-Z])/g, '-$1').toLowerCase()

q = kebabize('myCamelCasedString') // 'my-camel-cased-string'
q
q = kebabize('myCamelHas3Humps') // 'my-camel-has-humps'
q