using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void KataTest1()
    {
        Assert.AreEqual("theStealthWarrior", Kata.ToCamelCase("the_stealth_warrior"));
    }

    [Test]
    public void KataTest2()
    {
        Assert.AreEqual("TheStealthWarrior", Kata.ToCamelCase("The-Stealth-Warrior"));
    }

    [Test]
    public void KataTest3()
    {
        Assert.AreEqual("", Kata.ToCamelCase(""), "An empty string was provided but not returned");
    }

    [Test]
    public void KataTest4()
    {
        Assert.AreEqual("ABC", Kata.ToCamelCase("A-B-C"), "Kata.ToCamelCase('A-B-C') did not return correct value");
    }
}