namespace Solution
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class CalculateStringRotationTests
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual(4, CalculateStringRotation.ShiftedDiff("eecoff", "coffee"));
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual(-1, CalculateStringRotation.ShiftedDiff("Moose", "moose"));
        }

        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual(2, CalculateStringRotation.ShiftedDiff("isn't", "'tisn"));
        }

        [Test]
        public void BasicTest4()
        {
            Assert.AreEqual(0, CalculateStringRotation.ShiftedDiff("Esham", "Esham"));
        }

        [Test]
        public void BasicTest5()
        {
            Assert.AreEqual(0, CalculateStringRotation.ShiftedDiff(" ", " "));
        }

        [Test]
        public void BasicTest6()
        {
            Assert.AreEqual(-1, CalculateStringRotation.ShiftedDiff("hoop", "pooh"));
        }

        [Test]
        public void BasicTest7()
        {
            Assert.AreEqual(-1, CalculateStringRotation.ShiftedDiff("  ", " "));
        }

        [Test]
        public void BasicTest8()
        {
            Assert.AreEqual(2, CalculateStringRotation.ShiftedDiff("coffee", "eecoff"));
        }
    }
}