namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture, Description("Example tests")]
    public class ExampleTests
    {
        [Test, Description("Should handle sample case")]
        public void ExampleTest()
        {
            Assert.That(Kata.RemoveDuplicateWords("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), Is.EqualTo("alpha beta gamma delta"));
        }
    }
}