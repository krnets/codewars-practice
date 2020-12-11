using NUnit.Framework;

namespace Solution 
{
    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void SampleTest()
        {
            Assert.AreEqual(new[] {3, 5}, Kata.Divisors(15));
            Assert.AreEqual(new[] {2, 4, 8}, Kata.Divisors(16));
            Assert.AreEqual(new[] {11, 23}, Kata.Divisors(253));
            Assert.AreEqual(new[] {2, 3, 4, 6, 8, 12}, Kata.Divisors(24));
        }
    }
}