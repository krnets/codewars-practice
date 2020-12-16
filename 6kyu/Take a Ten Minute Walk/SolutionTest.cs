using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(true, Kata.IsValidWalk(new string[] {"n", "s", "n", "s", "n", "s", "n", "s", "n", "s"}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(false,
            Kata.IsValidWalk(new string[] {"w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"}));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(false, Kata.IsValidWalk(new string[] {"w"}));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(false, Kata.IsValidWalk(new string[] {"n", "n", "n", "s", "n", "s", "n", "s", "n", "s"}));
    }
}