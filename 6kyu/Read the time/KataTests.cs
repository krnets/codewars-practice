using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual("one o'clock", Solution.solve("13:00"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual("nine minutes past one", Solution.solve("13:09"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual("quarter past one", Solution.solve("13:15"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual("twenty nine minutes past one", Solution.solve("13:29"));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual("half past one", Solution.solve("13:30"));
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual("twenty nine minutes to two", Solution.solve("13:31"));
    }

    [Test]
    public void ExampleTest7()
    {
        Assert.AreEqual("quarter to two", Solution.solve("13:45"));
    }

    [Test]
    public void ExampleTest8()
    {
        Assert.AreEqual("one minute to two", Solution.solve("13:59"));
    }

    [Test]
    public void ExampleTest9()
    {
        Assert.AreEqual("twelve minutes to one", Solution.solve("00:48"));
    }

    [Test]
    public void ExampleTest10()
    {
        Assert.AreEqual("eight minutes past midnight", Solution.solve("00:08"));
    }

    [Test]
    public void ExampleTest11()
    {
        Assert.AreEqual("twelve o'clock", Solution.solve("12:00"));
    }

    [Test]
    public void ExampleTest12()
    {
        Assert.AreEqual("midnight", Solution.solve("00:00"));
    }

    [Test]
    public void ExampleTest13()
    {
        Assert.AreEqual("one minute past seven", Solution.solve("19:01"));
    }

    [Test]
    public void ExampleTest14()
    {
        Assert.AreEqual("one minute past seven", Solution.solve("07:01"));
    }

    [Test]
    public void ExampleTest15()
    {
        Assert.AreEqual("one minute to two", Solution.solve("01:59"));
    }

    [Test]
    public void ExampleTest16()
    {
        Assert.AreEqual("one minute past twelve", Solution.solve("12:01"));
    }

    [Test]
    public void ExampleTest17()
    {
        Assert.AreEqual("one minute past midnight", Solution.solve("00:01"));
    }

    [Test]
    public void ExampleTest18()
    {
        Assert.AreEqual("twenty nine minutes to twelve", Solution.solve("11:31"));
    }

    [Test]
    public void ExampleTest19()
    {
        Assert.AreEqual("twenty nine minutes to midnight", Solution.solve("23:31"));
    }

    [Test]
    public void ExampleTest20()
    {
        Assert.AreEqual("one minute past midnight", Solution.solve("00:01"));
    }

    [Test]
    public void ExampleTest21()
    {
        Assert.AreEqual("quarter to twelve", Solution.solve("11:45"));
    }

    [Test]
    public void ExampleTest22()
    {
        Assert.AreEqual("one minute to twelve", Solution.solve("11:59"));
    }

    [Test]
    public void ExampleTest23()
    {
        Assert.AreEqual("quarter to midnight", Solution.solve("23:45"));
    }

    [Test]
    public void ExampleTest24()
    {
        Assert.AreEqual("one minute to midnight", Solution.solve("23:59"));
    }

    [Test]
    public void ExampleTest25()
    {
        Assert.AreEqual("quarter to two", Solution.solve("01:45"));
    }

    [Test]
    public void ExampleTest26()
    {
        // Expected: "quarter past eleven"
        // But was:  "quarter past midnight"
        // ------------------------^
        Assert.AreEqual("quarter past eleven", Solution.solve("23:15"));
    }
    [Test]
    public void ExampleTest27()
    {
        // Expected: "quarter to one"
        // But was:  " minutes to one"
        // -----------^
        Assert.AreEqual("quarter to one", Solution.solve("00:45"));
    }
    [Test]
    public void ExampleTest28()
    {
        // Expected: "quarter past midnight"
        // But was:  "quarter past o'clock"
        // ------------------------^
        Assert.AreEqual("quarter past midnight", Solution.solve("00:15"));
    }
    [Test]
    public void ExampleTest29()
    {
        // Expected: "thirteen minutes to one"
        // But was:  "thirteen minutes to thirteen"
        // -------------------------------^
        Assert.AreEqual("thirteen minutes to one", Solution.solve("12:47"));
    }
}