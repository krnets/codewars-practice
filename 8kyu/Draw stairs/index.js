// 8kyu - Draw stairs

/* Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in "I\n I\n I", or printed:

I
 I
  I

Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I
*/

// function drawStairs(n) {
//     let res = ''
//     for (let i = 0; i < n; i++)
//         res += ' '.repeat(i) + 'I\n'
//     return res.trim()
// }

function drawStairs(n) {
    let res = 'I'
    for (let i = 1; i < n; i++)
        res += '\n' + ' '.repeat(i) + 'I'
    return res
}

// const drawStairs = n => [...Array(n)].map((_, i) => " ".repeat(i) + "I").join("\n");

q = drawStairs(1) // "I", "The first step has no padding on the left, just an 'I'"
q
q = drawStairs(3) // "I\n I\n  I", "There's something wrong with these 3 steps"
q
q = drawStairs(5) // "I\n I\n  I\n   I\n    I", "5-step stairs no good"
q