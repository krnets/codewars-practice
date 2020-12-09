using NUnit.Framework;

[TestFixture]
public class ConverterTests
{
    [Test]
    public void Test1()
    {
        int[] numbers = {5, 8, 12, 19, 22};
        Assert.AreEqual(13, Kata.sumTwoSmallestNumbers(numbers));		
    }  
}