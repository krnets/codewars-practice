namespace myjinxin
{
    using NUnit.Framework;

    [TestFixture]
    public class myjinxin
    {
        readonly Kata kata = new Kata();

        [Test]
        public void BasicTests1()
        {
            Assert.AreEqual('a', kata.abacaba(1));
        }

        [Test]
        public void BasicTests2()
        {
            Assert.AreEqual('b', kata.abacaba(2));
        }

        [Test]
        public void BasicTests3()
        {
            Assert.AreEqual('a', kata.abacaba(3));
        }

        [Test]
        public void BasicTests4()
        {
            Assert.AreEqual('c', kata.abacaba(4));
        }

        [Test]
        public void BasicTests5()
        {
            Assert.AreEqual('a', kata.abacaba(5));
        }

        [Test]
        public void BasicTests6()
        {
            Assert.AreEqual('b', kata.abacaba(6));
        }

        [Test]
        public void BasicTests7()
        {
            Assert.AreEqual('a', kata.abacaba(7));
        }

        [Test]
        public void BasicTests8()
        {
            Assert.AreEqual('d', kata.abacaba(8));
        }

        [Test]
        public void BasicTests12()
        {
            Assert.AreEqual('c', kata.abacaba(12));
        }

        [Test]
        public void BasicTests16()
        {
            Assert.AreEqual('e', kata.abacaba(16));
        }
    }
}