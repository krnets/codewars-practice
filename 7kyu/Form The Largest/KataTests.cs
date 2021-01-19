using NUnit.Framework;
[TestFixture]
class Tests
{
    [TestCase(213, 321)]
    [TestCase(7389, 9873)]
    [TestCase(63792, 97632)]
    [TestCase(566797, 977665)]
    [TestCase(1000000, 1000000)]
    public void BasicTests(int input, int expected)
    {
        Assert.That(Kata.MaxNumber(input), Is.EqualTo(expected));
    }
}