using NUnit.Framework;

public class Test
{
    [TestCase(2, 'A', ExpectedResult = "| | |A| | | | | | |")]
    [TestCase(0, 'A', ExpectedResult = "|A| | | | | | | | |")]
    [TestCase(8, 'A', ExpectedResult = "| | | | | | | | |A|")]
    public static string FixedTest(int index, char character)
    {
        return Kata.BuildRowText(index, character);
    }
}