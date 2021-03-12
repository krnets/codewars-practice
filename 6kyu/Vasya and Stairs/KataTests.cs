using NUnit.Framework;

[TestFixture]
public class StairsTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(6, Stairs.NumberOfSteps(10, 2));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(-1, Stairs.NumberOfSteps(3, 5));
    }
}