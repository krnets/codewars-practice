// function scoreboard(str) {
// let dict = {
//     nil: 0,
//     one: 1,
//     two: 2,
//     three: 3,
//     four: 4,
//     five: 5,
//     six: 6,
//     seven: 7,
//     eight: 8,
//     nine: 9
// }
// return str.split(' ').slice(-2).map(val => dict[val])
// }

// function scoreboard(str) {
// let dict = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
// return str.split(' ').slice(-2).map(val => dict.indexOf(val))
// }

scoreboard=(s)=>s.split(' ').slice(-2).map(w=>['nil','one','two','three','four','five','six','seven','eight','nine'].indexOf(w))


// scoreboard = a => a.split ` `.slice(-2).map(index => dict = {
//     nil: 0,
//     one: 1,
//     two: 2,
//     three: 3,
//     four: 4,
//     five: 5,
//     six: 6,
//     seven: 7,
//     eight: 8,
//     nine: 9
// } [index])

q = scoreboard("The score is four nil") // [4,0], "Should return: [4,0]"
q
q = scoreboard("new score: two three") // [2,3], "Should return: [2,3]"
q
q = scoreboard("two two") // [2,2], "Should return: [2,2]"
q
q = scoreboard("Arsenal just conceded another goal, two nil") // [2,0], "Should return: [2,0]"
q