using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(1, Solution.solve(1));
        Assert.AreEqual(2, Solution.solve(2));
        Assert.AreEqual(18, Solution.solve(18));
        Assert.AreEqual(48, Solution.solve(48));
        Assert.AreEqual(99, Solution.solve(100));
        Assert.AreEqual(9, Solution.solve(10));
        Assert.AreEqual(99, Solution.solve(110));
        Assert.AreEqual(1999, Solution.solve(2090));
        Assert.AreEqual(999999999989, Solution.solve(999999999992));
    }
}