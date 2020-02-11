// 7kyu - Average Scores

/* Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. 
You are not allowed to use any loops (including for, for/in, while, and do/while loops). */

const average = (scores) => Math.round(scores.reduce((a, b) => a + b, 0) / scores.length)

scores = [49, 3, 5, 300, 7];
q = average(scores) // 73
q

scores = [90, 98, 89, 100, 100, 86, 94];
q = average(scores) // 94
q