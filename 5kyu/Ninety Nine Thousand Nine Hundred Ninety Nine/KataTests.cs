using NUnit.Framework;

[TestFixture]
internal class Tests
{
    [TestCase(-4, "")]
    [TestCase(0, "zero")]
    [TestCase(7, "seven")]
    [TestCase(11, "eleven")]
    [TestCase(20, "twenty")]
    [TestCase(47, "forty seven")]
    [TestCase(100, "one hundred")]
    [TestCase(219, "two hundred nineteen")]
    [TestCase(305, "three hundred five")]
    [TestCase(4002, "four thousand two")]
    [TestCase(20005, "twenty thousand five")]
    [TestCase(6800, "six thousand eight hundred")]
    [TestCase(14111, "fourteen thousand one hundred eleven")]
    [TestCase(3892, "three thousand eight hundred ninety two")]
    [TestCase(99999, "ninety nine thousand nine hundred ninety nine")]
    public void BasicTest(int n, string expected)
    {
        Assert.That(Kata.NumberToEnglish(n), Is.EqualTo(expected));
    }
}