// 6kyu - Anagram difference

// Given two words, how many letters do you have to remove from them to make them anagrams?

//     First word : c od e w ar s (4 letters removed)
//     Second word : ha c k er r a nk (6 letters removed)
//     Result : 10

//     A word is an anagram of another word if they have the same letters (usually in a different order).
//     Do not worry about case. All inputs will be lowercase.
//     When you're done with this kata, check out its big brother/sister : https://www.codewars.com/kata/hardcore-anagram-difference

// Fundamentals | Strings | Algorithms

// function anagramDifference(w1, w2) {
//     let diff = 0, countW1 = {}, countW2 = {};
//     [...w1].forEach(v => countW1[v] = ++countW1[v] || 1);
//     [...w2].forEach(v => countW2[v] = ++countW2[v] || 1);
//     for (let key in countW1) {
//         if (countW1.hasOwnProperty(key) && countW2.hasOwnProperty(key))
//             countW2[key] = countW1[key] - countW2[key]
//         else if (countW1.hasOwnProperty(key))
//             countW2[key] = countW1[key]
//     }
//     for (let key in countW2)
//         diff += Math.abs(countW2[key])
//     return diff
// }

function anagramDifference(w1, w2) {
    let diff = 0, countW1 = {}, countW2 = {};
    [...w1].forEach(v => countW1[v] = ++countW1[v] || 1);
    [...w2].forEach(v => countW2[v] = ++countW2[v] || 1);
    Object.keys(countW1).map(v => diff += countW2[v] ? Math.abs(countW1[v] - countW2[v]) : countW1[v])
    Object.keys(countW2).map(v => diff += countW1[v] ? 0 : countW2[v])
    return diff
}


// // https://gist.github.com/gkucmierz/8ee04544fa842411f7553ef66ac2fcf0
// const intersection = (a1, a2) => {
//     const cnt = new Map();
//     a2.map(el => cnt[el] = el in cnt ? cnt[el] + 1 : 1);
//     return a1.filter(el => el in cnt && 0 < cnt[el]--);
// }

// function anagramDifference([...a1], [...a2]) {
//     return a1.length + a2.length - intersection(a1, a2).length * 2;
// }

q = anagramDifference("codewars", "hackerrank") // 10
q
q = anagramDifference("", "") // 0
q
q = anagramDifference("a", "") // 1
q
q = anagramDifference("", "a") // 1
q
q = anagramDifference("ab", "a") // 1
q
q = anagramDifference("ab", "cd") // 4
q
q = anagramDifference("aab", "a") // 2
q
q = anagramDifference("a", "aab") // 2
q