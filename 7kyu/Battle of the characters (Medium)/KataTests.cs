namespace Solution {
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void SampleTests()
        {
            Assert.AreEqual("Two", Kata.Battle("One", "Two"));
            Assert.AreEqual("One", Kata.Battle("One", "Neo"));
            Assert.AreEqual("Tie!", Kata.Battle("One", "neO"));
            Assert.AreEqual("Tie!", Kata.Battle("Foo", "BAR"));
            Assert.AreEqual("Four", Kata.Battle("Four", "Five"));
        }
    }
}