using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    private static object[] Basic_Test_Cases = new object[]
    {
        new object[] {"a b c d e fgh", "fgh"},
        new object[] {"one two three", "three"},
        new object[] {"red blue grey", "grey"},
    };

    [Test, TestCaseSource(typeof(SolutionTest), "Basic_Test_Cases")]
    public void Basic_Test(string test, string expected)
    {
        Assert.AreEqual(expected, Kata.LongestWord(test));
    }
}