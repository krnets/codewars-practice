using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    private static object[] Basic_Test_Cases =
    {
        new object[] {"1+2+3", 6},
        new object[] {"1+2 3", 24},
        new object[] {"1 2 3", 123},
    };

    [Test, TestCaseSource(typeof(SolutionTest), "Basic_Test_Cases")]
    public void Basic_Test(string test, int expected)
    {
        Assert.AreEqual(expected, Kata.Calculate(test));
    }
}