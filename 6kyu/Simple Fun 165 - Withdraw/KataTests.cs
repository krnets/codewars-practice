using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTest1()
    {
        var kata = new Kata();
        Assert.AreEqual(new int[] {0, 0, 2}, kata.Withdraw(40));
    }

    [Test]
    public void BasicTest2()
    {
        var kata = new Kata();
        Assert.AreEqual(new int[] {2, 1, 0}, kata.Withdraw(250));
    }

    [Test]
    public void BasicTest3()
    {
        var kata = new Kata();
        Assert.AreEqual(new int[] {2, 0, 3}, kata.Withdraw(260));
    }

    [Test]
    public void BasicTest4()
    {
        var kata = new Kata();
        Assert.AreEqual(new int[] {1, 1, 4}, kata.Withdraw(230));
    }

    [Test]
    public void BasicTest5()
    {
        var kata = new Kata();
        Assert.AreEqual(new int[] {0, 0, 3}, kata.Withdraw(60));
    }
}