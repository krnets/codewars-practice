// 7kyu - Difference between two collections

/* Find the difference between two collections. 
The difference means that either the character is present in one collection or it is present in other, 
but not in both. Return a sorted set with difference.

The collections can contain any character and can contain duplicates.

For instance:

A = [a,a,t,e,f,i,j]
B = [t,g,g,i,k,f]
difference = [a,e,g,j,k]   */

const diff = (a, b) => [...new Set(a.concat(b))].filter(v => a.includes(v) ^ b.includes(v)).sort()

q = diff(["a", "b"], ["a", "b"]) // []
q

a = ["a", "b"];
b = [];
q = diff(a, b) // a
q

a = [];
b = ["a", "b"];
q = diff(a, b) // b
q
q = diff([], []) // []
q

a = ["a", "b", "z"];
b = ["a", "b"];
q = diff(a, b) // ["z"]
q

a = ["a", "b", "z", "d", "e", "d"];
b = ["a", "b", "j", "j"];
q = diff(a, b) // ["d","e","j","z"]
q