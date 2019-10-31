// 7kyu - Complete The Pattern 7 - Cyclical Permutation

const pattern = n => Array.from({ length: n }, ((_, i) => Array.from({ length: n }, ((_, j) => (i + j) % n + 1)).join``)).join('\n')

q = pattern(4) // "1234\n2341\n3412\n4123"
q
q = pattern(7) // "1234567\n2345671\n3456712\n4567123\n5671234\n6712345\n7123456"
q
q = pattern(1) // "1"
q
q = pattern(0) // ""
q
q = pattern(-25) // ""
q