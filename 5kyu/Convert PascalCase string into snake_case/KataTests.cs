using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("test_controller", Kata.ToUnderscore("TestController"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("this_is_beautiful_day", Kata.ToUnderscore("ThisIsBeautifulDay"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("am7_days", Kata.ToUnderscore("Am7Days"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("my3_code_is4_times_better", Kata.ToUnderscore("My3CodeIs4TimesBetter"));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual("arbitrarily_sending_different_types_to_functions_makes_katas_cool",
            Kata.ToUnderscore("ArbitrarilySendingDifferentTypesToFunctionsMakesKatasCool"));
    }

    [Test]
    public void SampleTest6()
    {
        Assert.AreEqual("1", Kata.ToUnderscore(1), "Numbers should be turned to strings!");
    }
}