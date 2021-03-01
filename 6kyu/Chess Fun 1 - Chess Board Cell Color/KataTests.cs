using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTest1()
    {
        var kata = new Kata();
        Assert.AreEqual(true, kata.ChessBoardCellColor("A1", "C3"));
    }

    [Test]
    public void BasicTest2()
    {
        var kata = new Kata();
        Assert.AreEqual(false, kata.ChessBoardCellColor("A1", "H3"));
    }

    [Test]
    public void BasicTest3()
    {
        var kata = new Kata();
        Assert.AreEqual(false, kata.ChessBoardCellColor("A1", "A2"));
    }
}