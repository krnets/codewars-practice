using NUnit.Framework;
using System;
 
[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual(1, Solution.solve(new int[] {1,1,1}));
        Assert.AreEqual(2, Solution.solve(new int[] {1,2,1}));    
        Assert.AreEqual(2, Solution.solve(new int[] {4,1,1}));
        Assert.AreEqual(9, Solution.solve(new int[] {8,2,8}));
        Assert.AreEqual(5, Solution.solve(new int[] {8,1,4}));
        Assert.AreEqual(10, Solution.solve(new int[] {7,4,10}));
        Assert.AreEqual(18, Solution.solve(new int[] {12,12,12}));
        Assert.AreEqual(3, Solution.solve(new int[] {1,23,2}));   
    }
}