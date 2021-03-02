using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTests()
    {
        Assert.IsTrue(Kata.omnibool == true);
        Assert.IsTrue(Kata.omnibool == false);
    }
}