// 4kyu - Permutations

// function permutations(string) {
//     let array = []
//     for (let i = 0; i < Math.pow(string.length, 4); i++)
//         array.push([...string].sort(() => 0.5 - Math.random()))
//     return [...new Set(array.map((v => v.join ``)))]
// }

// function permutations(str) {
//     return str.length <= 1 ? [str] :
//         Array.from(new Set(
//             str.split('')
//             .map((char, i) => permutations(str.substr(0, i) + str.substr(i + 1)).map(p => char + p))
//             .reduce((r, x) => r.concat(x), [])
//         )) 
// }

// function permutations(string) {
//     const result = [];
//     heapPermutation(string.split(''), string.length, result);
//     return [...new Set(result)];
// }

// const swap = (arr, i, j) => {
//     arr
//     let tmp = arr[i];
//     arr[i] = arr[j];
//     arr[j] = tmp;
// }

// function heapPermutation(arr, size, result) {
//     if (size == 1) {
//         arr
//         result.push(arr.join(''));
//         return;
//     }

//     for (let i = 0; i < size; i++) {
//         heapPermutation(arr, size - 1, result);

//         if (size % 2 === 1) {
//             swap(arr, 0, size - 1);
//         } else {
//             swap(arr, i, size - 1);
//         }
//     }
// }

// recursive solution:
function permutations(string) {
    let result = []

    if (string.length == 0) {
        result.push(string)
        return result
    }

    for (let i = 0; i < string.length; i++) {
        let first = string[i]
        let rest = permutations(string.slice(0, i) + string.slice(i + 1))
        for (let j = 0; j < rest.length; j++) {
            let newStr = first + rest[j]
            if (!result.includes(newStr))
                result.push(newStr)
        }
    }
    return result
}

q = permutations('a') // ['a']
q
q = permutations('ab') // .sort(), ['ab', 'ba'].sort()
q
q = permutations('aabb') // .sort(), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'].sort()
q