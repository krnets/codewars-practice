namespace Solution
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class Sample_Test
    {
        private static IEnumerable<TestCaseData> testCases
        {
            get
            {
                yield return new TestCaseData(1).Returns("mocha_missing!");
                yield return new TestCaseData(3).Returns("Java");
                yield return new TestCaseData(6).Returns("JavaScript");
                yield return new TestCaseData(12).Returns("CoffeeScript");
            }
        }

        [Test, TestCaseSource("testCases")]
        public string Test(int n) => Kata.CaffeineBuzz(n);
    }
}