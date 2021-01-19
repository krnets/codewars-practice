namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class KataTests
    {
        [Test]
        public void BasicTests()
        {
            Assert.AreEqual("one,three,two", string.Join(",", Kata.SortMe(new[] { "one", "two", "three" })));
        }
    }
}