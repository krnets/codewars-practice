function countPositivesSumNegatives(input) {
    let negInts = 0;
    let countPosInts = 0;

    if (!input || input.length == 0) {
        return []
    }

    for (let i = 0; i < input.length; i++) {
        if (input[i] > 0) {
            countPosInts++
        } else {
            negInts += input[i]
        }
    }
    return [countPosInts, negInts]
}


var testData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15];
// var testData = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14];
// var testData = []
q = countPositivesSumNegatives(testData)
q

// describe("Example tests", function(){
//     var testData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15];
//     var actual = countPositivesSumNegatives(testData);
//     var expected = [10, -65];

//     Test.expect(actual[0] == expected[0] && actual[1] == expected[1], "Wrong return value.");
    
//     testData = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14];
//     actual = countPositivesSumNegatives(testData);
//     expected = [8, -50];
    
//     Test.expect(actual[0] == expected[0] && actual[1] == expected[1], "Wrong return value.");
// });