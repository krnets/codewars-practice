const maxProduct = (numbers, size) => numbers.sort((a, b) => b - a).slice(0, size).reduce((prev, curr) => prev * curr, 1)

q = maxProduct([4, 3, 5], 2) // 20
q
// q = maxProduct([10,8,7,9], 3) // 720
// q
// q = maxProduct([8,6,4,6], 3) // 288
// q
// q = maxProduct([10,2,3,8,1,10,4], 5) // 9600
// q
q = maxProduct([13, 12, -27, -302, 25, 37, 133, 155, -14], 5) // 247895375
q
// q = maxProduct([-4,-27,-15,-6,-1], 2) // 4
// q
// q = maxProduct([-17,-8,-102,-309], 2) // 136
// q
// q = maxProduct([10,3,-27,-1], 3) // -30
// q
// q = maxProduct([14,29,-28,39,-16,-48], 4) // -253344
// q
// q = maxProduct([1], 1) // 1
// q