using NUnit.Framework;

[TestFixture]
public class Suite2Tests
{
    [Test]
    public void Test01()
    {
        Assert.AreEqual("[0]", Suite2.game(0));
    }

    [Test]
    public void Test02()
    {
        Assert.AreEqual("[1, 2]", Suite2.game(1));
    }

    [Test]
    public void Test03()
    {
        Assert.AreEqual("[32]", Suite2.game(8));
    }

    [Test]
    public void Test04()
    {
        Assert.AreEqual("[800]", Suite2.game(40));
    }

    [Test]
    public void Test05()
    {
        Assert.AreEqual("[10201, 2]", Suite2.game(101));
    }

    [Test]
    public void Test06()
    {
        Assert.AreEqual("[20808]", Suite2.game(204));
    }

    [Test]
    public void Test07()
    {
        Assert.AreEqual("[651249, 2]", Suite2.game(807));
    }

    [Test]
    public void Test08()
    {
        Assert.AreEqual("[12570098]", Suite2.game(5014));
    }
}