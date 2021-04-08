using NUnit.Framework;

[TestFixture]
[DefaultFloatingPointTolerance(.000002)]
public class SuiteTests
{
    [Test]
    public void Test01()
    {
        Assert.AreEqual(1.275, Suite.going(5));
    }

    [Test]
    public void Test02()
    {
        Assert.AreEqual(1.2125, Suite.going(6));
    }

    [Test]
    public void Test03()
    {
        Assert.AreEqual(1.173214, Suite.going(7));
    }
}