// 7kyu - Case swapping

const swap = str => [...str].map(ch => ch == ch.toLowerCase() ? ch.toUpperCase() : ch.toLowerCase()).join ``

q = swap('HelloWorld') // 'hELLOwORLD'
q
q = swap('CodeWars') // 'cODEwARS'
q