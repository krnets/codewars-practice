namespace Solution
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    public class AddBinaryTest
    {
        [Test]
        public void Test_One_Two()
        {
            Assert.AreEqual("11", Kata.AddBinary(1, 2), "Should return \"11\" for 1 + 2");
        }

        [Test]
        public void Test_FiftyOne_Twelve()
        {
            Assert.AreEqual("111111", Kata.AddBinary(51, 12), "Should return \"111111\" for 51 + 12");
        }

        [Test]
        public void Test_Hundred_Zero()
        {
            Assert.AreEqual("1100100", Kata.AddBinary(100, 0), "Should return \"1100100\" for 100 + 0");
        }
    }

    [TestFixture]
    public class RandomAddBinaryTest
    {
        private static Random rnd = new Random();

        private static IEnumerable<TestCaseData> randomTestCases
        {
            get
            {
                const int Tests = 100;
                for (int i = 0; i < Tests; ++i)
                {
                    int a = rnd.Next(0, 100000);
                    int b = rnd.Next(0, 100000);

                    string expected = Convert.ToString(a + b, 2);

                    yield return new TestCaseData(a, b).Returns(expected)
                        .SetDescription($"Should return \"{expected}\" for {a} + {b}");
                }
            }
        }

        [Test, TestCaseSource("randomTestCases")]
        public string Random_Tests(int a, int b) => Kata.AddBinary(a, b);
    }
}