using NUnit.Framework;

[TestFixture]
public class CypherTest
{
    [Test]
    public void BasicTest()
    {
        string[] messages = {"dance on the table", "hide my beers", "scouts rocks"};
        string[] secretes = {"egncd pn thd tgbud", "hked mr bddys", "scplts ypcis"};
        Assert.AreEqual("agdeikluopry", Kata.FindTheKey(messages, secretes));
    }
}