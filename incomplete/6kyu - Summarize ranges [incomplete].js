// 6kyu - Summarize ranges

// function summaryRanges(nums) {
//     let result = []
//     nums
//     nums.unshift(0)

    // for (let i = 1; i < nums.length; i++) {
    //     if(nums[i] == (nums[i-1] + 1)) {
    //         result.push(nums[i])
    //     } else {
    //         continue
    //     }
    // }
    // return result
// }

function summaryRanges(nums) {
    let a = nums.filter((v,i) =>nums.indexOf(v) == i)
    a
    // let b = a.reduce((prev,curr,index) => curr - prev == 1 ? j)
    // b

}

// q = summaryRanges([]),[]
// q
// q = summaryRanges([1,1,1,1]),['1']
// q
// q = summaryRanges([1,2,3,4]),['1->4']
// q
// q = summaryRanges([0, 1, 2, 5, 6, 9]),["0->2", "5->6", "9"]
// q
// q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]),["0->7"]
// q
// q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7]),["0->7"]
// q
// q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]), ["0->7","9->10"]
// q
// q = summaryRanges([-2,0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]),["-2", "0->7", "9->10", "12"]
// q