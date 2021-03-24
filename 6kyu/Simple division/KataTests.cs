using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SampleTest
{
    private static IEnumerable<TestCaseData> testCases
    {
        get
        {
            yield return new TestCaseData(2, 256).Returns(true);
            yield return new TestCaseData(2, 253).Returns(false);
            yield return new TestCaseData(9, 243).Returns(true);
            yield return new TestCaseData(15, 12).Returns(false);
            yield return new TestCaseData(21, 2893401).Returns(true);
            yield return new TestCaseData(21, 2893406).Returns(false);
            yield return new TestCaseData(54, 2834352).Returns(true);
            yield return new TestCaseData(54, 2834359).Returns(false);
            yield return new TestCaseData(1000013, 7187761).Returns(true);
            yield return new TestCaseData(1000013, 7187762).Returns(false);
        }
    }

    [Test, TestCaseSource("testCases")]
    public bool Test(int a, int b) =>
        Kata.Solve(a, b);
}