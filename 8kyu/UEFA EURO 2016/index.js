// 8kyu - UEFA EURO 2016

// function uefaEuro2016(teams, scores) {
//     let res = `At match ${teams[0]} - ${teams[1]}, `
//     if (scores[0] < scores[1]) res += `${teams[1]} won!`
//     else if (scores[0] > scores[1]) res += `${teams[0]} won!`
//     else res += `teams played draw.`
//     return res
// }

function uefaEuro2016(teams, scores) {
    return `At match ${teams[0]} - ${teams[1]}, ${scores[0] == scores[1] ? 'teams played draw.' : teams[+(scores[0] < scores[1])] + ' won!'}`
}

q = uefaEuro2016(['Germany', 'Ukraine'], [2, 0]) // "At match Germany - Ukraine, Germany won!"
q
q = uefaEuro2016(['Belgium', 'Italy'], [0, 2]) // "At match Belgium - Italy, Italy won!"
q
q = uefaEuro2016(['Portugal', 'Iceland'], [1, 1]) // "At match Portugal - Iceland, teams played draw."
q