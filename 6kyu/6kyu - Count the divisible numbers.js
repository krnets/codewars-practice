// 6kyu - Count the divisible numbers

const divisibleCount = (x, y, k) => Math.floor(y / k) - Math.floor((x - 1) / k)

q = divisibleCount(6, 11, 2) //3
q