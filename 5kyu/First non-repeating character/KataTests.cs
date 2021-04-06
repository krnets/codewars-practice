using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("a", Kata.FirstNonRepeatingLetter("a"));
        Assert.AreEqual("t", Kata.FirstNonRepeatingLetter("stress"));
        Assert.AreEqual("e", Kata.FirstNonRepeatingLetter("moonmen"));
    }
}