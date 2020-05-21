// 7kyu - Sort array by last character

/* Write a function sortMe to sort a given array by last character of the element.
Element can be an integer or a string.

sortMe(['acvd','bcc']) => ['bcc','acvd']

As the last characters of strings are 'd' and 'c'. As, 'c' comes before 'd', sorting by last character will give ['bcc', 'acvd']
If two elements don't differ in the last character, that then they should be sorted by the order they come in the array. */

// const sortMe = arr =>
//     arr
//         .map((x, i) => [x, x.toString().slice(-1), i])
//         .sort((a, b) => a[1].localeCompare(b[1]) || a[2] - b[2])
//         .map(x => x[0])

// const _ = require('lodash')
// const sortMe = arr => _.sortBy(arr, _.flow(_.toString, _.last))

const sortMe = arr => require('lodash').sortBy(arr, v => String(v).slice(-1))

q = sortMe(['acvd', 'bcc']) // ['bcc','acvd']
q
q = sortMe(['14', '13']) // ["13", "14"]
q
q = sortMe(['asdf', 'asdf', '14', '13']) // ["13", "14", "asdf", "asdf"]
q
q = sortMe(['bsde', 'asdf', 14, '13']) // ["13", 14, "bsde", "asdf"]
q
q = sortMe(['asdf', 14, '13', 'asdf']) // ["13", 14, "asdf", "asdf"]
q
q = sortMe(['xxxf', 'aaaf', 'kf', 'f', 'ooooof']) // ["xxxf","aaaf","kf","f","ooooof"]
q
q = sortMe(['xdxf', 'xcxf', 'xbxf', 'xaxf']) // ["xdxf","xcxf","xbxf","xaxf"]
q
q = sortMe(['xdxf', 'xcxa', 'xbxf', 'xaxf']) // ["xcxa","xdxf","xbxf","xaxf"]
q
