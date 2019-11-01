function copy(array, start, stop, place) {
    let originalLength = array.length;
    let begin = [];
    let a = [];
    let positionToInsert = [];
    let temp = [];
    let end = [];
    let middleCutOut = array.slice(start, stop);
    let newStart = start + stop;

    if (Math.abs(place) > originalLength) {
        return array;
    }

    if (start >= 0)
        begin = array.slice(0, start)

    if (start < 0 && stop < 0)
        a = array.slice(newStart)

    if (middleCutOut.length == 0)
        middleCutOut = a

    if (place >= 0) {
        end = array.splice(place + middleCutOut.length)
        positionToInsert = array.splice(place, middleCutOut.length)
        temp = array.concat(middleCutOut).concat(end)
    } else {
        positionToInsert = array.splice(place)
        temp = array.concat(middleCutOut)
    }

    return temp.length == originalLength ? temp : temp.slice(0, originalLength);
}

// q = copy ([14, 0, 17], 4,-9,3)
// Expected: [14, 0, 17], instead got: [14, 0, 17, 18, 11, 16, 13, 3]
// q

// q = copy([9, 11, 7, 15, 8, 16], 4,8,-8)
// Expected: [9, 11, 7, 15, 8, 16], 
// instead got: [9, 11, 7, 15, 8, 16, 8, 16, 8, 16]
// q

// q = copy([10, 9, 2], 14,-1,-9)
// q
// q = copy([18, 10, 15, 8], -4, 1, 4)
// Expected: [18, 10, 15, 8], 
// tead got: [18, 10, 15, 8, 2]
// q

// q = copy ([11, 17, 7, 12, 10], -1,-11,19)
// Expected: [11, 17, 7, 12, 10], 
// tead got: [11, 17, 7, 12, 10, 11, 17, 7, 12, 10]
// q

// q = copy(["A", "B", "C", "D", "E", "F", "G"], 1, 5, 2)
// q
// q = copy([1, 2, 3, 4, 5], 0, 2, -2) // [1, 2, 3, 1, 2]
// q
// q = copy([1, 2, 3, 4, 5], 3, 4, 0) //, [4, 2, 3, 4, 5]
// q
// q = copy([1, 2, 3, 4, 5], -1, -2, -3) //, [1, 2, 3, 4, 5]
// q
// q = copy(["Banana", "Orange", "Apple", "Mango"], 0, 2, 2) //, ["Banana", "Orange", "Banana", "Orange"]
// q
// q = copy(["C", "W", "W", "W"], 1, 2, 0) // ["W", "W", "W", "W"]
// q
// q = copy(["Hackathon", "Katathon", "Code", "CodeWars", "Laptop", "Macbook", "JavaScript"], 1, 5, 2) 
// // // ["Hackathon","Katathon","Katathon","Code","CodeWars","Laptop","JavaScript"]
// q