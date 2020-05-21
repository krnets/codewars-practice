// const summation = (n) => Array.from({length: n}, (v,k) => k + 1).reduce((a,b) => a + b)
const summation = n => n * (n + 1) / 2;

q = summation(12)
q



// describe('summation', function () {
//     it('should return the correct total', function () {
//       Test.assertEquals(summation(1), 1)
//       Test.assertEquals(summation(8), 36)
//     })
//   })
  