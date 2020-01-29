// 7kyu - Driving School Series #1 

/* Every month, a random number of students take the driving test at Fast & Furious(F&F) Driving School. 
To pass the test, a student cannot accumulate more than 18 demerit points.

At the end of the month, F&F wants to calculate the average demerit points accumulated by ONLY the students 
who have passed,rounded to the nearest integer.

Write a function which would allow them to do so. If no students passed the test that month, 
return 'No pass scores registered.'.

[10,10,10,18,20,20] --> 12

The maximum number of demerit points a student can score before the tester calls it a day is 40. */

function passed(list) {
    let points = list.filter(v => v <= 18)
    return Math.round(points.reduce((a, b) => a + b, 0) / points.length) || 'No pass scores registered.'
}

q = passed([10, 10, 10, 18, 20, 20]) // 12
q
q = passed([21, 22, 24]) // 'No pass scores registered.'
q
q = passed([3, 22, 9, 13, 20, 18, 2, 14, 20, 8, 23, 12, 7, 21, 21, 19, 20, 11, 18, 7, 13, 22, 11, 20, 9]) // 10
q
q = passed([19, 16, 8, 11, 25, 10, 29, 22, 23]) // 11
q