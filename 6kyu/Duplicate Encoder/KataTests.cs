using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual("(((", Kata.DuplicateEncode("din"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual("()()()", Kata.DuplicateEncode("recede"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(")())())", Kata.DuplicateEncode("Success"), "should ignore case");
    }

    [Test]
    public void BasicTest4()
    {
        Assert.AreEqual("))((", Kata.DuplicateEncode("(( @"));
    }

    [Test]
    public void BasicTest5()
    {
        Assert.AreEqual("()(((())())", Kata.DuplicateEncode("CodeWarrior"));
    }

    [Test]
    public void BasicTest6()
    {
        Assert.AreEqual(")()))()))))()(", Kata.DuplicateEncode("Supralapsarian"), "should ignore case");
    }

    [Test]
    public void BasicTest7()
    {
        Assert.AreEqual("))))))", Kata.DuplicateEncode("iiiiii"), "duplicate-only-string");
    }
}