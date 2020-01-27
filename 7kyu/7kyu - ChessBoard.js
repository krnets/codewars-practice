// 7kyu - ChessBoard

/* Write a function that creates a string that represents an 8×8 grid, using newline characters to separate lines. 
At each position of the grid there is either a space or a “#” character (black='#', black always starts top/left). 
The characters should form a chess board.

When you have a program that generates this pattern, define a variable size = 8 and change the program so that 
it works for any size, outputting a grid of the given width and height. */

function board(size) {
    return Array(size).fill()
        .map((_, i) => Array(size).fill()
            .map((_, j) => '# '[(i + j) % 2]).join('')).join('\n')
}


// const board = (size) => Array(size).fill().map((_, i) => Array(size).fill().map((_, j) => '# ' [(i + j) % 2]).join('')).join('\n')


q = board(3) // "# # #\n # # \n# # #\n"
q
q = board(5) // "# # #\n # # \n# # #\n # # \n# # #\n"
q
q = board(11) // "# # # # # #\n # # # # # \n# # # # # #\n # # # # # \n# # # # # #\n # # # # # \n# # # # # #\n # # # # # \n# # # # # #\n # # # # # \n# # # # # #\n"
q