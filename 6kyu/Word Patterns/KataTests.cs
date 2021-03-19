using NUnit.Framework;

[TestFixture]
public class WordPatternTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(true, Kata.WordPattern("abab", "apple banana apple banana"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(true, Kata.WordPattern("abba", "car truck truck car"));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(false, Kata.WordPattern("abab", "apple banana banana apple"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(true, Kata.WordPattern("aaaa", "cat cat cat cat"));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual(false, Kata.WordPattern("aaaa", "cat cat dog cat"));
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual(true, Kata.WordPattern("bbbabcb", "c# c# c# javascript c# python c#"));
    }

    [Test]
    public void ExampleTest7()
    {
        Assert.AreEqual(true, Kata.WordPattern("abcdef", "apple banana cat donkey elephant flower"));
    }

    [Test]
    public void ExampleTest8()
    {
        Assert.AreEqual(false, Kata.WordPattern("xyzzyx", "apple banana apple banana"));
    }

    [Test]
    public void ExampleTest9()
    {
        Assert.AreEqual(true, Kata.WordPattern("xyzzyx", "1 2 3 3 2 1"));
    }

    [Test]
    public void ExampleTest10()
    {
        Assert.AreEqual(true, Kata.WordPattern("aafggiilp", "cow cow fly pig pig sheep sheep chicken aardvark"));
    }

    [Test]
    public void ExampleTest11()
    {
        Assert.AreEqual(false, Kata.WordPattern("aafggiilp", "cow cow fly rooster pig sheep sheep chicken aardvark"));
    }

    [Test]
    public void ExampleTest12()
    {
        Assert.AreEqual(false, Kata.WordPattern("aaaa", "cat cat cat"));
    }

    [Test]
    public void ExampleTest13()
    {
        Assert.AreEqual(false, Kata.WordPattern("abba", "dog dog dog dog"));
    }

    [Test]
    public void ExampleTest14()
    {
        Assert.AreEqual(false,
            Kata.WordPattern("dgxvotikgbgfkjudxbwdelunnu",
                "nhetodtmeq saarnegijgbksl fgqrqwolmrbwk oblqukslepx fgqrqwolmrbwk dyjscxblvoeo vmrmiwuqpvcb dlbbanmuuu oblqukslepx xkmigmsobip dyjscxblvoeo dlbbanmuuu fgqrqwolmrbwk qlffminnabd vjjqhrbevuiqin dcmuylrawqjnji wsfmxfprsnpm nhetodtmeq emggqgjmlvhxhm thuirkaiju pdfalrbtuq pdfalrbtuq koppfwwvcimsuf wsfmxfprsnpm saarnegijgbksl emggqgjmlvhxhm"));
    }
}