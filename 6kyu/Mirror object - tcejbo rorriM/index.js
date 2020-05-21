// 6kyu - Mirror object - tcejbo rorriM

/* Mirror - Mirror

Can you mirror the properties on an object?

Given an object with properties with no value

abc: -
arara: -
xyz: -

Return a new object that have the properties with its mirrored key!

abc: cba
arara: arara
xyz: zyx

"You cannot change the original object, because if you did that the reflection would change." */

// const mirror = obj => {
//     let clone = Object.assign({}, obj)
//     for (let key in clone)
//         clone[key] = [...key].reverse().join('')
//     return clone
// }

// const mirror = obj => {
//     let clone = {...obj}
//     for (let key in clone)
//         clone[key] = [...key].reverse().join('')
//     return clone
// }

const mirror = obj => Object.keys(obj).reduce((m, k) => (m[k] = [...k].reverse().join(''), m), {})

const expected = {
    abc: 'cba',
    arara: 'arara',
};

const actual = mirror({
    abc: undefined,
    arara: undefined,
});

q = mirror(expected)
q
q = mirror(expected).abc
q
q = mirror(expected).arara
q

// q = expected.abc
// q
// q = actual.abc
// q
// Object.keys(expected).forEach(k => log(k));

// assert.deepEqual(actual, expected);