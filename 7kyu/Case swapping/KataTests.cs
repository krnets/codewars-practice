using NUnit.Framework;

[TestFixture]
public class SwapTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("hELLOwORLD", Kata.Swap("HelloWorld"));
        Assert.AreEqual("cODEwARS", Kata.Swap("CodeWars"));
    }
}