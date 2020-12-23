using NUnit.Framework;

[TestFixture]
public class TortoiseTests
{
    [Test]
    public void Test1()
    {
        Assert.AreEqual(new int[] {0, 32, 18}, Tortoise.Race(720, 850, 70));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(new int[] {3, 21, 49}, Tortoise.Race(80, 91, 37));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(new int[] {2, 0, 0}, Tortoise.Race(80, 100, 40));
    }
}