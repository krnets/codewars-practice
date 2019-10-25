function monkeyCount(n) {
    return  Array.from({length: n}, (v,k) => k + 1)
}

q = monkeyCount(8)
q

// Test.describe("monkeyCount", _ => {
//     Test.assertSimilar((monkeyCount(5)), [1, 2, 3, 4, 5]);
//     Test.assertSimilar((monkeyCount(3)), [1, 2, 3]);
//     Test.assertSimilar((monkeyCount(9)), [1, 2, 3, 4, 5, 6, 7, 8, 9]);
//     Test.assertSimilar((monkeyCount(10)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
//     Test.assertSimilar((monkeyCount(20)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);
//   });