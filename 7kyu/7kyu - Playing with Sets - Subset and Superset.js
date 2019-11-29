// 7kyu - Playing with Sets - Subset and Superset

/* If every member of set A is also a member of set B, then A is said to be a subset of B, 
written A ⊆ B (also pronounced "A is contained in B"). 
Equivalently, we can write B ⊇ A, read as "B is a superset of A", "B includes A", or "B contains A".

  {1, 3} ⊆ {1, 2, 3, 4}.
  {1, 2, 3, 4} ⊆ {1, 2, 3, 4}.

  {1, 2, 3, 4} ⊇ {1, 3}.
  {1, 2, 3, 4} ⊇ {1, 2, 3, 4}.

Create 2 functions:

    isSubsetOf getting 2 sets as arguments and returning true if 2d set contains all elements of 1st one.
    isSupersetOf getting 2 sets as arguments and returning true if 1st set contains all elements of 2d one. */

const isSubsetOf = (s1, s2) => [...s1].every(v => s2.has(v))

// const isSupersetOf = (s1, s2) => [...s2].every(v => s1.has(v))
const isSupersetOf = (s1, s2) => isSubsetOf(s2, s1)

A = new Set([1, 2]);
B = new Set([1, 2, 3]);

q = isSubsetOf(A, B) // -> true
q
q = isSubsetOf(B, A) // -> false
q
q = isSupersetOf(A, B) // -> false
q
q = isSupersetOf(B, A) // -> true
q

A1 = new Set([1, 2, 3])
A2 = new Set([3, 2, 1])
B = new Set([1, 2, 3, 4, 5])
X = new Set([1, 2, 4, 5, 6, 7])

q = isSubsetOf(A1, A1) // "A is contained in A" 
q
q = isSubsetOf(A1, A2) // "{1,2,3} is contained in {3,2,1}" 
q
q = isSubsetOf(A1, B) //  "{1,2,3} is contained in {1,2,3,4,5}" 
q
q = !isSubsetOf(A1, X) // "{1,2,3} is not contained in {1,2,4,5,6,7}" 
q
q = isSupersetOf(A1, A1) // "A includes A" 
q
q = isSupersetOf(A1, A2) // "{1,2,3} includes {3,2,1}" 
q
q = isSupersetOf(B, A1) // "{1,2,3} includes {1,2,3,4,5}" 
q
q = !isSupersetOf(A1, X) // "{1,2,3} doesnt include {1,2,4,5,6,7}" 
q