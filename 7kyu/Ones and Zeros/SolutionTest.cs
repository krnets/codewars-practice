using NUnit.Framework;

namespace Solution
{
    [TestFixture]
    public class SolutionTest
    {
        int[] Test1 = {0, 0, 0, 0};
        int[] Test2 = {1, 1, 1, 1};
        int[] Test3 = {0, 1, 1, 0};
        int[] Test4 = {0, 1, 0, 1};

        [Test]
        public void BasicTesting()
        {
            Assert.AreEqual(0, Kata.binaryArrayToNumber(Test1));
            Assert.AreEqual(15, Kata.binaryArrayToNumber(Test2));
            Assert.AreEqual(6, Kata.binaryArrayToNumber(Test3));
            Assert.AreEqual(5, Kata.binaryArrayToNumber(Test4));
        }

        int[] Test5 = {1, 0, 1, 1};
        int[] Test6 = {1, 0, 0, 1};
        int[] Test7 = {0, 0, 0, 1};
        int[] Test8 = {1, 0, 1, 0};
        int[] Test9 = {1, 0, 0, 0};
        int[] Test10 = {0, 1, 0, 0};

        [Test]
        public void MoreTests()
        {
            Assert.AreEqual(11, Kata.binaryArrayToNumber(Test5));
            Assert.AreEqual(9, Kata.binaryArrayToNumber(Test6));
            Assert.AreEqual(1, Kata.binaryArrayToNumber(Test7));
            Assert.AreEqual(10, Kata.binaryArrayToNumber(Test8));
            Assert.AreEqual(8, Kata.binaryArrayToNumber(Test9));
            Assert.AreEqual(4, Kata.binaryArrayToNumber(Test10));
        }
    }
}