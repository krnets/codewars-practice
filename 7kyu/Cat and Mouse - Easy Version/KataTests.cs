using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("Escaped!", Kata.CatMouse("C....m"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("Caught!", Kata.CatMouse("C..m"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("Escaped!", Kata.CatMouse("C.....m"));
    }
}