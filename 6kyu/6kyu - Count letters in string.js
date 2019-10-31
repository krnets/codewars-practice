// function letterCount(word) {
//   const letters = word.split('');
//   const counter = {};

//   letters.reduce((counter, letter) => {
//     !counter[letter] ? counter[letter] = 1 : counter[letter]++;
//     return counter;
//   }, counter)

//   return counter;
// }

// function letterCount(str) {
//     let myArr = [...str].map((v, i) => [...v, {
//         count: 0
//     }])
//     myArr

//     let mapCounted = new Map(myArr)

//     for (let char of str) {
//         mapCounted.get(char).count++
//     }

//     let mapFlattened = new Map()

//     for (let [key, value] of mapCounted.entries()) {
//         mapFlattened.set(key, value.count)
//     }

//     let result = Array.from(mapFlattened).reduce((result, [key, value]) => (
//         Object.assign(result, {
//             [key]: value
//         })
//     ), {});

//     return result
// }


// const letterCount = s => s.split('')
//                           .reduce((cache,letter) => letter in cache ? 
//                                   (cache[letter]++,cache) : 
//                                   (cache[letter] = 1,cache),
//                                   {})

// const letterCount = require('lodash/countBy');

// const letterCount = (s) => {
//     const arr = s.split('')
//     arr
//     const setArr = Array.from(new Set(arr))
//     let buzz = {}
//     buzz
//     const bar = setArr.forEach(
//       (x) => { 
//         buzz[x] = arr
//           .reduce(
//             (acc, y) => { 
//               return x === y 
//                  ? acc + 1 
//                  : acc
//             }, 
//             0
//           )
//       })
//       buzz
//     return buzz
//   }

// function letterCount(s) {
//     let letterMap = {}
//     s.split('').forEach(r => letterMap[r] = letterMap[r] 
//                     ? letterMap[r] + 1 
//                     : 1)
//     return letterMap
// }

// function letterCount(s) {
//     let result = {};

//     for (let index in s) {
//         const char = s[index];
//         result[char] = result.hasOwnProperty(char) ? result[char] + 1 : 1;
//     }
//     return result;
// }

// function letterCount(s) {
//     const letters = {};
//     for (let i = 0; i < s.length; i++) {
//         if (!letters[s[i]]) {
//             letters[s[i]] = s.split(s[i]).length - 1;
//         }
//     }

//     return letters;
// }

const letterCount = s =>
    s.split('').reduce(
        (acc, c) => ({
            ...acc,
            [c]: (acc[c] || 0) + 1,
        }), {},
    );

// q = letterCount("codewars") // {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1});
// q
q = letterCount("activity") // "a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1});
q
// q = letterCount("arithmetics") // , {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2});
// q
// q = letterCount("traveller") // {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1});
// q
// q = letterCount("daydreamer") //  {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1});
// q