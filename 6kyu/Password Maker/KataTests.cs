using NUnit.Framework;

public class ExampleTests
{
    [Test]
    public void TestUpperOnly()
    {
        bool upper = true, lower = false, digits = false;
        int len = 5;
        Util.Validate(Dinglemouse.MakePassword(len, upper, lower, digits), len, upper, lower, digits);
    }

    [Test]
    public void TestLowerOnly()
    {
        bool upper = false, lower = true, digits = false;
        int len = 5;
        Util.Validate(Dinglemouse.MakePassword(len, upper, lower, digits), len, upper, lower, digits);
    }

    [Test]
    public void TestDigitsOnly()
    {
        bool upper = false, lower = false, digits = true;
        int len = 5;
        Util.Validate(Dinglemouse.MakePassword(len, upper, lower, digits), len, upper, lower, digits);
    }
}