using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    private static object[] Basic_Test_Cases = new object[]
    {
        new object[] {384000000, 42},
    };

    [Test, TestCaseSource(typeof(SolutionTest), "Basic_Test_Cases")]
    public void Basic_Test(double distance, int? expected)
    {
        Assert.AreEqual(expected, Kata.FoldTo(distance));
    }
}