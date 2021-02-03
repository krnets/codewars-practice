using NUnit.Framework;

[TestFixture]
class Tests
{
    [TestCase(00002)]
    [TestCase(00003)]
    [TestCase(00011)]
    [TestCase(00055)]
    [TestCase(25432)]
    public void Special(int number)
    {
        Assert.That(Kata.SpecialNumber(number), Is.EqualTo("Special!!"));
    }

    [TestCase(02783)]
    [TestCase(00006)]
    [TestCase(00009)]
    [TestCase(00026)]
    [TestCase(00092)]
    public void NotSpecial(int number)
    {
        Assert.That(Kata.SpecialNumber(number), Is.EqualTo("NOT!!"));
    }
}