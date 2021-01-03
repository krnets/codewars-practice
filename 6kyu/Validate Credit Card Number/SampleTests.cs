using NUnit.Framework;

[TestFixture]
public class SampleTests
{
    [Test]
    public void TestCase1()
    {
        var _ = new solution();
        Assert.AreEqual(false, _.validate("477 073 360"));
    }

    [Test]
    
    public void TestCase2()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("5422 0148 5514"));
    }

    [Test]
    public void TestCase3()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("8314 7046 0245"));
    }

    [Test]
    public void TestCase4()
    {
        var _ = new solution();
        Assert.AreEqual(false, _.validate("6654 6310 43044"));
    }

    [Test]
    public void TestCase5()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("0768 2757 5685 6340"));
    }

    [Test]
    public void TestCase6()
    {
        var _ = new solution();
        Assert.AreEqual(false, _.validate("7164 6207 74042"));
    }

    [Test]
    public void TestCase7()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("8383 7332 3570 8514"));
    }

    [Test]
    public void TestCase8()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("481 135"));
    }

    [Test]
    public void TestCase9()
    {
        var _ = new solution();
        Assert.AreEqual(true, _.validate("355 032 5363"));
    }
}