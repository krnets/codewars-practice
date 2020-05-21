const nthSmallest = (arr, pos) => arr.sort((a, b) => a - b)[pos - 1]

q = nthSmallest([3, 1, 2], 2) // 2
q
q = nthSmallest([15, 20, 7, 10, 4, 3], 3) // 7
q
q = nthSmallest([-5, -1, -6, -18], 4) // -1
q
q = nthSmallest([-102, -16, -1, -2, -367, -9], 5) // -2
q
q = nthSmallest([2, 169, 13, -5, 0, -1], 4) // 2
q