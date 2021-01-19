namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Test
    {
        [Test]
        public void SampleTest1()
        {
            Assert.AreEqual(0, Kata.Gimme(new double[] { 2, 3, 1 }));
        }
        [Test]
        public void SampleTest2()
        {
            Assert.AreEqual(1, Kata.Gimme(new double[] { 5, 10, 14 }));
        }
    }
}