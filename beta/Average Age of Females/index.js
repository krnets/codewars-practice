// Beta - Average Age of Females

var t1 = [{name:'Sarah', gender:'female', age:25}, {name:'Tom', gender:'male', age:18}, {name:'Tim', gender:'male', age:65}, {name:'Kim', gender:'female', age:58}];
var t2 = [{name:'Bob', gender:'male', age:14}, {name:'Tom', gender:'male', age:44}, {name:'Tim', gender:'male', age:52}];
var t3 = [{name:'Sarah', gender:'female', age:25}, {name:'Tom', gender:'male', age:18}, {name:'Tim', gender:'male', age:65}];

// function averageFemale(list) {
//     let femaleList = list.filter(v => v.gender == 'female')
//     let combinedAge = femaleList.map(v => v.age).reduce((a, b) => a + b, 0)
//     return combinedAge / femaleList.length || 0
// }

const averageFemale = list => (l = list.filter(v => v.gender == 'female')).reduce((a, b) => a + b.age, 0) / l.length || 0

q = averageFemale(t1) // 41.5
q
q = averageFemale(t2) // 0
q
q = averageFemale(t3) // 25
q