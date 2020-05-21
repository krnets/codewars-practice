// 8kyu - Implement a Filter function

/* What we want to implement is a filter function, like Array.filter(), 
also similar to the _.filter() in underscore.js and lodash.js.

The usage is quite simple, like:

[1,2,3,4].filter((num)=>{ return num > 3})

should output [4] */

Array.prototype.filter = function (pred) {
    let res = []
    for (let i = 0; i < this.length; i++)
        if (pred(this[i]))
            res.push(this[i])
    return res
}

q = [1, 2, 3, 4].filter((num) => { return num > 3 }) // [4]
q