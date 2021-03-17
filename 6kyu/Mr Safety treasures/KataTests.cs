using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTest()
    {
        Assert.AreEqual("66542", Kata.Unlock("Nokia"));
        Assert.AreEqual("82588", Kata.Unlock("Valut"));
        Assert.AreEqual("864538", Kata.Unlock("toilet"));
    }
}