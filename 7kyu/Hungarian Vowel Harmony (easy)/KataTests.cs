using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("ablaknak", Kata.Dative("ablak"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("tükörnek", Kata.Dative("tükör"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("keretnek", Kata.Dative("keret"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual("otthonnak", Kata.Dative("otthon"));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual("virágnak", Kata.Dative("virág"));
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual("tettnek", Kata.Dative("tett"));
    }

    [Test]
    public void ExampleTest7()
    {
        Assert.AreEqual("rokkantnak", Kata.Dative("rokkant"));
    }

    [Test]
    public void ExampleTest8()
    {
        Assert.AreEqual("rossznak", Kata.Dative("rossz"));
    }

    [Test]
    public void ExampleTest9()
    {
        Assert.AreEqual("gonosznak", Kata.Dative("gonosz"));
    }
}