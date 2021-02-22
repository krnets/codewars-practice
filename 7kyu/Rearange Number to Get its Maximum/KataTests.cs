using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class Basic_Tests
{
    private static IEnumerable<TestCaseData> testCases
    {
        get { yield return new TestCaseData(123).Returns(321); }
    }

    [Test, TestCaseSource("testCases")]
    public int? Test(int num) => Kata.MaxRedigit(num);
}

[TestFixture]
public class Edge_Tests
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(-1).Returns(null);
            yield return new TestCaseData(0).Returns(null);
        }
    }

    [Test, TestCaseSource("testCases")]
    public int? Test(int num) => Kata.MaxRedigit(num);
}