using NUnit.Framework;

[TestFixture]
public class StrongestEvenNumberTest
{
    [Test]
    public void SampleTests()
    {
        Assert.AreEqual(2, StrongestEvenNumber.strongestEven(1, 2));
        Assert.AreEqual(8, StrongestEvenNumber.strongestEven(5, 10));
        Assert.AreEqual(48, StrongestEvenNumber.strongestEven(48, 56));
        Assert.AreEqual(192, StrongestEvenNumber.strongestEven(129, 193));
    }
}