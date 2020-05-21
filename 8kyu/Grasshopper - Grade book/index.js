/* Grade book

Complete the function so that it finds the mean of the 
three scores passed to it and 
returns the letter value associated with that grade.

Numerical Score 	Letter Grade
90 <= score <= 100 	'A'
80 <= score < 90 	'B'
70 <= score < 80 	'C'
60 <= score < 70 	'D'
0 <= score < 60 	'F'

Tested values are all between 0 and 100. 
Theres is no need to check for negative values 
or values greater than 100. */

function getGrade(s1, s2, s3) {
    let score = Math.floor((s1 + s2 + s3) / arguments.length);

    return score >= 90 ? 'A' :
           score >= 80 ? 'B' :
           score >= 70 ? 'C' :
           score >= 60 ? 'D' : 'F'
}

q = getGrade(95, 90, 93) // 'A'
q
q = getGrade(100, 85, 96) // 'A'
q
q = getGrade(92, 93, 94) // 'A'
q
q = getGrade(72, 33, 94) // 'A'
q
q = getGrade(42, 33, 94) // 'A'
q
q = getGrade(42, 33, 54) // 'A'
q