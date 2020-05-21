// 7kyu - Multiplication - Generators #2

/* Generators can be used to wonderful things. You can use them for numerous things, 
but here is one specific example. You are studying for a test so you must practice your multiplication, 
but you don't have a multiplication table showing the different examples. 
You have decided to create a generator that prints out a limitless list of time tables.

Your generator must take one parameter `a` then everytime the generator is called you must 
return a string in the format of: `'a x b = c'` where c is the answer. Also, the value of `b`, 
which starts at 1, must increment by 1 each time!  */

// function* generator(a, b = 1) {
//     while (true) yield `${a} x ${b} = ${a * b++}`
// }

function* generator(a) {
    for (let i = 1;; i++) yield `${a} x ${i} = ${a * i}`
}

var gen = generator(1)
q = gen.next().value // 1 x 1 = 1
q
q = gen.next().value // 1 x 2 = 2
q
q = gen.next().value // 1 x 3 = 3
q
q = gen.next().value // 1 x 4 = 4
q
q = gen.next().value // 1 x 5 = 5
q

var gen = generator(54)
q = gen.next().value // 54 x 1 = 54
q
q = gen.next().value // 54 x 2 = 108
q
q = gen.next().value // 54 x 3 = 162
q
q = gen.next().value // 54 x 4 = 216
q
q = gen.next().value // 54 x 5 = 270
q