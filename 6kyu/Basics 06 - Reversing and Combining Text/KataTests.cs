namespace smile67Kata
{
    using NUnit.Framework;

    [TestFixture]
    public class smile67KataTest
    {
        [Test]
        public void smile67KataTest_withoutRandom1()
        {
            Assert.AreEqual("cbafed", new Kata().reverseAndCombineText("abc def"));
        }

        [Test]
        public void smile67KataTest_withoutRandom2()
        {
            // Assert.AreEqual("defabcjklghi", new Kata().reverseAndCombineText("abc def ghi jkl"));
        }

        [Test]
        public void smile67KataTest_withoutRandom3()
        {
            Assert.AreEqual("cbafed", new Kata().reverseAndCombineText("cbafed"));
        }

        [Test]
        public void smile67KataTest_withoutRandom4()
        {
            Assert.AreEqual("trzwqfdstrteettr45hh4325543544hjhjh21lllll",
                new Kata().reverseAndCombineText("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12  44"));
        }

        [Test]
        public void smile67KataTest_withoutRandom5()
        {
            Assert.AreEqual("gffds432243fdsfdseewttf", new Kata().reverseAndCombineText("sdfsdf wee sdffg 342234 ftt"));
        }
    }
}