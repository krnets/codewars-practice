// 7kyu - Playing with Sets : Symmetric difference

/* The symmetric difference is an extension of the complement. 
Denoted A Δ B, it's the set of all element of A which are not element of B 
and all element of B which are not element of A.

{7,8,9,10} Δ {9,10,11,12} = {7,8,11,12}.

Create function symDiff getting 2 sets as arguments and returning a new Set as result of symmetric difference of these sets.

A = new Set([1,2,3]);
B = new Set([2,3,4]);

symDiff(A,B) // -> {1,4}

Note: as I've got some problem outputting "Δ" in tests, I will use "^" instead of it. */

// function symDiff(s1, s2) {
//     let common = [...s1].filter(v => s2.has(v))
//     return new Set([...s1, ...s2].filter(v => !common.includes(v)))
// }

// function symDiff(s1, s2) {
//     let common = [...s1].filter(v => s2.has(v))
//     let merged = new Set([...s1, ...s2])
//     for (let v of merged)
//         if (common.includes(v))
//             merged.delete(v)
//     return merged
// }

const symDiff = (s1, s2) => new Set([...s1, ...s2].filter(v => s1.has(v) ^ s2.has(v)))

// function symDiff(s1, s2) {
//     let diff = (s1, s2) => new Set([...s1].filter(v => !s2.has(v)))
//     let union = (s1, s2) => new Set([...s1, ...s2])
//     return union(diff(s1, s2), diff(s2, s1))
// }

A = new Set([1, 2, 3, 4])
B = new Set([1, 3, 5, 7])
C = new Set([2, 4, 5, 7])

q = symDiff(A, A) // new Set()
q
q = symDiff(A, B) // C 
q
q = new Set([...symDiff(B, A)].sort()) // C 
q
q = symDiff(A, B) instanceof Set // true, "A ^ B should be a Set too"
q