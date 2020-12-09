namespace Solution
{
    using NUnit.Framework;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void ExampleTest1()
        {
            Assert.AreEqual(true, Kata.XO("xo"));
        }

        [Test]
        public void ExampleTest2()
        {
            Assert.AreEqual(true, Kata.XO("xxOo"));
        }

        [Test]
        public void ExampleTest3()
        {
            Assert.AreEqual(false, Kata.XO("xxxm"));
        }

        [Test]
        public void ExampleTest4()
        {
            Assert.AreEqual(false, Kata.XO("Oo"));
        }

        [Test]
        public void ExampleTest5()
        {
            Assert.AreEqual(false, Kata.XO("ooom"));
        }

        [Test]
        public void ExampleTest6()
        {
            Assert.AreEqual(true, Kata.XO("XO"));
            Assert.AreEqual(true, Kata.XO("xo0"));
            Assert.AreEqual(true, Kata.XO("xxxxxoooxooo"));
            Assert.AreEqual(false, Kata.XO("Oo"));
            Assert.AreEqual(false, Kata.XO("xxxoo"));
            Assert.AreEqual(true, Kata.XO(""), "Empty string contains equal amount of x and o");
            Assert.AreEqual(true, Kata.XO("abcdefghijklmnopqrstuvwxyz"), "Alphabet contains equal amount of x and o");
        }
    }
}