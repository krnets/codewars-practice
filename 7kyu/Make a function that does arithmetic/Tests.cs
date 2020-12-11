using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(3, Kata.Arithmetic(1, 2, "add"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(6, Kata.Arithmetic(8, 2, "subtract"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(10, Kata.Arithmetic(5, 2, "multiply"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(4, Kata.Arithmetic(8, 2, "divide"));
    }
}