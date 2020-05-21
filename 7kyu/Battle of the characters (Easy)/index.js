// 7kyu - Battle of the characters (Easy)

/* Groups of characters decided to make a battle. Help them to figure out which group is more powerful. 
Create a function that will accept 2 variables and return the one who's stronger.

    Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
    Only capital chatacters can and will participate a battle.
    Only two groups to a fight.
    Group whose total power (A + B + C + ...) is bigger wins.
    If the powers are equal, it's a tie. */

function battle(x, y) {
    let xsum = [...x].reduce((acc, v) => acc + v.charCodeAt() - 64, 0)
    let ysum = [...y].reduce((acc, v) => acc + v.charCodeAt() - 64, 0)
    return xsum > ysum ? x : xsum < ysum ? y : 'Tie!'
}

q = battle("AAA", "Z") // "Z", "Unfair fight!"
q
q = battle("ONE", "TWO") // "TWO", "Unfair fight!"
q
q = battle("ONE", "NEO") //  "Tie!", "Unfair fight!"
q
q = battle("FOUR", "FIVE") // "FOUR", "Unfair fight!"
q