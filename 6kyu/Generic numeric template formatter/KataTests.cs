using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual("546 52532 89", Kata.NumericFormatter("xxx xxxxx xx", "5465253289"));
        Assert.AreEqual("123 45678 90", Kata.NumericFormatter("xxx xxxxx xx"));
        Assert.AreEqual("+555 1803 1978", Kata.NumericFormatter("+555 aaaa bbbb", "18031978"));
        Assert.AreEqual("+555 1234 5678", Kata.NumericFormatter("+555 aaaa bbbb"));
        Assert.AreEqual("1234 5678 9012", Kata.NumericFormatter("xxxx yyyy zzzz"));
    }
}