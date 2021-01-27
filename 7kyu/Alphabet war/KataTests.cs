using NUnit.Framework;

[TestFixture]
public class AlphabetWarTest
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("Right side wins!", Kata.AlphabetWar("z"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("Let's fight again!", Kata.AlphabetWar("zdqmwpbs"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("Right side wins!", Kata.AlphabetWar("zzzzs"));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("Left side wins!", Kata.AlphabetWar("wwwwwwz"));
    }
}