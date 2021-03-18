using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(5, Solution.convergence(3));
        Assert.AreEqual(6, Solution.convergence(5));
        Assert.AreEqual(5, Solution.convergence(10));
        Assert.AreEqual(2, Solution.convergence(15));
        Assert.AreEqual(29, Solution.convergence(500));
        Assert.AreEqual(283, Solution.convergence(5000));
    }
}