using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(true, Solution.solve("abc"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(false, Solution.solve("abd"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(true, Solution.solve("dabc"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(false, Solution.solve("abbc"));
    }
}