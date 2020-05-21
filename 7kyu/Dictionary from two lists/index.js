// 7kyu - Dictionary from two lists

// function createDict(keys, values) {
//     let dict = {}
//     keys.forEach((k, i) => values[i] == undefined ? dict[k] = null : dict[k] = values[i])
//     return dict
// }

// const createDict = (keys, values, dict = {}) => (keys.forEach((k,i) => values[i] == undefined ? dict[k] = null : dict[k] = values[i]; dict)

const createDict = (keys, values) => keys.reduce((dict, k, i) => (dict[k] = i in values ? values[i] : null, dict), {})
// const createDict = (keys, values) => keys.reduce((dict, k, i) => (dict[k] = i < values.length ? values[i] : null, dict), {})


q = createDict(['a', 'b', 'c'], [1, 2, 3])
q
// {'a': 1, 'b': 2, 'c': 3}
q = createDict(['a', 'b', 'c'], [1, 2, 3, 4])
q
// {'a': 1, 'b': 2, 'c': 3}
q = createDict(['a', 'b', 'c', 'd'], [1, 2, 3])
q
// {'a': 1, 'b': 2, 'c': 3, 'd':null}