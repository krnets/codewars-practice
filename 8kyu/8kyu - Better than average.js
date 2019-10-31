function betterThanAverage(classPoints, yourPoints) {
    return yourPoints > classPoints.reduce((a,b) => a + b, 0) / classPoints.length
}

// function betterThanAverage(classPoints, yourPoints) {
//     return classPoints.reduce((a, b) => a + b, 0) < yourPoints * classPoints.length
// }

q = betterThanAverage([2, 3], 5) // true);
q
q = betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75) // true);
q
q = betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 9) // false);
q