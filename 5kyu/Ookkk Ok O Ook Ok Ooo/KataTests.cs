using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual("H", Kata.OkkOokOo("Ok, Ook, Ooo!"));
        Assert.AreEqual("e", Kata.OkkOokOo("Okk, Ook, Ok!"));
        Assert.AreEqual("l", Kata.OkkOokOo("Okk, Okk, Oo!"));
        Assert.AreEqual("o", Kata.OkkOokOo("Okk, Okkkk!"));
        Assert.AreEqual("W", Kata.OkkOokOo("Ok, Ok, Okkk!"));
        Assert.AreEqual("r", Kata.OkkOokOo("Okkk, Ook, O!"));
        Assert.AreEqual("d", Kata.OkkOokOo("Okk, Ook, Oo!"));
    }
}