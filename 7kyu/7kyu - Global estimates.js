// 7kyu - Global estimates

/* Lately, feature requests have been piling up and you need a way to make global estimates of the time 
it would take to implement them all. If you estimate feature A to take 4 to 6 hours to implement, 
and feature B to take 2 to 5 hours, then in the best case it will only take you 6 (4 + 2) hours to 
implement both features, and in the worst case it will take you 11 (6 + 5). In the average case, it will take you 8.5 hours.

To help you streamline the estimation process, write a function that returns a tuple (JS: array) 
of the global best case, average case and worst case given a tuple of tuples (JS: array of arrays) 
representing best case and worst case guesses.

estimates = ((1, 2), (3, 4))
global_estimate(estimates) -> (4, 5, 6)

estimates = [[1, 2], [3, 4]]
globalEstimate(estimates) -> [4, 5, 6]

Don't worry about rounding or invalid input. */

function globalEstimate(estimates) {
    let min = estimates.map(v => Math.min(...v)).reduce((a, b) => a + b, 0)
    let max = estimates.map(v => Math.max(...v)).reduce((a, b) => a + b, 0)
    let avg = (min + max) / 2
    return [min, avg, max]
}

q = globalEstimate([[1, 2],[3, 4]]) // [4, 5, 6]
q
q = globalEstimate( [[0, 1],[0, 10]]) //  [0, 5.5, 11]]
q
q = globalEstimate([[0, 0],[0, 0]]) // [0, 0, 0]
q
q = globalEstimate([[1, 1]]) // [1, 1, 1]
q
q = globalEstimate([ [1, 3], [1, 4], [1, 5] ]) // [3, 7.5, 12]
q