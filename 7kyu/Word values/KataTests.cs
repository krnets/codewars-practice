namespace Solution
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class SolutionTest
    {
        private static IEnumerable<TestCaseData> sampleTestCases
        {
            get
            {
                yield return new TestCaseData(new[] {new[] {"codewars", "abc", "xyz"}})
                    .Returns(new[] {88, 12, 225});

                yield return new TestCaseData(new[] {new[] {"abc abc", "abc abc", "abc", "abc"}})
                    .Returns(new[] {12, 24, 18, 24});
            }
        }

        [Test, TestCaseSource("sampleTestCases")]
        public int[] SampleTest(string[] a) => Kata.WordValue(a);
    }
}