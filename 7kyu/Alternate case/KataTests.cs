namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void MyTest()
        {
            Assert.AreEqual("ABC", Program.alternateCase("abc"));
            Assert.AreEqual("abc", Program.alternateCase("ABC"));
            Assert.AreEqual("hELLO wORLD", Program.alternateCase("Hello World"));
        }
    }
}