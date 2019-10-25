// const histogram = results => results
//     .reduce((accum, current, index) =>
//         (index + 1) + '|' + (current ? '#'.repeat(current) + ' ' + current : '') + '\n' + accum, '')

// const histogram = results => results
//         .reduceRight((accum, current, index) => 
//             (index + 1) + ' ' +  accum, '') + '\n' 

// Expected: '    10\n    #\n    #\n7   #\n#   #\n#   #     5\n#   #     #\n# 3 #     #\n# # #     #\n# # # 1   #\n# # # #   #\n-----------\n1 2 3 4 5 6\n'
// Actual:   '    10 \n    # \n    # \n7   # \n#   # \n#   #     5 \n#   #     # \n# 3 #     # \n# # #     # \n# # # 1   # \n# # # #   # \n-----------\n1 2 3 4 5 6\n'

// function histogram(results) {
//     let len = results.length
//     let highest = Math.max(...results)
//     let index = [...Array(len + 1).keys()].slice(1).join(' ')
//     let output = ''

//     for (let h = highest; h >= 0; h--) {
//         output += Array(len).fill(0)
//             .map((_, i) =>
//                 (results[i] == h && results[i] != 0) ?
//                 results[i] :
//                 (results[i] < h || results[i] == 0) ?
//                 ' ' : '#')
//             .join(' ')
//             .replace(/\s*$/, '') + '\n'
//     }
//     return highest ?
//         output += '-'.repeat(len * 2 - 1) + '\n' + index + '\n' :
//         '-'.repeat(len * 2 - 1) + '\n' + index + '\n'
// }

const histogram = (results, height = Math.max(...results)) => [
    ...Array.from({ length: height ? height + 1 : 0 }, (_, i) => i)
            .map(n => results.map(i => i == height - n ?
                (i ? i : ' ') :
                (i > height - n ? '#' : ' '))
            .join(' ')
            .trimRight()),
    '-----------',
    '1 2 3 4 5 6',
    ''
].join('\n')

// var histogram = function(results) {
//     let highest = Math.max(...results);
//     let str = "";
//     for(let i = highest; i >= 0; i--){
//         str += Array(6).fill(0).map((a, idx) => 
// (results[idx] === i && results[idx] !== 0) ? 
// results[idx] : (results[idx] < i || results[idx] === 0) ? 
// " " : "#").join(" ").replace(/\s*$/,"")+"\n";
//     }
//     return (highest) ?  str += "-----------\n1 2 3 4 5 6\n" : "-----------\n1 2 3 4 5 6\n";
// }


q = histogram([7, 3, 10, 1, 0, 5])
q

// =====================================

var expected =
    "    10\n" +
    "    #\n" +
    "    #\n" +
    "7   #\n" +
    "#   #\n" +
    "#   #     5\n" +
    "#   #     #\n" +
    "# 3 #     #\n" +
    "# # #     #\n" +
    "# # # 1   #\n" +
    "# # # #   #\n" +
    "-----------\n" +
    "1 2 3 4 5 6\n";