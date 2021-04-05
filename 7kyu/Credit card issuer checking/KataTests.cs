namespace Solution
{
    using NUnit.Framework;

    [TestFixture]
    public class Tests
    {
        [TestCase(4111111111111111, "VISA")]
        [TestCase(6011111111111117, "Discover")]
        [TestCase(9111111111111111, "Unknown")]
        [TestCase(9111111111111111, "Unknown")]
        [TestCase(4012888888881881, "VISA")]
        [TestCase(378282246310005, "AMEX")]
        [TestCase(5105105105105100, "Mastercard")]
        [TestCase(5105105105105106, "Mastercard")]
        public void SampleTests(long input, string result)
        {
            Assert.That(Kata.getIssuer(input), Is.EqualTo(result));
        }
    }
}