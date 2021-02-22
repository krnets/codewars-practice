using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    private static object[] sampleTestCases = new object[]
    {
        new object[] {new double[] {1, 5, 11}, 15},
        new object[] {new double[] {15, 20, 30, 31, 32, 44, 100}, 0},
        new object[] {new double[] {1, 2, 3, 4}, 140},
        new object[] {new double[] { }, 0},
        new object[] {new double[] {1, 2, 3, 4, 5, 6, 7, 8, 9}, 65},
        new object[] {new double[] {0, 5, 10, 10.5, 4.5}, 30},
    };

    [Test, TestCaseSource("sampleTestCases")]
    public void SampleTest(double[] test, int expected)
    {
        Assert.AreEqual(expected, Darts.ScoreThrows(test));
    }
}