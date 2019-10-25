// class SmallestIntegerFinder {
//     findSmallestInt(args) {
//         return Math.min(...args)
//     }
// }


// class SmallestIntegerFinder {
//     findSmallestInt(args) {
//         let min = Infinity
//         args.forEach((value, index) => {
//             if (value < min) {
//                 min = value
//             }
//         })
//         return min
//     }
// }
class SmallestIntegerFinder {
    findSmallestInt(args) {
        // return args.reduce((accum, current) =>
        //     current < accum ?
        //     current :
        //     accum)
        return Math.min(...args)
    }
} 
p = new SmallestIntegerFinder()
// q = p.findSmallestInt([78, 56, 232, 412, 228])
q = p.findSmallestInt([78,56,-232,12,0])
q

// Test.assertEquals(sif.findSmallestInt([78,56,232,12,8]),8,'Should return the smallest int 8');
// Test.assertEquals(sif.findSmallestInt([78,56,232,12,18]),12,'Should return the smallest int 12');
// Test.assertEquals(sif.findSmallestInt([78,56,232,412,228]),56,'Should return the smallest int 56');
// Test.assertEquals(sif.findSmallestInt([78,56,232,12,0]),0,'Should return the smallest int 0');
// Test.assertEquals(sif.findSmallestInt([1,56,232,12,8]),1,'Should return the smallest int 1');