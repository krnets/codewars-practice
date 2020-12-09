namespace Solution
{
    using NUnit.Framework;

    [TestFixture]
    public class KataTests
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual(3, Kata.FindShort("bitcoin take over the world maybe who knows perhaps"));
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual(3, Kata.FindShort("turns out random test cases are easier than writing out basic ones"));
        }

        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual(3, Kata.FindShort("lets talk about javascript the best language"));
        }

        [Test]
        public void BasicTest4()
        {
            Assert.AreEqual(1, Kata.FindShort("i want to travel the world writing code one day"));
        }

        [Test]
        public void BasicTest5()
        {
            Assert.AreEqual(2, Kata.FindShort("Lets all go on holiday somewhere very cold"));
        }
    }
}