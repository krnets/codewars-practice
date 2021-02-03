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
            Assert.AreEqual("THE qck brwn FOX jmps vr THE lzy DOG",
                Kata.SmallWordHelper("The quick brown fox jumps over the lazy dog"));
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual("I'M jst A smll wrd frm A smll wrd fmly",
                Kata.SmallWordHelper("I'm just a small word from a small word family"));
        }
    }
}