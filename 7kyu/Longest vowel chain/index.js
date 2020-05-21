// function longestVowelChain(str) {

//     let a0 = str.length
//     a0


//     // delete any non vowels
//     let a = str.replace(/[^aeiou]/gi, ' ')
//     a


//     // delete blank spots 
//     let c = a.split(' ')
//     c


//     let c1 = c.length
//     c1


//     let c2 = str.split(/[^aeiou]/)
//     c2

//     let c3 = c2.length
//     c3

//     // map over each string to get its length
//     let d  = c.map(v => v = v.length)
//     d


//     let d2 = c2.map(v => v = v.length)
//     d2


//     // use spread operator to apply Math.max to an array
//     // let e = Math.max(...d)
//     // e
//     let e = d.reduce((prev, curr) => Math.max(prev, curr))
//     e


//     let e2 = c2.reduce((prev, curr) => Math.max(prev, curr.length),0)
//     e2

//     return e2
//     // return Math.max(...str
//     //         .replace(/[^aeiou]/gi, ' ')
//     //         .split(' ')
//     //         .map(v => v = v.length))
//     return str.replace(/[^aeiou]/gi, ' ')
//               .split(' ')
//               .map(v => v = v.length)
//               .reduce((prev, curr) => Math.max(prev, curr))
// }

// const longestVowelChain = str => str
//                         .split(/[^aeiou]/)
//                         .reduce((prev, curr) => 
//                             Math.max(prev, curr.length), 0)

// const longestVowelChain = s => {
//     return Math.max(...s
//                     .split(/[^aeiou]+/)
//                     .map(x => x.length))
// }

const longestVowelChain = s => s
                  .split(/[^aeiou]/)
                  .reduce((s,n)=> Math.max(s,n.length),0);


q = longestVowelChain("codewarriors") // 2
q
q = longestVowelChain("suoidea") // 3
q
q = longestVowelChain("ultrarevolutionariees") // 3
q
q = longestVowelChain("strengthlessnesses") // 1
q
q = longestVowelChain("cuboideonavicuare") // 2
q
q = longestVowelChain("conhuooaos") // 5
q
q = longestVowelChain("iiihoovaeaaaoougjyaw") // 8
q
q = longestVowelChain("strspprmsb")
q