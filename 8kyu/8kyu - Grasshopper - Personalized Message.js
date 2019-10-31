// 8kyu - Grasshopper - Personalized Message

const greet = (name, owner) => (name == owner) ? 'Hello boss' : 'Hello guest'

// function greet(name, owner) {
//     if (name == owner)
//         return 'Hello boss'
//     else
//         return 'Hello guest'
// }

q = greet('Daniel', 'Daniel') // 'Hello boss'
q
q = greet('Greg', 'Daniel') // 'Hello guest'
q