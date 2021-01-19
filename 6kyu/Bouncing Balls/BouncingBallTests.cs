using NUnit.Framework;

[TestFixture]
public class BouncingBallTests
{
    [Test]
    public void Test0()
    {
        Assert.AreEqual(1, BouncingBall.bouncingBall(2.0, 0.5, 1));
    }

    [Test]
    public void Test1()
    {
        Assert.AreEqual(3, BouncingBall.bouncingBall(3.0, 0.66, 1.5));
    }

    [Test]
    public void Test2()
    {
        Assert.AreEqual(15, BouncingBall.bouncingBall(30.0, 0.66, 1.5));
    }

    [Test]
    public void Test3()
    {
        Assert.AreEqual(21, BouncingBall.bouncingBall(30, 0.75, 1.5));
    }

    [Test]
    public void Test4()
    {
        Assert.AreEqual(3, BouncingBall.bouncingBall(30, 0.4, 10));
    }

    [Test]
    public void Test5()
    {
        Assert.AreEqual(3, BouncingBall.bouncingBall(40, 0.4, 10));
    }

    [Test]
    public void Test6()
    {
        Assert.AreEqual(-1, BouncingBall.bouncingBall(10, 0.6, 10));
    }

    [Test]
    public void Test7()
    {
        Assert.AreEqual(-1, BouncingBall.bouncingBall(40, 1, 10));
    }

    [Test]
    public void Test8()
    {
        Assert.AreEqual(-1, BouncingBall.bouncingBall(-5, 0.66, 1.5));
    }

    [Test]
    public void Test9()
    {
        Assert.AreEqual(-1, BouncingBall.bouncingBall(5, -1, 1.5));
    }
}