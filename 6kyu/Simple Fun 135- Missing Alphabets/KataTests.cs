using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void BasicTest1()
    {
        var kata = new Kata();
        Assert.AreEqual("z", kata.MissingAlphabets("abcdefghijklmnopqrstuvwxy"));
    }

    [Test]
    public void BasicTest2()
    {
        var kata = new Kata();
        Assert.AreEqual("", kata.MissingAlphabets("abcdefghijklmnopqrstuvwxyz"));
    }

    [Test]
    public void BasicTest3()
    {
        var kata = new Kata();
        Assert.AreEqual("zz", kata.MissingAlphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"));
    }

    [Test]
    public void BasicTest4()
    {
        var kata = new Kata();
        Assert.AreEqual("ayzz", kata.MissingAlphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"));
    }

    [Test]
    public void BasicTest5()
    {
        var kata = new Kata();
        Assert.AreEqual("bfghijklmnpqtuvxyz", kata.MissingAlphabets("codewars"));
    }
}