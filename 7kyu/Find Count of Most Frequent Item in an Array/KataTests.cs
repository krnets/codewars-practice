namespace Solution {
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
    
        private static object[] Basic_Test_Cases = new object[]
        {
            new object[] {new int[] {3, -1, -1}, 2},
            new object[] {new int[] {3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3}, 5},
        };
  

        [Test, TestCaseSource(typeof(SolutionTest), "Basic_Test_Cases")]
        public void Basic_Test(int[] test, int expected)
        {
            Assert.AreEqual(expected, Kata.MostFrequentItemCount(test));
        }
    
        // Note: Random tests output total user code execution time
    }
}