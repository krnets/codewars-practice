using NUnit.Framework;

class Assertions
{
    public static void Valid(string s)
    {
        bool expected = true;
        bool actual = Brace.validBraces(s);
        Assert.AreEqual(expected, actual);
    }

    public static void Invalid(string s)
    {
        bool expected = false;
        bool actual = Brace.validBraces(s);
        Assert.AreEqual(expected, actual);
    }
}

[TestFixture]
public class BraceTests
{
    [Test]
    public void Test1()
    {
        Assertions.Valid("()");
    }

    [Test]
    public void Test2()
    {
        Assertions.Valid("[]");
    }

    [Test]
    public void Test3()
    {
        Assertions.Valid("(){}[]");
    }

    [Test]
    public void Test4()
    {
        Assertions.Valid("([{}])");
    }

    [Test]
    public void Test5()
    {
        Assertions.Valid("([{}])");
    }

    [Test]
    public void Test6()
    {
        Assertions.Invalid("[(])");
    }

    [Test]
    public void Test7()
    {
        Assertions.Valid("({})[({})]");
    }

    [Test]
    public void Test8()
    {
        Assertions.Invalid("(})");
    }

    [Test]
    public void Test9()
    {
        Assertions.Valid("{}");
    }

    [Test]
    public void Test10()
    {
        Assertions.Valid("(({{[[]]}}))");
    }

    [Test]
    public void Test11()
    {
        Assertions.Valid("{}({})[]");
    }

    [Test]
    public void Test12()
    {
        Assertions.Invalid(")(}{][");
    }

    [Test]
    public void Test13()
    {
        Assertions.Invalid("())({}}{()][][");
    }

    [Test]
    public void Test14()
    {
        Assertions.Invalid("(((({{");
    }

    [Test]
    public void Test15()
    {
        Assertions.Invalid("}}]]))}])");
    }
}