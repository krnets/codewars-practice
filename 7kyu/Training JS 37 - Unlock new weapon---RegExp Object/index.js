// 7kyu - Training JS #37: Unlock new weapon---RegExp Object

/*  Create function countAnimals which accept two parameters: 
animals, a string contains some animals; 
count, an array list of which animals we should count. 
The result should be a number array. */

function countAnimals(animals, count) {
    return count.map(v => (animals.match(new RegExp(v, 'g')) || []).length)
}

q = countAnimals("dog,cat", ["dog", "cat"]) // [1,1]
q
q = countAnimals("dog,cat", ["dog", "cat", "pig"]) // [1,1,0]
q
q = countAnimals("dog,dog,cat", ["dog", "cat"]) // [2,1]
q
q = countAnimals("dog,dog,cat", ["pig", "cow"]) // [0,0]
q