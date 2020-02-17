// 5kyu - Double Cola

/* Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; 
there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! 
The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, 
drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

Write a program that will return the name of the person who will drink the n-th cola.

The input data consist of an array which contains at least 1 name, and single integer n which may go as high 
as the biggest number your language of choice supports (if there's such limit, of course).

Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.

whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard" */

// function whoIsNext(names, r) {
//     while (r > names.length)
//         r = Math.floor((r - names.length + 1) / 2)
//     return names[r - 1]
// }

const whoIsNext = (names, r) => names[r - 1] || whoIsNext(names, Math.floor((r - names.length) / 2))

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
q = whoIsNext(names, 1) // "Sheldon"
q
q = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) // "Sheldon"
q
q = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) // "Penny"
q
q = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) // "Leonard"
q