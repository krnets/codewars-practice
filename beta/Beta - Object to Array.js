// Beta - Object to Array

/* Your task is to create two functions :

    One function to turn an object into an array
    One function to turn an array into an object

arrayToObject([1, 1, 2, 2, 3, 3]) => {1:2, 2:2, 3:2}
objectToArray({2:5, 99:1}) => [2, 2, 2, 2, 2, 99]

arrayToObject receives an array. 
It must return an object, where the key is the values found in the array and the value is the number of times 
it was found({value:times_found})

objectToArray receives an object. 
It must return an array. Each value is repeated as many times as each key of the object. 
When the key of the object is a number, the values of the array must be numbers. 
(Ex : {1:5} must return [1,1,1,1,1] not ['1','1','1','1','1'] )

You must not change the value given in input. */


const arrayToObject = arr => arr.reduce((count, v) => (count[v] = ++count[v] || 1, count), {})

const objectToArray = obj => Object.keys(obj).reduce((arr, v) => arr.concat(Array.from({length: obj[v]}, () => Number(v) || v)), [])

// const objectToArray = obj => [].concat(...Object.keys(obj).map(v => Array.from({length: obj[v]}, () => Number(v) || v)))



q  = arrayToObject([1, 1, 2, 2, 3, 3]) // {1:2, 2:2, 3:2}
q
q = arrayToObject([]) // {}
q
q = arrayToObject(["a","a","e","e","i","o","o","o","o"]) // {a:2,e:2,i:1,o:4}
q
q = objectToArray({a:4,o:1}) // ['a','o','a','a','a']
q
q = objectToArray( {none:0, nada:0, rien: 0}) // []
q