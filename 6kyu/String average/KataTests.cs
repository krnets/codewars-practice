namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Test
    {
        [Test]
        public void SampleTestEmpty()
        {
            Assert.AreEqual("n/a", Kata.AverageString(""));
        }

        [Test]
        public void SampleTest0()
        {
            Assert.AreEqual("zero", Kata.AverageString("zero zero zero zero zero"));
        }

        [Test]
        public void SampleTest2()
        {
            Assert.AreEqual("two", Kata.AverageString("one one eight one"));
        }

        [Test]
        public void SampleTest3A()
        {
            Assert.AreEqual("three", Kata.AverageString("four six two three"));
        }

        [Test]
        public void SampleTest3B()
        {
            Assert.AreEqual("three", Kata.AverageString("one two three four five"));
        }

        [Test]
        public void SampleTest4A()
        {
            Assert.AreEqual("four", Kata.AverageString("zero nine five two"));
        }

        [Test]
        public void SampleTest4B()
        {
            Assert.AreEqual("four", Kata.AverageString("five four"));
        }
    }
}