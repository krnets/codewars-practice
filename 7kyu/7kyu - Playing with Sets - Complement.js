// 7kyu - Playing with Sets : Complement

/* Set objects are new JavaScript built-in objects defined since ECMAScript 2015
A Set lets you store unique values of any type. It comes with some useful methods like .add, .clear, .has . . . 
BUT some "Set operations" are missing, like . . . Complement
Two sets can be "subtracted". The relative complement of B in A, denoted by A \ B (or A − B), 
is the set of all elements that are members of A but not members of B. 
Note that it is valid to "subtract" members of a set that are not in the set, 
such as removing the element green from the set {1, 2, 3}; doing so has no effect.

  {1, 2} \ {1, 2} = ∅.
  {1, 2, 3, 4} \ {1, 3} = {2, 4}.

Create function diff getting 2 sets as arguments and returning a new Set as result of relative complement of second set in first.

A = new Set([1,2]);
B = new Set([2,3]);

diff(A,B) // -> {1}
diff(B,A) // -> {3}

Fundamentals | Sets | Arrays */

// function diff(s1, s2) {
//     let a1 = Array.from(s1)
//     let a2 = Array.from(s2)
//     return new Set(a1.filter(v => !a2.includes(v)))
// }


// const diff = (s1, s2) => new Set([...s1].filter(v => ![...s2].includes(v)))
// const diff = (s1, s2) => new Set(Array.from(s1).filter(v => !s2.has(v)))
const diff = (s1, s2) => new Set([...s1].filter(e => !s2.has(e)))

A = new Set([1, 2])
B = new Set([2, 3])

q = diff(A, B) // -> {1}
q
q = diff(B, A) // -> {3}
q

A = new Set([1, 2, 3, 4])
B = new Set([1, 3, 5, 7])
AB = new Set([2, 4])
BA = new Set([5, 7])

q = diff(A, A) // new Set(), "A - A == {}"
q
q = diff(A, B) // AB 
q
q = diff(B, A) // BA 
q
q = diff(A, B) instanceof Set // true, "A - B should be a Set too"
q