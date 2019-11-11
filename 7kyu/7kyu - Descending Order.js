// 7kyu - Descending Order

const descendingOrder = n => +[...String(n)].sort((a, b) => b - a).join ``


q = descendingOrder(0) // 0
q
q = descendingOrder(1) // 1
q
q = descendingOrder(123456789) // 987654321
q