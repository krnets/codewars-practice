// 7kyu - Find the capitals

/* Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string. */
 
var capitals = function (word) {
    for (var res = [], i = 0; i < word.length; i++)
        if (word[i] == word[i].toUpperCase())
            res.push(i)
    return res
}

q = capitals('CodEWaRs') // [0,3,4,6] 
q