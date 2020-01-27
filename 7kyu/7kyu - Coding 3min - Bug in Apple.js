// 7kyu - Coding 3min: Bug in Apple

/* Find out "B"(Bug) in a lot of "A"(Apple). 
There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array ```apple```
output: Location of "B", ```[x,y]``` */

function sc(apple) {
    for (let i = 0; i < apple.length; i++)
        for (let j = 0; j < apple[i].length; j++)
            if (apple[i][j] == 'B')
                return [i, j]
}

// const sc = (apple) => apple.map((row, i) => [i, row.findIndex(v => v == 'B')]).filter(x => !x.includes(-1))[0]

apple = [
    ["B", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"]
]
q = sc(apple) // [0,0]
q

apple = [
    ["A", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"]
]
q = sc(apple) // [1,1]
q

apple = [
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"]
]
q = sc(apple) // [4,1]
q