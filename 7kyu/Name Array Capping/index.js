// 7kyu - Name Array Capping

// Create a method that accepts an array of names, and returns an array of each name with its first letter capitalized.

const capMe = names => names.map(v => v[0].toUpperCase() + v.slice(1).toLowerCase())

q = capMe(['jo', 'nelson', 'jurie']) // returns ['Jo', 'Nelson', 'Jurie']
q
q = capMe(['KARLY', 'DANIEL', 'KELSEY']) // returns ['Karly', 'Daniel', 'Kelsey']
q