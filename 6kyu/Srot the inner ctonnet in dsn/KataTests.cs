using NUnit.Framework;

public class KataTests
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("srot the inner ctonnet in dsnnieedcg oredr",
            Kata.SortTheInnerContent("sort the inner content in descending order"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("wiat for me", Kata.SortTheInnerContent("wait for me"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("tihs ktaa is esay", Kata.SortTheInnerContent("this kata is easy"));
    }
}