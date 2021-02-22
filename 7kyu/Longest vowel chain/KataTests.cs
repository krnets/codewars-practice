namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void SampleTest1()
        {
            Assert.AreEqual(2, Kata.Solve("codewarriors"));
        }

        [Test]
        public void SampleTest2()
        {
            Assert.AreEqual(3, Kata.Solve("suoidea"));
        }

        [Test]
        public void SampleTest3()
        {
            Assert.AreEqual(3, Kata.Solve("ultrarevolutionariees"));
        }

        [Test]
        public void SampleTest4()
        {
            Assert.AreEqual(1, Kata.Solve("strengthlessnesses"));
        }

        [Test]
        public void SampleTest5()
        {
            Assert.AreEqual(2, Kata.Solve("cuboideonavicuare"));
        }

        [Test]
        public void SampleTest6()
        {
            Assert.AreEqual(5, Kata.Solve("chrononhotonthuooaos"));
        }

        [Test]
        public void SampleTest7()
        {
            Assert.AreEqual(8, Kata.Solve("iiihoovaeaaaoougjyaw"));
        }
    }
}