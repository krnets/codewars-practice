namespace Solution
{
    using NUnit.Framework;
    using System;
    using Kata;

    [TestFixture]
    public class Test
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual("TestCase", "test case".CamelCase());
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual("CamelCaseMethod", "camel case method".CamelCase());
        }

        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual("SayHello", "say hello".CamelCase());
        }

        [Test]
        public void BasicTest4()
        {
            Assert.AreEqual("CamelCaseWord", " camel case word".CamelCase());
        }

        [Test]
        public void BasicTest5()
        {
            Assert.AreEqual("", "".CamelCase());
        }
    }
}