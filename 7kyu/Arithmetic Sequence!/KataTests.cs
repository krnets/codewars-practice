using NUnit.Framework;
using System;
using System.Collections.Generic;

[TestFixture]
public class SampleTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(1, 2, 3).Returns(7);
            yield return new TestCaseData(2, 2, 2).Returns(6);
            yield return new TestCaseData(-50, 10, 20).Returns(150);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int Test(int first, int n, int c) => Kata.Nthterm(first, n, c);
}