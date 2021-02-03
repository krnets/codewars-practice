namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Tests
    {
        [Test]
        public void ExampleTests()
        {
            const string name = "Alex";
            Assert.AreEqual("Hello, Alex!", name.SayHello());
            Assert.AreEqual("Goodbye, Alex. See you again soon!", name.SayGoodbye());
        }
    }
}