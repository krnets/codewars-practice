namespace TransformToPrime
{
    using NUnit.Framework;
    using System;
    using System.Linq;

    [TestFixture]
    public class Tests
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual(1, Solution.MinimumNumber(new int[] {3, 1, 2}));
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual(0, Solution.MinimumNumber(new int[] {5, 2}));
        }

        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual(0, Solution.MinimumNumber(new int[] {1, 1, 1}));
        }

        [Test]
        public void BasicTest4()
        {
            Assert.AreEqual(5, Solution.MinimumNumber(new int[] {2, 12, 8, 4, 6}));
        }

        [Test]
        public void BasicTest5()
        {
            Assert.AreEqual(2, Solution.MinimumNumber(new int[] {50, 39, 49, 6, 17, 28}));
        }
    }
}