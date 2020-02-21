// 4kyu - Strip Comments

/* Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"   */


// function solution(str, arr) {
//     str = str.split("\n")
//     for(let i = 0; i < str.length; i++){
//         let shorter;
//         for(let j = 0; j < arr.length; j++) {
//             let idx = str[i].indexOf(arr[j]);
//             if(idx > -1)
//                 shorter = (idx<shorter||!shorter) ? idx : shorter;
//         }
//         if(shorter)
//             str[i] = str[i].substr(0, shorter).trim();
//     }
//     return str.join("\n");
// }

// function solution(input, markers) {
//     let output = input.split('\n')
//     let marker = 0

//     for (let i = 0; i < output.length; i++) {
//         for (let j = 0; j < markers.length; j++) {
//             let index = output[i].indexOf(markers[j])
//             if (index > -1)
//                 marker = (index < marker || !marker) ? index : marker
//         }
//         if (marker)
//             output[i] = output[i].substr(0, marker).trim()
//     }
//     return output.join('\n')
// }

// function solution(input, markers) {
//     return input.split('\n').map(
//         line => markers.reduce(
//             (line, marker) => line.split(marker)[0].trim(), line)
//     ).join('\n')
// }
const solution = (input, markers) => input.replace(new RegExp(`\\s*[${markers.join('|')}].+`, 'g'), '')
// const solution = (input, markers) => input.replace(new RegExp("\\s?[" + markers.join("") + "].*(\\n)?", "gi"), "$1")
// const solution = (input, markers) => input.replace(new RegExp(" [" + markers.join(',') + "].+", "gi"), '');

q = solution("apples, plums % and bananas\npears\noranges !applesauce", ["%", "!"])
q
// "apples, plums\npears\noranges"

function checkComments(input, markers, expected) {
    var actual;
    actual = solution(input, markers);
    return Test.expect(actual === expected, "Returned '" + actual + "' but expected '" + expected + "'");
};

q = checkComments("apples, plums % and bananas\npears\noranges !applesauce", ["%", "!"], "apples, plums\npears\noranges")
q
q = checkComments("Q @b\nu\ne -e f g", ["@", "-"], "Q\nu\ne")
q