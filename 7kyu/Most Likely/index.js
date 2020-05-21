// 7kyu - Most Likely

/* Create a function mostLikely which compares two probabilities, 
returning true if the first one is most likely otherwise false.
For this exercise probability is expressed as two numbers separated 
by a colon e.g. a probability of 1 in 3 will be 1:3.

mostLikely('1:3','1:2') will return false as 1 in 3 is less likely than 1 in 2. */

// const mostLikely = (prob1, prob2) => eval(prob1.replace(':', '/')) > eval(prob2.replace(':', '/'))
// const mostLikely = (...ps) => eval(ps.join('>').replace(/:/g, '/'));
const mostLikely = (prob1, prob2) => [prob1, prob2].map(p => p.split(':')).reduce((a, b) => a[0] / a[1] > b[0] / b[1])

// function mostLikely(prob1, prob2) {
//     let [p1, p2] = [prob1, prob2].map(p => p.split(':').reduce((a, b) => a / b))
//     return p1 > p2
// }

// function mostLikely(prob1, prob2) {
//     [ [a, b], [c, d] ] = [prob1, prob2].map(p => p.split(':'))
//     return a / b > c / d
// }


q = mostLikely('1:3', '1:2') // false
q