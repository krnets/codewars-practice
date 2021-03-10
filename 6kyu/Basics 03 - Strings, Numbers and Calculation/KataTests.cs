namespace smile67Kata
{
    using NUnit.Framework;

    [TestFixture]
    public class smile67KataTest
    {
        [Test]
        public void smile67KataTest_withoutRandom1()
        {
            Assert.AreEqual("47", new Kata().calculateString(";$%�fsdfsd235??df/sdfgf5gh.000kk0000"));
        }

        [Test]
        public void smile67KataTest_withoutRandom2()
        {
            Assert.AreEqual("54929268", new Kata().calculateString("sdfsd23454sdf*2342"));
        }

        [Test]
        public void smile67KataTest_withoutRandom3()
        {
            Assert.AreEqual("-210908", new Kata().calculateString("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"));
        }

        [Test]
        public void smile67KataTest_withoutRandom4()
        {
            Assert.AreEqual("234676", new Kata().calculateString("fsdfsd234.4554s4234df+sf234442"));
        }
    }
}