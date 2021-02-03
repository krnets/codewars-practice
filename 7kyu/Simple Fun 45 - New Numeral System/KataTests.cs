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
            Assert.AreEqual(new string[] {"A + G", "B + F", "C + E", "D + D"}, kata.NewNumeralSystem('G'));
        }

        [Test]
        public void BasicTest2()
        {
            var kata = new Kata();
            Assert.AreEqual(new string[] {"A + A"}, kata.NewNumeralSystem('A'));
        }

        [Test]
        public void BasicTest3()
        {
            var kata = new Kata();
            Assert.AreEqual(new string[] {"A + D", "B + C"}, kata.NewNumeralSystem('D'));
        }

        [Test]
        public void BasicTest4()
        {
            var kata = new Kata();
            Assert.AreEqual(new string[] {"A + E", "B + D", "C + C"}, kata.NewNumeralSystem('E'));
        }

        [Test]
        public void BasicTest5()
        {
            var kata = new Kata();
            Assert.AreEqual(new string[] {"A + O", "B + N", "C + M", "D + L", "E + K", "F + J", "G + I", "H + H"},
                kata.NewNumeralSystem('O'));
        }
    }
}