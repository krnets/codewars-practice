using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(string.Join(",", new[] {"*"}), string.Join(",", Kata.TowerBuilder(1)));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(string.Join(",", new[] {" * ", "***"}), string.Join(",", Kata.TowerBuilder(2)));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(string.Join(",", new[] {"  *  ", " *** ", "*****"}), string.Join(",", Kata.TowerBuilder(3)));
    }
}