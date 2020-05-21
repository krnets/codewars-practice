// 6kyu - Round by 0.5 steps

/* Round any given number to the closest 0.5 step */

// const solution = n => Math.round(n * 10 / 5) * 5 / 10
const solution = n => Math.round(n * 2) / 2

q = solution(4.2) // 4
q
q = solution(4.4) // 4.5
q
q = solution(4.6) // 4.5
q
q = solution(4.8) // 5
q