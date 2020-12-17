using NUnit.Framework;

[TestFixture]
public class WhichAreInTests
{
    [Test]
    public void Test1()
    {
        string[] a1 = {"arp", "live", "strong"};
        string[] a2 = {"lively", "alive", "harp", "sharp", "armstrong"};

        string[] expected = {"arp", "live", "strong"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test2()
    {
        string[] a1 = {"arp", "mice", "bull"};
        string[] a2 = {"lively", "alive", "harp", "sharp", "armstrong"};

        string[] expected = {"arp"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test3()
    {
        string[] a1 = {"cod", "code", "wars", "ewar"};
        string[] a2 = {"lively", "alive", "harp", "sharp", "armstrong", "codewars"};

        string[] expected = {"cod", "code", "ewar", "wars"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test4()
    {
        string[] a1 = {"cod", "code", "wars", "ewar", "ar"};
        string[] a2 = {"lively", "alive", "harp", "sharp", "armstrong", "codewars"};

        string[] expected = {"ar", "cod", "code", "ewar", "wars"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test5()
    {
        string[] a1 = {"cod", "code", "wars", "ewar", "ar"};
        string[] a2 = { };

        string[] expected = { };
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test6()
    {
        string[] a1 = {"1295", "code", "1346", "1028", "ar"};
        string[] a2 = {"12951295", "ode", "46", "10281066", "par"};

        string[] expected = {"1028", "1295", "ar"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test7()
    {
        string[] a1 = {"&()", "code", "1346", "1028", "ar"};
        string[] a2 = {"12&()95", "coderange", "46", "1066", "par"};

        string[] expected = {"&()", "ar", "code"};
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }

    [Test]
    public void Test8()
    {
        string[] a1 = {"ohio", "code", "1346", "1028", "art"};
        string[] a2 = {"Carolina", "Ohio", "4600", "NY", "California"};

        string[] expected = { };
        Assert.AreEqual(expected, WhichAreIn.inArray(a1, a2));
    }
}