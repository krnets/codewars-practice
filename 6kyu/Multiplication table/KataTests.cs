namespace Solution
{
    using NUnit.Framework;


    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void MyTest()
        {
            int[,] expected = new int[,] {{1, 2, 3}, {2, 4, 6}, {3, 6, 9}};
            Assert.AreEqual(expected, Solution.MultiplicationTable(3));
        }
    }
}