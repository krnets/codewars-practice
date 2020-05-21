// 7kyu - Playing with Sets : Union

/* Set objects are new JavaScript built-in objects defined since ECMAScript 2015

A Set lets you store unique values of any type. It comes with some useful methods like .add, .clear, .has . . . 
BUT some "Set operations" are missing, like . . . Union

Two sets can be "added" together. The union of A and B, denoted by A ∪ B, is the set of all things that are members of either A or B.

  {1, 2} ∪ {1, 2} = {1, 2}.
  {1, 2} ∪ {2, 3} = {1, 2, 3}.
  {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}

Create function union getting 2 sets as arguments and returning a new Set as result of union of these 2 sets.

A = new Set([1,2]);
B = new Set([2,3]);

C = union(A,B) // -> {1,2,3} */

// const union = (s1, s2) => new Set(Array.from(s1).concat(Array.from(s2)))
// const union = (s1, s2) => new Set([...s1], [...s2])

function union(s1, s2) {
    const s3 = new Set()
    for (const item of s1) s3.add(item)
    for (const item of s2) s3.add(item)
    return s3
}

A = new Set([1, 2]), B = new Set([2, 3]), C = new Set([1, 2, 3]);

q = union(A, A) // A, "A ∪ A == A"
q
q = union(A, B) // C 
q
q = [...union(A, B)].sort() // [...union(B,A)].sort() // "A ∪ B == B ∪ A" 
q
q = union(A, B) instanceof Set // true, "A ∪ B should be a Set too"
q