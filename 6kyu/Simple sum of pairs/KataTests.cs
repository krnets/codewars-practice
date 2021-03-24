using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(0, Solution.solve(0));
        Assert.AreEqual(1, Solution.solve(1));     
        Assert.AreEqual(18, Solution.solve(18));
        Assert.AreEqual(11, Solution.solve(29)); 
        Assert.AreEqual(33, Solution.solve(1140));
        Assert.AreEqual(68, Solution.solve(50000000));     
        Assert.AreEqual(144, Solution.solve(15569047737));
        Assert.AreEqual(116, Solution.solve(2452148459));
   
    }
}