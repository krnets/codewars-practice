using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("1337", Kata.ToLeetSpeak("LEET"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("(0D3W@R$", Kata.ToLeetSpeak("CODEWARS"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual("#3110 W0R1D", Kata.ToLeetSpeak("HELLO WORLD"));
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("10R3M !P$UM D010R $!7 @M37", Kata.ToLeetSpeak("LOREM IPSUM DOLOR SIT AMET"));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06",
            Kata.ToLeetSpeak("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"));
    }
}