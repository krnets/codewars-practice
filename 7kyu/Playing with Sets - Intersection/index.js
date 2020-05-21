// 7kyu - Playing with Sets : Intersection

/* A new set can be constructed by determining which members two sets have "in common". 
The intersection of A and B, denoted by A ∩ B, is the set of all things that are members of 
both A and B. If A ∩ B = ∅, then A and B are said to be disjoint.

  {1, 2} ∩ {1, 2} = {1, 2}.
  {1, 2} ∩ {2, 3} = {2}.

Create function inter getting 2 sets as arguments and returning a new Set as result of intersection of these 2 sets. */

// const inter = (s1, s2) => new Set([...s1].filter(v => s2.has(v)))

function inter(s1, s2) {
    const s3 = new Set()
    for (const item of s1)
        if (s2.has(item))
            s3.add(item)
    return s3
}

A = new Set([1, 2])
B = new Set([2, 3])
C = new Set([2])
AB = inter(A, B)

q = inter(A, A) // A, "A inter A == A"
q
q = AB // C 
q;
[...AB].sort();
[...inter(B, A)].sort() // "A inter B == B inter A" 
q
q = AB instanceof Set // true, "A inter B should be a Set too"
q