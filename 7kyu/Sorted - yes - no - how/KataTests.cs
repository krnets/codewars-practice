namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class KataTests
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual("yes, ascending", Kata.IsSortedAndHow(new[] { 1, 2 }));
        }
        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual("yes, descending", Kata.IsSortedAndHow(new[] { 15, 7, 3, -8 }));
        }
        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual("no", Kata.IsSortedAndHow(new[] { 4, 2, 30 }));
        }
    }
}