using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(2, Solution.solve(")()("));
        Assert.AreEqual(1, Solution.solve("((()"));
        Assert.AreEqual(-1, Solution.solve("((("));
        Assert.AreEqual(3, Solution.solve("())((("));
        Assert.AreEqual(4, Solution.solve("())()))))()()("));
    }
}