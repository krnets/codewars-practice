var array1 = [true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ];
    
function countSheeps(array) {
    // let total = 0
    // for (let i = 0; i < array.length; i++) {
    //     if (array[i] == true) {
    //         total++
    //     }
    //  }
    // return total
    // return array.reduce((total, current) => current + total)
    return array.filter(Boolean).length
    // return array.filter(x => x).length
    // return array.reduce((result, current) => {
    //     if (current) result++;
    //     return result
    // },0)
}

q = countSheeps(array1)
q

    
// Test.expect(countSheeps(array1) == 17, "There are 17 sheeps in total")
