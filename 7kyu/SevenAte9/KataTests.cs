using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [TestCase("165561786121789797", "16556178612178977")]
    [TestCase("797", "77")]
    [TestCase("7979797", "7777")]
    public void ExampleTests(string input, string expected)
    {
        Assert.That(Kata.SevenAteNine(input), Is.EqualTo(expected));
    }
}