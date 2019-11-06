// 7kyu - Build a square

// const generateShape = int => [...Array(int)].map(_ => ['+'.repeat(int)]).join('\n')
// const generateShape = int => Array(int).fill().map(_ => ['+'.repeat(int)]).join('\n')
// const generateShape = int => Array(int).fill().map(_ => '+'.repeat(int)).join('\n')
const generateShape = int => ('+'.repeat(int) + '\n').repeat(int).trim()

q = generateShape(8)
// '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'
q