using NUnit.Framework;

class ExampleTest
{
    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(1L, Kata.Layers(1));
        Assert.AreEqual(2L, Kata.Layers(5));
        Assert.AreEqual(3L, Kata.Layers(25));
        Assert.AreEqual(4L, Kata.Layers(30));
        Assert.AreEqual(5L, Kata.Layers(50));
    }
}