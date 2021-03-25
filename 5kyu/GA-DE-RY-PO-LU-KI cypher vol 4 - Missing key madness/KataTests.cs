using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTest()
    {
        string[] messages = {"dance", "level", "right", "yours"};
        string[] secretes = {"tpnes", "irvri", "dkucr", "elghy"};
        Assert.AreEqual("akerilnuopty", Kata.SearchForKey(messages, secretes));
    }
}