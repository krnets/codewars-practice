namespace myjinxin
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class myjinxin
    {
        [Test]
        public void BasicTests()
        {
            var kata = new Kata();

            Assert.AreEqual(10, kata.GrowingPlant(100, 10, 910));

            Assert.AreEqual(1, kata.GrowingPlant(10, 9, 4));
        }
    }
}