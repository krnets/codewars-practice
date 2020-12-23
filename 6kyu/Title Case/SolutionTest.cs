using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void MyTest1()
    {
        Assert.AreEqual("A Clash of Kings", Kata.TitleCase("a clash of KINGS", "a an the of"));
    }

    [Test]
    public void MyTest2()
    {
        Assert.AreEqual("", Kata.TitleCase(""));
    }

    [Test]
    public void MyTest3()
    {
        Assert.AreEqual("The Quick Brown Fox", Kata.TitleCase("the quick brown fox"));
    }

    [Test]
    public void MyTest4()
    {
        Assert.AreEqual("The Wind in the Willows", Kata.TitleCase("THE WIND IN THE WILLOWS", "The In"));
    }
}