// 6kyu - What will be the odd one out?

/* Write a function that will take in a string and return all the unpaired characters 
(show up an odd number of times in the string) in the order they were encountered as an array. 
In case of multiple options to choose from, take the last occurence as the unpaired character.

    A wide range of characters is used, and some of them may not render properly in your browser.
    Your solution should be linear in terms of string length to pass the last test.

oddOneOut('Hello World')   ===  ["H", "e", " ", "W", "r", "l", "d"]
oddOneOut('Codewars')      ===  ["C", "o", "d", "e", "w", "a", "r", "s"]
oddOneOut('woowee')        ===  []
oddOneOut('wwoooowweeee')  ===  []
oddOneOut('racecar')       ===  ["e"]
oddOneOut('Mamma')         ===  ["M"]
oddOneOut('Mama')          ===  ["M", "m"] */


// function oddOneOut(str) {
//     let res = [];
//     let chars = {};
//     [...str].forEach(v => chars[v] = ++chars[v] || 1);
//     chars = Object.entries(chars).filter(v => v[1] != 1).map(v => v[1] % 2 == 0 ? v : [v[0], v[1] - 1]).reduce((o, v) => (o[v[0]] = v[1], o), {});
//     [...str].forEach(c => chars[c] > 0 ? --chars[c] : res.push(c));
//     return res;
// }

// function oddOneOut(str) {
//     let chars = new Set();
//     for (let c of str) {
//       if (chars.has(c))
//         chars.delete(c);
//       else
//         chars.add(c);
//     }
//     return Array.from(chars);
//   }

function oddOneOut(str) {
    let chars = new Set()
    for (let c of str)
        chars.has(c) ? chars.delete(c) : chars.add(c)
    return [...chars]
}

q = oddOneOut('Hello World') // ["H", "e", " ", "W", "r", "l", "d"]
q
q = oddOneOut('Codewars') // ["C", "o", "d", "e", "w", "a", "r", "s"]
q
q = oddOneOut('woowee') // []
q
q = oddOneOut('wwoooowweeee') // []
q
q = oddOneOut('racecar') // ["e"]
q
q = oddOneOut('Mamma') // ["M"]
q
q = oddOneOut('Mama') // ["M", "m"]
q
q = oddOneOut('¼ x 4 = 1') // ["¼", "x", "4", "=", "1"]
q
q = oddOneOut('¼ x 4 = 1 and ½ x 4 = 2') // ["¼", "1", "a", "n", "d", "½", "2"]
q