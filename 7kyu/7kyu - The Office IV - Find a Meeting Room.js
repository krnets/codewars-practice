// 7kyu - The Office IV - Find a Meeting Room

// function meeting(x) {
//     let i = x.findIndex(v => v == 'O');
//     return (i == -1) ? 'None available!' : i
// }

// const meeting = x => (i = x.findIndex(v => v == 'O')) > -1 ? i : 'None available!'
// const meeting = x => x.indexOf('O') == -1 ? 'None available!' : x.indexOf('O')
const meeting = x => (idx = x.indexOf('O')) > -1 ? idx : 'None available!'
// const meeting = x => ~(idx = x.indexOf('O')) ? idx : 'None available!'


q = meeting(['X', 'O', 'X']) // 1
q
q = meeting(['O', 'X', 'X', 'X', 'X']) // 0
q
q = meeting(['X', 'X', 'X', 'X', 'X']) // 'None available!'
q