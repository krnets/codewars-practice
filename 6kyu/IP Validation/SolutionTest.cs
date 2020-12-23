namespace Solution
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void TestCase1()
        {
            Assert.AreEqual(true, Kata.is_valid_IP("0.0.0.0"));
        }

        [Test]
        public void TestCase2()
        {
            Assert.AreEqual(true, Kata.is_valid_IP("12.255.56.1"));
        }

        [Test]
        public void TestCase3()
        {
            Assert.AreEqual(true, Kata.is_valid_IP("137.255.156.100"));
        }

        [Test]
        public void TestCase4()
        {
            Assert.AreEqual(false, Kata.is_valid_IP(""));
        }

        [Test]
        public void TestCase5()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("abc.def.ghi.jkl"));
        }

        [Test]
        public void TestCase6()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("123.456.789.0"));
        }

        [Test]
        public void TestCase7()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56"));
        }

        [Test]
        public void TestCase8()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56.00"));
        }

        [Test]
        public void TestCase9()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56.7.8"));
        }

        [Test]
        public void TestCase10()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.256.78"));
        }

        [Test]
        public void TestCase11()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("1234.34.56"));
        }

        [Test]
        public void TestCase12()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("pr12.34.56.78"));
        }

        [Test]
        public void TestCase13()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56.78sf"));
        }

        [Test]
        public void TestCase14()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56 .1"));
        }

        [Test]
        public void TestCase15()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("12.34.56.-1"));
        }

        [Test]
        public void TestCase16()
        {
            Assert.AreEqual(false, Kata.is_valid_IP("123.045.067.089"));
        }
    }
}