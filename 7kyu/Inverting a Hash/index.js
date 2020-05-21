// 7kyu - Inverting a Hash

/* Given a Hash made up of keys and values, invert the hash by swapping them.

Given:
  { a: '1',
    b: '2',
    c: '3' }
Return:
  { 1: 'a',
    2: 'b',
    3: 'c' }

Given:
  { foo:   'bar',
    hello: 'world' }
Return:
  { bar:   'foo',
    world: 'hello' }

    Keys and values may be of any type appropriate for use as a key.
    All hashes provided as input will have unique values, so the inversion is involutive. In other words, do not worry about identical values stored under different keys. */

// function invertHash(hash) {
//     let arr = Object.entries(hash);
//     return arr.reduce((obj, a) => (obj[a[1]] = a[0], obj), {});
// }

// const invertHash = (hash, arr = Object.entries(hash)) => arr.reduce((obj, a) => (obj[a[1]] = a[0], obj), {})
// const invertHash = (hash) => Object.entries(hash).reduce((obj, a) => (obj[a[1]] = a[0], obj), {})
// const invertHash = (hash) => Object.entries(hash).reduce((obj, key) => (obj[key[1]] = key[0], obj), {})
// const invertHash = (hash) => Object.keys(hash).reduce((obj, key) => (obj[hash[key]] = key, obj), {})
// const invertHash = (hash) => Object.entries(hash).reduce((obj, [val, key]) => Object.assign(obj, {[key]: val}), {})
const invertHash = (hash) => Object.entries(hash).reduce((obj, [val, key]) => (obj[key] = val, obj), {})

q = invertHash({ hello: 'world' }) // { world: 'hello' });
q
q = invertHash({ a: '1', b: '2', c: '3' }) // { 1: 'a', 2: 'b', 3: 'c' });
q