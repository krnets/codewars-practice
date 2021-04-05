using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test, Description("test")]
    public void Test1()
    {
        Assert.AreEqual("grfg", Kata.Rot13("test"),
            $"Input: test, Expected Output: grfg, Actual Output: {Kata.Rot13("test")}");
    }

    [Test, Description("Test")]
    public void Test2()
    {
        Assert.AreEqual("Grfg", Kata.Rot13("Test"),
            $"Input: Test, Expected Output: Grfg, Actual Output: {Kata.Rot13("Test")}");
    }
}