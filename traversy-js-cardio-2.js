// CHALLENGE 1: LONGEST WORD
// Return the longest word of a string
// ex. longestWord('Hi there, my name is Brad') === 'there,'

function longestWord(sen) {
    // SOLUTION 1 - Return a single longest word
    // SOLUTION 2 - Return an array and include multiple words if they have the same length
    // SOLUTION 3 - Only return an array if multiple words, otherwise return a string
    const wordArr = sen.toLowerCase().match(/[a-z0-0]+/g)
    wordArr

    const sorted = wordArr.sort((a, b) => b.length - a.length)
    sorted

    const longestWordArr = sorted.filter(word => word.length === sorted[0].length)
    longestWordArr

    if (longestWordArr.length === 1) {
        return longestWordArr[0]
    } else {
        return longestWordArr
    }
}

q = longestWord('Hello there, my name is Brad')
q

// CHALLENGE 2: ARRAY CHUNKING
// Split an array into chunked arrays of a specific length
// ex. chunkArray([1, 2, 3, 4, 5, 6, 7], 3) === [[1, 2, 3],[4, 5, 6],[7]]
// ex. chunkArray([1, 2, 3, 4, 5, 6, 7], 2) === [[1, 2],[3, 4],[5, 6],[7]]

function chunkArray(arr, chunk) {
    // SOLUTION 1
    const sliceArray = []
    let i = 0

    while (i < arr.length) {
        sliceArray.push(arr.slice(i, i += chunk))
    }
   
    return sliceArray
    // SOLUTTION 2
//     const chunkedArray = []
//     arr.forEach(val => {
//         const last = chunkedArray[chunkedArray.length - 1]
//         if (!last || last.length === chunk) {
//             chunkedArray.push([val])
//         } else {
//             last.push(val)
//             last
//         }
//     });
//    return chunkedArray
}



// q = (chunkArray([1, 2, 3, 4, 5, 6, 7], 2) === [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7 ] ])
p = chunkArray([1, 2, 3, 4, 5, 6, 7], 3)
p

q = chunkArray([1, 2, 3, 4, 5, 6, 7], 2)
q

// CHALLENGE 3: FLATTEN ARRAY
// Take an array of arrays and flatten to a single array
// ex. [[1, 2], [3, 4], [5, 6], [7]] = [1, 2, 3, 4, 5, 6, 7]

function flattenArray(arrays) {
    arrays    
    return arrays.flat(Infinity)
    // return arrays.reduce((a,b) => a.concat(b))
    // return [].concat.apply([],arrays)
    // return [].concat(...arrays)
}

p = flattenArray([1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]])
// q
// p = flattenArray(q)
p

// CHALLENGE 4: ANAGRAM
// Return true if anagram and false if not
// ex. 'elbow' === 'below'
// ex. 'Dormitory' === 'dirty room##'

function isAnagram(str1, str2) {
    let sortedStr1 = str1.toLowerCase().split('').sort().join('').trim()
    sortedStr1
    let sortedStr2 = str2.toLowerCase().split('').sort().join('').trim()
    sortedStr2
    return sortedStr1 === sortedStr2
}

// q = isAnagram('listen', 'silent')
// q = isAnagram('below', 'elbow')
// q = isAnagram('Dormitory', 'Dirty room')
// q = isAnagram('Astronomer', 'Moon starer')
// q = isAnagram('Funeral', 'Real fun')
q = isAnagram('School master', 'The classroom')
q

// CHALLENGE 5: LETTER CHANGES
// Change every letter of the string to the one that follows it and capitalize the vowels
// Z should turn to A
// ex. 'hello there' === 'Ifmmp UIfsf'

function letterChanges(str) {
    let newStr = str.replace(/[a-zA-Z]/gi, function(char) {
        if (char === 'z') {
            return 'a'
        } else if ( char === 'Z') {
            return 'A'
        } else  {
            return String.fromCharCode(char.charCodeAt() + 1)
        }
    })
    
    newStr = newStr.replace(/a|i|e|i|o|u/gi, vowel => vowel.toUpperCase())
    return newStr
}

q = letterChanges('Hello there')
q
// Call Function