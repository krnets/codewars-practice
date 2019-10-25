const isDivisible = (n, x, y) => (n % x == 0) && (n % y == 0)


q = isDivisible(3, 3, 4) // false
q
q = isDivisible(12, 3, 4) // true
q
q = isDivisible(8, 3, 4) // false
q
q = isDivisible(48, 3, 4) // true
q