const take = (arr, n) => arr.slice(0, n)

q = take([0,1,2,3,5,8,13], 3)
q


// describe("Sample Tests", function(){
//     it("should work for sample tests", function(){
//       Test.assertDeepEquals(take([0, 1, 2, 3, 5, 8, 13], 3), [0, 1, 2], "should return the first 3 items");
//     });
//   });