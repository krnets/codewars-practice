// 7kyu - Cat and Mouse - Easy Version

/* You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'.

You need to find out if the cat can catch the mouse from it's current position. The cat can jump over three characters. So:

C.....m returns 'Escaped!' <-- more than three characters between

C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump. */

const catMouse = (x) => /\.{4}/.test(x) ? 'Escaped!' : 'Caught!'

q = catMouse('C....m'), "Escaped!"
q
q = catMouse('C..m'), "Caught!"
q
q = catMouse('C.....m'), "Escaped!"
q