// 7kyu - Search JSON for any key value pair

/* Write a function that can search some JSON records and return matching character details.
Search for objects in the collection by any of the objects keys and return an array of all the matches.
The basic structure of the JSON object is shown below:

let characters = {"characters": [
    {"name":"Bill Cipher", "age":"Unknown", "speciality":"warp reality"},
    // ......
]};

The JSON object is preloaded and can be accessed using the variable characters.

Your function will also need to accommodate the following:

    Passed value does not match any keys: in this instance return an empty array.
    Passed key does not exist: in this instance return an empty array.
    Passed val should not be case sensitive. */

let characters =  [{"name":"Dipper Pines", "age":"12", "speciality":"adventurer"}, 
                   {"name":"Waddles", "age":"Unknown", "speciality":"pig stuff"},
                   {"name":"Wendy Corduroy", "age":"15", "speciality":"sociable and nonchalant"}]

const getCharacters = (obj, key, val) => obj.filter(v => RegExp('^' + val + '$', 'i').test(v[key]))
// const getCharacters = (obj, key, val) => obj.filter(v => RegExp(`^${val}$`, 'i').test(v[key]))
// const getCharacters = (obj, key, val) => obj.characters.filter(v => RegExp(`^${val}$`, 'i').test(v[key]))

// const getCharacters = (obj, key, val) => obj.filter(v => v[key] && v[key].toLowerCase() == val.toLowerCase())
// const getCharacters = (obj, key, val) => obj.characters.filter(v => v[key] && v[key].toLowerCase() == val.toLowerCase())

q = getCharacters(characters, 'name', 'Dipper Pines')
//   [{"name":"Dipper Pines", "age":"12", "speciality":"adventurer"}]) //  true
q
q = getCharacters(characters, 'name', 'waddles')
//   [{"name":"Waddles", "age":"Unknown", "speciality":"pig stuff"}]) //  true
q
q = getCharacters(characters, 'name', 'Wendy')
// [{"name":"Wendy Corduroy", "age":"15", "speciality":"sociable and nonchalant"}])  // false
q