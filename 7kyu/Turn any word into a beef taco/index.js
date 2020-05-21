// 7kyu - Turn any word into a beef taco

/* Turn every word we find into the taco bell recipe with each ingredient.
We want to input a word as a string, and return a list representing that word as a taco.

Key
all vowels (except 'y') = beef
t = tomato
l = lettuce
c = cheese
g = guacamole
s = salsa

We do not care about case here. 'S' is therefore equivalent to 's' in our taco.
Ignore all other letters; we don't want our taco uneccesarily clustered or else it will be too difficult to eat.
Note that no matter what ingredients are passed, our taco will always have a shell. */

// function tacofy(word) {
//     let ingredients = { 'a': 'beef', 'e': 'beef', 'i': 'beef', 'o': 'beef', 'u': 'beef', 't': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa' }
//     let taco = [...word].map(v => ingredients[v.toLowerCase()]).filter(v => v)
//     taco.unshift('shell')
//     taco.push('shell')
//     return taco
// }

const tacofy = word => ['shell', ...word.toLowerCase().replace(/[^aeioutlcgs]/g, '').split ``.map(c => ({
    t: 'tomato', l: 'lettuce', c: 'cheese', g: 'guacamole', s: 'salsa' })[c] || 'beef').concat(['shell'])]

// function tacofy(word) {
//     let map = {t:'tomato',l:'lettuce',c: 'cheese',g: 'guacamole',s:'salsa',a:'beef',e:'beef',i:'beef',o:'beef',u:'beef'};
//     return ['shell', ...[...word].map(x => map[x.toLowerCase()]).filter(v=>v), 'shell'];
// }

q = tacofy("") // ['shell', 'shell']
q
q = tacofy("a") // ['shell', 'beef', 'shell']
q
q = tacofy("ggg") // ['shell', 'guacamole', 'guacamole', 'guacamole', 'shell']
q
q = tacofy("ogl") // ['shell', 'beef', 'guacamole', 'lettuce', 'shell']
q
q = tacofy("ydjkpwqrzto") // ['shell', 'tomato', 'beef', 'shell']
q