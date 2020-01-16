// 8kyu - Twice as old

/* Your function takes two arguments:

    current father's age (years)
    current age of his son (years)

Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). */

function twiceAsOld(dadYearsOld, sonYearsOld) {
    return Math.abs(dadYearsOld - sonYearsOld * 2)
}


q = twiceAsOld(36, 7) // 22
q
q = twiceAsOld(55, 30) // 5
q
q = twiceAsOld(42, 21) // 0
q
q = twiceAsOld(22, 1) // 20
q
q = twiceAsOld(29, 0) // 29
q