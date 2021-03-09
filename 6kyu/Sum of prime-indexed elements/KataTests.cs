using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(0, Solution.solve(new int [] {}));
        Assert.AreEqual(7, Solution.solve(new int [] {1,2,3,4}));     
        Assert.AreEqual(13, Solution.solve(new int [] {1,2,3,4,5,6}));
        Assert.AreEqual(47, Solution.solve(new int [] {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}));
   
    }
}