using NUnit.Framework;


[TestFixture]
public class Test
{
    [Test]
    public void Test1()
    {
        StringAssert.AreEqualIgnoringCase("loquen", Kata.Remove_char("eloquent"));
    }

    [Test]
    public void Test2()
    {
        StringAssert.AreEqualIgnoringCase("ountr", Kata.Remove_char("country"));
    }

    [Test]
    public void Test3()
    {
        StringAssert.AreEqualIgnoringCase("erso", Kata.Remove_char("person"));
    }

    [Test]
    public void Test4()
    {
        StringAssert.AreEqualIgnoringCase("lac", Kata.Remove_char("place"));
    }

    [Test]
    public void Test5()
    {
        StringAssert.AreEqualIgnoringCase("", Kata.Remove_char("ok"));
    }
}