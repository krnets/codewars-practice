// 7kyu - The Office I - Outed

// function outed(meet, boss) {
//     let a = Object.values(meet).reduce((a, b) => a + b) + meet[boss]
//     let b = Object.keys(meet).length
//     return a / b <= 5 ? 'Get Out Now!' : 'Nice Work Champ!'
// }

function outed(meet, boss) {
    let teamSize = Object.keys(meet).length
    let avgHappiness = Object.values(meet).reduce((a, b) => a + b) + meet[boss]
    return (avgHappiness / teamSize) > 5 ? 'Nice Work Champ!' : 'Get Out Now!'
}

q = outed({ 'tim': 0, 'jim': 2, 'randy': 0, 'sandy': 7, 'andy': 0, 'katie': 5, 'laura': 1, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 0 }, 'laura') 
// 'Get Out Now!'
q
q = outed({ 'tim': 1, 'jim': 3, 'randy': 9, 'sandy': 6, 'andy': 7, 'katie': 6, 'laura': 9, 'saajid': 9, 'alex': 9, 'john': 9, 'mr': 8 }, 'katie') 
// 'Nice Work Champ!'
q
q = outed({ 'tim': 2, 'jim': 4, 'randy': 0, 'sandy': 5, 'andy': 8, 'katie': 6, 'laura': 2, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 8 }, 'john') 
// 'Get Out Now!'
q