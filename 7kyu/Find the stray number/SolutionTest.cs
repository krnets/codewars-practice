using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SimpleArray1()
    {
        Assert.AreEqual(2, Solution.Stray(new int[] {1, 1, 2}));
    }
}