namespace smile67Kata
{
    using NUnit.Framework;

    [TestFixture]
    public class smile67KataTest
    {
        [Test]
        public void smile67KataTest_withoutRandom1()
        {
            Assert.AreEqual(256, new Kata().nextHigher(128));
        }

        [Test]
        public void smile67KataTest_withoutRandom2()
        {
            Assert.AreEqual(2, new Kata().nextHigher(1));
        }

        [Test]
        public void smile67KataTest_withoutRandom3()
        {
            Assert.AreEqual(1279, new Kata().nextHigher(1022));
        }

        [Test]
        public void smile67KataTest_withoutRandom4()
        {
            Assert.AreEqual(191, new Kata().nextHigher(127));
        }

        [Test]
        public void smile67KataTest_withoutRandom5()
        {
            Assert.AreEqual(1253359, new Kata().nextHigher(1253343));
        }
    }
}