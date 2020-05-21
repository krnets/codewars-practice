// 8kyu - Calculate BMI

/* Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese" */


function bmi(weight, height) {
    let index = weight / Math.pow(height, 2)
    return index > 30 ? 'Obese' : index > 25 ? 'Overweight' : index > 18.5 ? 'Normal' : 'Underweight'
}

q = bmi(80, 1.80) // "Normal"
q
q = bmi(50, 1.80) // "Underweight"
q
q = bmi(80, 1.80) // "Normal"
q
q = bmi(90, 1.80) // "Overweight"
q
q = bmi(110, 1.80) // "Obese"
q
q = bmi(50, 1.50) // "Normal"
q