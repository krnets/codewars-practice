// 7kyu - Drawing a Cross!

/* The aim of this kata is to write function drawACross which returns a cross shape 
with 'x' characters on a square grid of size and height of our sole input n. 
All non-'x' characters in the grid should be filled with a space character (" ").

For example for drawACross(7), the function should draw the following grid:

x     x
 x   x 
  x x  
   x   
  x x  
 x   x 
x     x

The arms of the cross must only intersect through one central 'x' character, 
and start in the corner of the grid, so for even values of n, return "Centered cross not possible!"

If n<3, function should return "Not possible to draw cross for grids less than 3x3!" */

// function drawACross(n) {
//     if (n < 3) return 'Not possible to draw cross for grids less than 3x3!'
//     if (n % 2 == 0) return 'Centered cross not possible!'
//     let str = ''
//     for (let i = 0; i < n / 2 - 1; i++) {
//         let a = i * 2
//         str += ' '.repeat(i) + 'x' + ' '.repeat(Math.abs(n - a - 2)) + 'x' + ' '.repeat(i) + '\n'
//     }
//     return (str + ' '.repeat((n) / 2) + 'x' + ' '.repeat((n) / 2) + '\n' + str.split `\n`.reverse().join `\n`).replace(/\n\n/, '\n')
// }

// function drawACross(n) {
//     if (n < 3) return 'Not possible to draw cross for grids less than 3x3!';
//     if (n % 2 == 0) return 'Centered cross not possible!';
//     return ''.padEnd(n * (n + 1) - 1).replace(/./g, (c, i) => (i + 1) % (n + 1) ? i % (n + 2) && (i + 1) % n ? c : 'x' : '\n');
// }

function drawACross(n) {
    if (n < 3) return 'Not possible to draw cross for grids less than 3x3!'
    if (n % 2 == 0) return 'Centered cross not possible!'
    let grid = Array(n).fill().map(_ => Array(n).fill(' '))
    for (let i = 0; i < n; i++) {
        grid[i][i] = 'x'
        grid[n-i-1][i] = 'x'
    }
    return grid.map(v => v.join('')).join('\n')
}


q = drawACross(7)
// 'x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x'
// , 'Should draw a centered cross in a grid of height and width n!')
q
q = drawACross(15)
// 'x             x\n x           x \n  x         x  \n   x       x   \n    x     x    \n     x   x     \n      x x      \n       x       \n      x x      \n     x   x     \n    x     x    \n   x       x   \n  x         x  \n x           x \nx             x'
// , 'Should draw a centered cross in a grid of height and width n!')
q
q = drawACross(25)
// 'x                       x\n x                     x \n  x                   x  \n   x                 x   \n    x               x    \n     x             x     \n      x           x      \n       x         x       \n        x       x        \n         x     x         \n          x   x          \n           x x           \n            x            \n           x x           \n          x   x          \n         x     x         \n        x       x        \n       x         x       \n      x           x      \n     x             x     \n    x               x    \n   x                 x   \n  x                   x  \n x                     x \nx                       x', 'Should draw a centered cross in a grid of height and width n!')
q
q = drawACross(6)
// 'Centered cross not possible!'
// , 'If a centred cross is not possible, display the correct error message!')
q
q = drawACross(10)
// 'Centered cross not possible!'
// , 'If a centred cross is not possible, display the correct error message!')
q
q = drawACross(2)
// 'Not possible to draw cross for grids less than 3x3!'
// , 'Numbers less than three should return the correct error message')
q