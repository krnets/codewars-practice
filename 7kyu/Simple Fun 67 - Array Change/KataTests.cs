namespace myjinxin
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class myjinxin
    {
        [Test]
        public void BasicTest1()
        {
            var kata = new Kata();

            Assert.AreEqual(3, kata.ArrayChange(new int[] {1, 1, 1}));
        }

        [Test]
        public void BasicTest2()
        {
            var kata = new Kata();
            Assert.AreEqual(5, kata.ArrayChange(new int[] {-1000, 0, -2, 0}));
        }

        [Test]
        public void BasicTest3()
        {
            var kata = new Kata();
            Assert.AreEqual(12, kata.ArrayChange(new int[] {2, 1, 10, 1}));
        }

        [Test]
        public void BasicTest4()
        {
            var kata = new Kata();
            Assert.AreEqual(13, kata.ArrayChange(new int[] {2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15}));
        }
    }
}