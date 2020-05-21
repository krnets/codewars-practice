// 7kyu - Battle of the characters (Medium)

/* Groups of characters decided to make a battle. Help them to figure out what group is more powerful. 
Create a function that will accept 2 variables and return the one who's stronger.

    Each character has its own power:

      A = 1, B = 2, ... Y = 25, Z = 26
      a = 0.5, b = 1, ... y = 12.5, z = 13

    Only alphabetical characters can and will participate in a battle.
    Only two groups to a fight.
    Group whose total power (a + B + c + ...) is bigger wins.
    If the powers are equal, it's a tie.

  battle("One", "Two"); // => "Two"`
  battle("ONE", "NEO"); // => "Tie!" */

// function battle(x, y) {
//     let ABC = [...Array(26).keys()].map(v => String.fromCharCode(v + 65))
//     let abc = [...Array(26).keys()].map(v => String.fromCharCode(v + 97))
//     let xs = [...x].map(v => ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2)
//     let ys = [...y].map(v => ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2)
//     let xsum = xs.reduce((a, b) => a + b, 0)
//     let ysum = ys.reduce((a, b) => a + b, 0)
//     return xsum > ysum ? x : xsum < ysum ? y : 'Tie!'
// }

function battle(x, y) {
    let ABC = [...Array(26).keys()].map(v => String.fromCharCode(v + 65))
    let abc = [...Array(26).keys()].map(v => String.fromCharCode(v + 97))
    let xpsum = [...x].reduce((acc, v) => acc + (ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2), 0)
    let ypsum = [...y].reduce((acc, v) => acc + (ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2), 0)
    return xpsum > ypsum ? x : xpsum < ypsum ? y : 'Tie!'
}

// function battle(x, y) {
//     let ABC = [...Array(26).keys()].map(v => String.fromCharCode(v + 'A'.charCodeAt()))
//     let abc = [...Array(26).keys()].map(v => String.fromCharCode(v + 'a'.charCodeAt()))
//     let xpsum = [...x].reduce((acc, v) => acc + (ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2), 0)
//     let ypsum = [...y].reduce((acc, v) => acc + (ABC.includes(v) ? ABC.indexOf(v) + 1 : (abc.indexOf(v) + 1) / 2), 0)
//     return xpsum > ypsum ? x : xpsum < ypsum ? y : 'Tie!'
// }

q = battle("Aa", "Bb") // Bb
q
q = battle("One", "Two") // "Two"
q
q = battle("One", "Neo") // "One"
q
q = battle("One", "neO") // "Tie!"
q
q = battle("Foo", "BAR") // "Tie!"
q
q = battle("Four", "Five") // "Four"
q