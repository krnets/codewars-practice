// 7kyu - Sum of a nested list

// import _ from 'lodash'
// const sumNested = arr => _(arr).flattenDeep().sum()

// with custom deep flatten:
const flatten = a => a.reduce((flat, i) => {
    if (Array.isArray(i)) 
        return flat.concat(flatten(i)); 
    return flat.concat(i)},[])

const sumNested = arr => flatten(arr).reduce((a, b) => a + b, 0)

// single line ES6 version using built-in functions only:
// const sumNested = arr => arr.reduce((a, b) => a + (Array.isArray(b) ? sumNested(b) : b), 0)


let q = sumNested([[1, [3, [4, [5, 6]]]],[2]])
q
q = sumNested([1]) // 1
q
q = sumNested([1, 2, 3, 4]) // 10
q
q = sumNested([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) // 55
q
q = sumNested([]) // 0
q
q = sumNested([[1],[]]) // 1
q
q = sumNested([[1, 2, 3, 4]]) // 10
q
q = sumNested([1, [1],[[1]],[[[1]]]]) // 4
q
q = sumNested([1, [1],[1, [1]],[1, [1],[1, [1]]]]) // 8
q
q = sumNested([[[[],[],[[[[[[[[[[]]]]]]]]]]],[],[],[[[],[[]]]]],[]]) // 0
q