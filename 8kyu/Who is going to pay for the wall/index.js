// 8kyu - Who is going to pay for the wall?

/* Your code will show Full name of the neighbor and the truncated version of the name as an array. 
If the number of the characters in name is equal or less than two, it will return an array containing only the name as is" */

// const whoIsPaying = (name) => name.length > 2 ? [name, name.slice(0,2)] : [name]
const whoIsPaying = (name) => [...new Set([name, name.slice(0,2)])]

q = whoIsPaying("Mexico") // ["Mexico", "Me"])
q
q = whoIsPaying("Melania") // ["Melania", "Me"])
q
q = whoIsPaying("Melissa") // ["Melissa", "Me"])
q
q = whoIsPaying("Me") // ["Me"])
q
q = whoIsPaying("") // [""])
q
q = whoIsPaying("I") // ["I"])
q