using NUnit.Framework;

[TestFixture]
public class AccountTest
{
    [Test]
    public void ValueTest1()
    {
        Padovan t = new Padovan();
        Assert.AreEqual(1, t.Get(1));
    }

    [Test]
    public void ValueTest5()
    {
        Padovan t = new Padovan();
        Assert.AreEqual(3, t.Get(5));
        // 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...
    }

    [Test]
    public void ValueTest8()
    {
        Padovan t = new Padovan();
        Assert.AreEqual(7, t.Get(8));
    }

    [Test]
    public void ValueTest11()
    {
        Padovan t = new Padovan();
        Assert.AreEqual(16, t.Get(11));
    }

    [Test]
    public void ValueTest14()
    {
        Padovan t = new Padovan();
        Assert.AreEqual(37, t.Get(14));
    }
}