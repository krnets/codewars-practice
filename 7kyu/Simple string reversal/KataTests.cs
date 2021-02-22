using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("srawedoc", Solution.solve("codewars"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("edoc ruoy", Solution.solve("your code"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("skco redo cruoy", Solution.solve("your code rocks"));
    }
}