using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    [TestCase(100000, ExpectedResult = "100,000")]
    [TestCase(5678545, ExpectedResult = "5,678,545")]
    [TestCase(-420902, ExpectedResult = "-420,902")]
    public static string FixedTest(int num)
    {
        return Kata.NumberFormat(num);
    }
}