// const helloWorld = str => {
//     let a = [...str].map((v,i) => str.codePointAt(i))
//     a
//     // return a
//     let b = a.map((v,i) => String.fromCharCode(v)).join``
//     b
//     return b
// }

// [72, 101, 108, 108, 111, 44, 32]
// [87, 111, 114, 108, 100, 33]

// const helloWorld = () => String.fromCharCode(72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33)

const helloWorld = () => /Hello, World!/.source


q = helloWorld() // "Hello, World!"
q
// q = helloWorld("Hello, World!")
// q
// q = helloWorld("Hello, ")
// q
// q = helloWorld("World!")
// q