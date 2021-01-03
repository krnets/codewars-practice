using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    private static object[] sampleTestCases = new object[]
    {
        new object[] {"iiisdoso", new int[] {8, 64}},
        new object[] {"iiisdosodddddiso", new int[] {8, 64, 3600}},
    };

    [Test, TestCaseSource("sampleTestCases")]
    public void SampleTest(string data, int[] expected)
    {
        Assert.AreEqual(expected, Deadfish.Parse(data));
    }
}