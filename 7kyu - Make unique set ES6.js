const makeUnique=arr=>[...new Set(arr)]

q = makeUnique([]) // []
q
q = makeUnique([1, 2, 3, 3]) // [1, 2, 3]
q
q = makeUnique(['A', 'A', 0]) // ['A', 0]
q