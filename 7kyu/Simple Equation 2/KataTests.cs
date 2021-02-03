namespace SolveIt
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Test
    {
        [Test]
        public void PlusTest()
        {
            Assert.AreEqual(957737, Kata.result("854+584   + 956201   +98+0"),
                string.Format("Expect {0}, but it was {1}", 957737, Kata.result("854+584   + 956201   +98+0")));
        }

        [Test]
        public void MinusTest()
        {
            Assert.AreEqual(-956029, Kata.result("854-584   - 956201   -98-0"),
                string.Format("Expect {0}, but it was {1}", -956029, Kata.result("854-584   - 956201   -98-0")));
        }

        [Test]
        public void PlusMinusTest()
        {
            Assert.AreEqual(-954665, Kata.result("854+584   - 956201   +98-0"),
                string.Format("Expect {0}, but it was {1}", -954665, Kata.result("854+584   - 956201   +98-0")));
        }
    }
}