namespace Kata
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class ArrayMathTest
    {
        [Test]
        public void BasicTests()
        {
            Assert.AreEqual(540, ArrayMath.Product(new int[] {5, 4, 1, 3, 9}));
            Assert.AreEqual(-672, ArrayMath.Product(new int[] {-2, 6, 7, 8}));
            Assert.AreEqual(10, ArrayMath.Product(new int[] {10}));
            Assert.AreEqual(0, ArrayMath.Product(new int[] {0, 2, 9, 7}));
        }

        [Test]
        public void ArgumentNullTest()
        {
            Assert.Throws<ArgumentNullException>(() => { ArrayMath.Product(null); });
        }

        [Test]
        public void InvalidOperationTest()
        {
            Assert.Throws<InvalidOperationException>(() => { ArrayMath.Product(new int[] { }); });
        }
    }
}