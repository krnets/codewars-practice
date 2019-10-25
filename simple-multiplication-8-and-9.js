// const simpleMultiplication = n => n % 2 == 0 ? n * 8 : n * 9
const simpleMultiplication = n => (n << 3) + (n & 1) * n;


a = 5 << 3
a
b = (5 & 1) * 5 
b 
c = a + b
c


q = simpleMultiplication(2) // 16
q
q = simpleMultiplication(1) // 9
q
q = simpleMultiplication(8) // 64
q
q = simpleMultiplication(4) // 32
q
q = simpleMultiplication(5) // 45
q