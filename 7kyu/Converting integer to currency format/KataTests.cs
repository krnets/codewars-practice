using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    [TestCase(100000, ExpectedResult="100,000")]
    [TestCase(5678545, ExpectedResult="5,678,545")]
    public static string FixedTest(int price)
    {
        return Kata.ToCurrency(price);
    }
}