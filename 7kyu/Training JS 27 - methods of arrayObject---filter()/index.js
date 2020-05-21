// 7kyu - Training JS #27: methods of arrayObject---filter()

/* Write function countGrade which accepts 1 parameters (scores) as array of numbers.
Your task is to count the grade distribution of the scores, to return an object like this:
{S:888, A:888, B:888, C:888, D:888, X:888}

Grading rules:
Grade S: Full marks(score=100)
Grade A: score<100 and score>=90
Grade B: score<90 and score>=80
Grade C: score<80 and score>=60
Grade D: score<60 and score>=0
Grade X: score=-1(The cheating guy gets a score like that)

countGrade([50,60,70,80,90,100]) should return {S:1, A:1, B:1, C:2, D:1, X:0}
countGrade([65,75,,85,85,95,100,100]) should return {S:2, A:1, B:2, C:2, D:0, X:0}
countGrade([-1,-1,-1,-1,-1,-1]) should return {S:0, A:0, B:0, C:0, D:0, X:6} */

// const countGrade = (scores) => 
//     [['S', score => score == 100],
//      ['A', score => score >= 90 && score < 100],
//      ['B', score => score >= 80 && score < 90],
//      ['C', score => score >= 60 && score < 80],
//      ['D', score => score >= 0 && score < 60],
//      ['X', score => score == -1]]
//     .map(([grade, fn]) => [grade, scores.filter(fn)])
//     .reduce((res, [grade, array]) => (res[grade] = array.length, res), {})

// function countGrade(scores) {
//     return {
//         S: scores.filter(v => v == 100).length,
//         A: scores.filter(v => v >= 90 && v < 100).length,
//         B: scores.filter(v => v >= 80 && v < 90).length,
//         C: scores.filter(v => v >= 60 && v < 80).length,
//         D: scores.filter(v => v >= 0 && v < 60).length,
//         X: scores.filter(v => v == -1).length
//     }
// }

const countGrade = (scores) => (count = (fn) => scores.filter(v => fn(v)).length, {
    S: count(v => v == 100),
    A: count(v => v >= 90 && v < 100),
    B: count(v => v >= 80 && v < 90),
    C: count(v => v >= 60 && v < 80),
    D: count(v => v >= 0 && v < 60),
    X: count(v => v == -1)
})


q = countGrade([50, 60, 70, 80, 90, 100]) // {S:1, A:1, B:1, C:2, D:1, X:0}
q
q = countGrade([65, 75, , 85, 85, 95, 100, 100]) // {S:2, A:1, B:2, C:2, D:0, X:0}
q
q = countGrade([-1, -1, -1, -1, -1, -1]) // {S:0, A:0, B:0, C:0, D:0, X:6}
q