namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Test
    {
        [Test]
        public void SampleTest()
        {
            Assert.AreEqual(100, Kata.FindLongest(new int[] { 1, 10, 100 }));
            Assert.AreEqual(9000, Kata.FindLongest(new int[] { 9000, 8, 800 }));
            Assert.AreEqual(900, Kata.FindLongest(new int[] { 8, 900, 500 }));
        }
    }
}