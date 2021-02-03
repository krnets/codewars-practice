namespace AsciiResort
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SlopeTest
    {
        [Test]
        public void SampleDecimal()
        {
            string result = Slope.DetermineCool(10, "ThisIsADecimal");
            Console.WriteLine(result);
            Assert.AreEqual("1348", result);
        }
    }
}