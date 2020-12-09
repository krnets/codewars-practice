namespace Solution
{
    using NUnit.Framework;

    [TestFixture]
    public class BasicTests
    {
        [Test]
        public void test1()
        {
            Assert.IsTrue(Kata.IsIsogram("Dermatoglyphics"));
        }

        [Test]
        public void test2()
        {
            Assert.IsTrue(Kata.IsIsogram("isogram"));
        }

        [Test]
        public void test3()
        {
            Assert.IsFalse(Kata.IsIsogram("moose"));
        }

        [Test]
        public void test4()
        {
            Assert.IsFalse(Kata.IsIsogram("isIsogram"));
        }

        [Test]
        public void test5()
        {
            Assert.IsFalse(Kata.IsIsogram("aba"));
        }

        [Test]
        public void test6()
        {
            Assert.IsFalse(Kata.IsIsogram("moOse"));
        }
    }
}