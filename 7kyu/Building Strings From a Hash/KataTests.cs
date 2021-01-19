namespace Solution
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class SolutionTest
    {
        [Test, Description("Basic Tests")]
        public void Test()
        {
            Assert.AreEqual("a = 1,b = 2", Kata.StringifyDict(new Dictionary<char, int> { { 'a', 1 }, { 'b', 2 } }));
            Assert.AreEqual("b = 1,c = 2,e = 3", Kata.StringifyDict(new Dictionary<char, int> { { 'b', 1 }, { 'c', 2 }, { 'e', 3 } }));
            Assert.AreEqual("", Kata.StringifyDict(new Dictionary<char, int>()));
        }
    }
}