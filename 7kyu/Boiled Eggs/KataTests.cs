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
            Assert.AreEqual(0, Kata.CookingTime(0), "0 eggs");
            Assert.AreEqual(5, Kata.CookingTime(5), "5 eggs");
            Assert.AreEqual(10, Kata.CookingTime(10), "10 eggs");
        }
    }
}