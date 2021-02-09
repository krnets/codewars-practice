namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class ExampleTests
    {
        [Test]
        public void LongestAtTheBeginning()
        {
            Assert.AreEqual(new Tuple<char?, int>('a', 4), Kata.LongestRepetition("aaaabb"));
            Assert.AreEqual(new Tuple<char?, int>('b', 5), Kata.LongestRepetition("abbbbb"));
        }

        [Test]
        public void LongestAtTheEnd()
        {
            Assert.AreEqual(new Tuple<char?, int>('a', 4), Kata.LongestRepetition("bbbaaabaaaa"));
        }

        [Test]
        public void LongestInTheMiddle()
        {
            Assert.AreEqual(new Tuple<char?, int>('u', 3), Kata.LongestRepetition("cbdeuuu900"));
        }

        [Test]
        public void MultipleLongest1()
        {
            Assert.AreEqual(new Tuple<char?, int>('b', 1), Kata.LongestRepetition("ba"));
        }

        [Test]
        public void MultipleLongest2()
        {
            Assert.AreEqual(new Tuple<char?, int>('a', 2), Kata.LongestRepetition("aabb"));
        }

        [Test]
        public void EmptyString()
        {
            Assert.AreEqual(new Tuple<char?, int>(null, 0), Kata.LongestRepetition(""));
        }
    }
}