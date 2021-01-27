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

            Assert.AreEqual(true, kata.InviteMoreWomen(new int[] {1, -1, 1}));

            Assert.AreEqual(true, kata.InviteMoreWomen(new int[] {1, 1, 1}));

            Assert.AreEqual(false, kata.InviteMoreWomen(new int[] {-1, -1, -1}));

            Assert.AreEqual(false, kata.InviteMoreWomen(new int[] {1, -1}));
        }
    }
}