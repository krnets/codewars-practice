// 6kyu - Multiples of 3 or 5

// const solution = number => Array(number - 1).fill().map((_, i) => i + 1).filter(v => v % 3 == 0 || v % 5 == 0).reduce((a, b) => a + b, 0)
// const solution = number => Number.isInteger(number) ? Array(Math.abs(number)).fill().map((_, i) => i).reduce((a, b) => a + (b % 3 == 0 || b % 5 == 0 ? b : 0), 0) : 0
// const solution = number => Array(Math.abs(number)).fill().map((_, i) => i)
//                                     .reduce((a, b) => a + (b % 3 == 0 || b % 5 == 0 ? b : 0), 0)

function solution(number) {
    for (var sum = 0, i = 0; i < number; i++)
        if (i % 3 == 0 || i % 5 == 0)
            sum += i
    return sum
}

q = solution(10) // 23
q
q = solution(2)
q