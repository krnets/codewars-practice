/* 8kyu - Cat years, Dog years

Return respective ages as [humanYears,catYears,dogYears]
    humanYears >= 1
    humanYears are whole numbers only

Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that */

function humanYearsCatYearsDogYears(humanYears) {
    let catYears = (humanYears) => {
        for (var res = 0, i = humanYears; i > 0; i--)
            res += (i > 2 ? 4 : i > 1 ? 9 : 15)
        return res
    }
    let dogYears = (humanYears) => {
        for (var res = 0, i = humanYears; i > 0; i--)
            res += (i > 2 ? 5 : i > 1 ? 9 : 15)
        return res
    }
    return [humanYears, catYears(humanYears), dogYears(humanYears)]
}

q = humanYearsCatYearsDogYears(1) // [1,15,15]
q
q = humanYearsCatYearsDogYears(2) // [2,24,24]
q
q = humanYearsCatYearsDogYears(10) // [10,56,64]
q