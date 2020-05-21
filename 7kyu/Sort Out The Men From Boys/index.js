function menFromBoys(arr) {
    let evenNums = []
    let oddNums = []

    for (let i of arr) {
        if (i % 2 == 0) {
            evenNums.push(i)
        } else { 
            oddNums.push(i)    
        }
    }

    let mergedAndSorted = [evenNums.sort((a,b) => a - b), oddNums.sort((a,b) => b - a)]
    let flattened = mergedAndSorted.reduce((accum, value) => accum.concat(value))

    return [...new Set(flattened)]    
}

// const menFromBoys = (array) => Array.of(...new Set(array)).sort((a, b) => a & 1 && b & 1 ? b - a : a & 1 ? 1 : b & 1 ? -1 : a - b);

// function menFromBoys (arr) {
//     return [...new Set
//             ([...arr.filter(v => v % 2 == 0)
//                     .sort((a, b) => a - b), 
//               ...arr.filter(v => v % 2 != 0)
//                     .sort((a, b) => b - a)])];
// }

q = menFromBoys([7, 3, 14, 17]) //, [14,17,7,3]);
q
q = menFromBoys([2, 43, 95, 90, 37]) //, [2,90,95,43,37]);
q
q = menFromBoys([20, 33, 50, 34, 43, 46]) //, [20,34,46,50,43,33]);
q
q = menFromBoys([82, 91, 72, 76, 76, 100, 85]) //, [72,76,82,100,91,85]);
q
q = menFromBoys([2, 15, 17, 15, 2, 10, 10, 17, 1, 1]) //, [2,10,17,15,1]);
q
q = menFromBoys([-32, -39, -35, -41]) //, [-32,-35,-39,-41]);
q
q = menFromBoys([-64, -71, -63, -66, -65]) //, [-66,-64,-63,-65,-71]);
q
q = menFromBoys([-94, -99, -100, -99, -96, -99]) //, [-100,-96,-94,-99]);
q
q = menFromBoys([-53, -26, -53, -27, -49, -51, -14]) //, [-26,-14,-27,-49,-51,-53]);
q
q = menFromBoys([-17, -45, -15, -33, -85, -56, -86, -30]) //, [-86,-56,-30,-15,-17,-33,-45,-85]);
q
q = menFromBoys([12, 89, -38, -78]) //, [-78,-38,12,89]);
q
q = menFromBoys([2, -43, 95, -90, 37]) // , [-90,2,95,37,-43]);
q
q = menFromBoys([82, -61, -87, -12, 21, 1]) //, [-12,82,21,1,-61,-87]);
q
q = menFromBoys([63, -57, 76, -85, 88, 2, -28]) //, [-28,2,76,88,63,-57,-85]);
q
q = menFromBoys([49, 818, -282, 900, 928, 281, -282, -1]) //, [-282,818,900,928,281,49,-1]);
q