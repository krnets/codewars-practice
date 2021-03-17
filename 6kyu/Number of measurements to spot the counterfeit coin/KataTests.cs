using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(0, Kata.HowManyMeasurements(1));
        Assert.AreEqual(1, Kata.HowManyMeasurements(2));
        Assert.AreEqual(1, Kata.HowManyMeasurements(3));
        Assert.AreEqual(2, Kata.HowManyMeasurements(8));
        Assert.AreEqual(5, Kata.HowManyMeasurements(100));
    }
}