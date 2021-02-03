namespace myjinxin
{
    using NUnit.Framework;

    [TestFixture]
    public class myjinxin
    {
        [Test]
        public void BasicTest1()
        {
            var kata = new Kata();
            Assert.AreEqual(14, kata.SwapAdjacentBits(13), "");
        }

        [Test]
        public void BasicTest2()
        {
            var kata = new Kata();
            Assert.AreEqual(133, kata.SwapAdjacentBits(74), "");
        }

        [Test]
        public void BasicTest3()
        {
            var kata = new Kata();
            Assert.AreEqual(1073741823, kata.SwapAdjacentBits(1073741823), "");
        }

        [Test]
        public void BasicTest4()
        {
            var kata = new Kata();
            Assert.AreEqual(0, kata.SwapAdjacentBits(0), "");
        }

        [Test]
        public void BasicTest5()
        {
            var kata = new Kata();
            Assert.AreEqual(2, kata.SwapAdjacentBits(1), "");
        }

        [Test]
        public void BasicTest6()
        {
            var kata = new Kata();
            Assert.AreEqual(166680, kata.SwapAdjacentBits(83748), "");
        }
    }
}