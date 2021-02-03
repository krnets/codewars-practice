using NUnit.Framework;

namespace myjinxin
{
    [TestFixture]
    public class myjinxin
    {
        [Test]
        public void BasicTest1()
        {
            var kata = new Kata();

            Assert.AreEqual(new[] {-1, 3, -1, 2, 4}, kata.ArrayPreviousLess(new[] {3, 5, 2, 4, 5}));
        }

        [Test]
        public void BasicTest2()
        {
            var kata = new Kata();
            Assert.AreEqual(new[] {-1, -1, -1, 1, 3, 4, 4, 1},
                kata.ArrayPreviousLess(new[] {2, 2, 1, 3, 4, 5, 5, 3}));
        }

        [Test]
        public void BasicTest3()
        {
            var kata = new Kata();
            Assert.AreEqual(new[] {-1, -1, -1}, kata.ArrayPreviousLess(new[] {3, 2, 1}));
        }
    }
}