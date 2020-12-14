using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("no one likes this", Kata.Likes(new string[0]));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("Peter likes this", Kata.Likes(new string[] {"Peter"}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("Jacob and Alex like this", Kata.Likes(new string[] {"Jacob", "Alex"}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("Max, John and Mark like this", Kata.Likes(new string[] {"Max", "John", "Mark"}));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual("Alex, Jacob and 2 others like this",
            Kata.Likes(new string[] {"Alex", "Jacob", "Mark", "Max"}));
    }
}