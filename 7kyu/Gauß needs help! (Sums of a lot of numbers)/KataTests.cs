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
                yield return new TestCaseData(0).Returns(null);
                yield return new TestCaseData(100l).Returns(5050l);
                yield return new TestCaseData(300l).Returns(45150l);
                yield return new TestCaseData(50000l).Returns(1250025000l);
            }
        }

        [Test, TestCaseSource("testCases")]
        public long? Test(long n) => Kata.RangeSum(n);
    }
}