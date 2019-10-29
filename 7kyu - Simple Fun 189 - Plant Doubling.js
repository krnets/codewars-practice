// 7kyu - Simple Fun 189 - Plant Doubling

// const plantDoubling = n => n.toString(2).split('1').length - 1
// const plantDoubling = n => n.toString(2).match(/1/g).length
// const plantDoubling = n => n.toString(2).replace(/0/g,'').length ;
// const plantDoubling = n => [...n.toString(2)].reduce((acc, cur) => +cur + acc, 0)
const plantDoubling = n => n && 1 + plantDoubling(n & n - 1)
// const plantDoubling = n => n && plantDoubling(n >> 1) + (n & 1)

// function plantDoubling(n) {
//     return (n === 1) ? 1 :
//         (n % 2 === 1 ? 1 : 0) + plantDoubling(Math.trunc(n / 2));
// }


q = plantDoubling(5) // 2
q
q = plantDoubling(8) // 1
q
q = plantDoubling(536870911) // 29
q
q = plantDoubling(1) // 1
q