using NUnit.Framework;

namespace Solution
{
    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void Test1()
        {
            Assert.AreEqual(new string[2] { "AbCdEf", "aBcDeF" }, Kata.Capitalize("abcdef"));
        }
        [Test]
        public void Test2()
        {
            Assert.AreEqual(new string[2] { "CoDeWaRs", "cOdEwArS" }, Kata.Capitalize("codewars"));
        }
        [Test]
        public void Test3()
        {
            Assert.AreEqual(new string[2] { "AbRaCaDaBrA", "aBrAcAdAbRa" }, Kata.Capitalize("abracadabra"));
        }
        [Test]
        public void Test4()
        {
            Assert.AreEqual(new string[2] { "CoDeWaRrIoRs", "cOdEwArRiOrS" }, Kata.Capitalize("codewarriors"));
        }
    }
}