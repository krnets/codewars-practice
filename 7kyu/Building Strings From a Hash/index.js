// 7kyu - Building Strings From a Hash

// const solution = pairs => {
//     let keys = Object.keys(pairs)
//     let vals = Object.values(pairs)
//     return Array(keys.length).fill().map((_,i) => keys[i] + ' = ' + vals[i]).toString()
// }

const solution = pairs => Object.keys(pairs).map(key => key + ' = ' + pairs[key]).join(',')
// const solution = pairs => Object.entries(pairs).map(([key, value]) => key + ' = ' + value).join(',')
// const solution = pairs => JSON.stringify(pairs).replace(/:/g,' = ').replace(/\"|\{|\}/g,'') //.replace("{","").replace("}","")

q = solution({
    a: 1,
    b: '2'
}) // should return "a = 1,b = 2"
q