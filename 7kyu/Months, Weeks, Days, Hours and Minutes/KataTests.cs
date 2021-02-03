namespace Solution
{
    using NUnit.Framework;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void FixedTest1()
        {
            Assert.AreEqual("1 minute", Kata.DisplayValue(1));
        }

        [Test]
        public void FixedTest2()
        {
            Assert.AreEqual("1 hour 40 minutes", Kata.DisplayValue(100));
        }

        [Test]
        public void FixedTest3()
        {
            Assert.AreEqual("1 month 1 minute", Kata.DisplayValue(40321));
        }

        [Test]
        public void FixedTest4()
        {
            Assert.AreEqual("1 month 1 week 1 day 17 hours 14 minutes", Kata.DisplayValue(52874));
        }
    }
}