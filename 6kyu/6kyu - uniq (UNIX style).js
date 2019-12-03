// 6kyu - uniq (UNIX style)

/* Implement the uniq() function which behaves like the uniq command in UNIX. 
It takes as input an array and returns an array in which all duplicate elements 
following each other have been reduced to one instance. */

const uniq = a => a.filter((v, i) => i == 0 || v != a[i - 1])
// const uniq = a => a.filter((v, i) => !i || !(v == a[i - 1]))

// const uniq = a => a.reduce((o, v, i) => { if (!i || a[i - 1] != v) o.push(v); return o; }, [])
// const uniq = a => a.reduce((o, v, i) => (!i || a[i - 1] != v) ? o.concat(v) : o, [])
// const uniq = a => !a.length ? [] : a.slice(1).reduce((acc, x) => x == acc[acc.length - 1] ? acc : [...acc, x], [a[0]]);

// function uniq(a) {
//     for (let i = 0; i < a.length - 1; i++)
//         if (a[i] == a[i + 1]) {
//             a.splice(i, 1)
//             i--
//         }
//     return a
// }


q = uniq(['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c']) // -> returns ['a','b','c','a','b','c']
q
q = uniq(['a', 'a', 'b', undefined, 'c', 'a', 'b', 'c'])
q