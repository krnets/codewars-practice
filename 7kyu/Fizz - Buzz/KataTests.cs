using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    private static object[] sampleTestCases = new object[]
    {
        new object[] {20, new int[] {5, 2, 1}},
        new object[] {2, new int[] {0, 0, 0}},
        new object[] {30, new int[] {8, 4, 1}},
        new object[] {300, new int[] {80, 40, 19}},
    };

    [Test, TestCaseSource("sampleTestCases")]
    public void SampleTest(int number, int[] expected)
    {
        Assert.AreEqual(expected, Kata.Solution(number));
    }
}