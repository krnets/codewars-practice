// 6kyu - Summarize ranges

function summaryRanges(nums) {
    nums = [...new Set(nums)]

    let parted = []
    let marker = []

    for (let i = 0; i < nums.length; i++) {
        marker.push(nums[i])
        if (nums[i + 1] - nums[i] != 1) {
            parted.push(marker)
            marker = []
        }
    }

    return parted.map(v =>
        v.length == 1 ?
        v + '' :
        v[0] + '->' + v[v.length - 1])
}

q = summaryRanges([]), []
q
q = summaryRanges([1, 1, 1, 1]), ['1']
q
q = summaryRanges([1, 2, 3, 4]), ['1->4']
q
q = summaryRanges([0, 1, 2, 5, 6, 9]), ["0->2", "5->6", "9"]
q
q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]), ["0->7"]
q
q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7]), ["0->7"]
q
q = summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]), ["0->7", "9->10"]
q
q = summaryRanges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]), ["-2", "0->7", "9->10", "12"]
q