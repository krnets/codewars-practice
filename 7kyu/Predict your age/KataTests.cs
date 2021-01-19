namespace Solution
{
    using NUnit.Framework;
    using System;
    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void FixedTest()
        {
            Assert.AreEqual(86, Predicter.PredictAge(65, 60, 75, 55, 60, 63, 64, 45));
            Assert.AreEqual(79, Predicter.PredictAge(32, 54, 76, 65, 34, 63, 64, 45));
        }
    }
}