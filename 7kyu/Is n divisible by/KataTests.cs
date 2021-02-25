namespace Codewars
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual(false, KataChallenge.IsDivisible(3, 3, 4));
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual(true, KataChallenge.IsDivisible(12, 3, 4));
        }
    }
}