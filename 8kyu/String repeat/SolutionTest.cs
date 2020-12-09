using NUnit.Framework;

namespace Kata
{
    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void test1()
        {
            Assert.AreEqual("***", Program.repeatStr(3, "*"));
        }

        [Test]
        public void test2()
        {
            Assert.AreEqual("#####", Program.repeatStr(5, "#"));
        }

        [Test]
        public void test3()
        {
            Assert.AreEqual("ha ha ", Program.repeatStr(2, "ha "));
        }
    }
}