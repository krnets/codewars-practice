// const minValue = (nums) => +Array.from(new Set(nums)).sort((a,b) => a - b).join('')
// const minValue = (nums) => +[...new Set(nums)].sort().join``

const minValue = (values) => +values.sort((a,b) => a-b).filter((v, i) => values.indexOf(v) == i).join('')

const assertEquals = (fn, cmp) => fn == cmp

q = minValue([1, 3, 1]) // 13)
q
q = minValue([4, 7, 5, 7]) // 457)
q
q = assertEquals(minValue([1, 3, 1]), 13)
q
q = assertEquals(minValue([4, 7, 5, 7]), 457)
q
q = assertEquals(minValue([4, 8, 1, 4]), 148)
q
q = assertEquals(minValue([5, 7, 9, 5, 7]), 579)
q
q = assertEquals(minValue([6, 7, 8, 7, 6, 6]), 678)
q
q = assertEquals(minValue([5, 6, 9, 9, 7, 6, 4]), 45679)
q
q = assertEquals(minValue([1, 9, 1, 3, 7, 4, 6, 6, 7]), 134679)
q
q = assertEquals(minValue([3, 6, 5, 5, 9, 8, 7, 6, 3, 5, 9]), 356789)
q
q = assertEquals(minValue([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)
q
q = assertEquals(minValue([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)
q