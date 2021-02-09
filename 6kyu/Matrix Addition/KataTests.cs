namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void SampleTest()
        {
            Assert.AreEqual(new int[][]
            {
                new int[] {3, 5},
                new int[] {3, 5}
            }, Kata.MatrixAddition(new int[][]
                {
                    new int[] {1, 2},
                    new int[] {1, 2}
                },
                new int[][]
                {
                    new int[] {2, 3},
                    new int[] {2, 3}
                }));
        }
    }
}