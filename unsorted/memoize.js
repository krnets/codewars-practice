// const memoize = fn => {
//     const cache = new Map()
//     const cached = function(val) {
//         return cache.has(val) 
//             ? cache.get(val) 
//             : cache.set(val, fn.call(this, val)) && cache.get(val)
//     }
//     cached.cache = cache;
//     return cached
// }
const memoize = func => {
    // Create cache object to store results
    const results = {}   

    return (...args) => {
        // Create a key for our cache
        const argKey = JSON.stringify(args);
        // Only execute function if no cached value
        if (!results[argKey]) {
            results[argKey] = func(...args)
        }    
        return results[argKey]

    }
}

const inefficientSquare = memoize(num => {
    let total = 0;

    for (let i = 0; i < num; i++) {
        for (let j = 0; j < num; j++) {
            total++
        }
    }
    return total
})

const start = new Date()
q = inefficientSquare(4000)
q
const end = new Date()
console.log(end - start)

const start2 = new Date()
q = inefficientSquare(4000)
q
const end2 = new Date()
console.log(end2 - start2)

const start3 = new Date()
q = inefficientSquare(4000)
q
const end3 = new Date()
console.log(end3 - start3)