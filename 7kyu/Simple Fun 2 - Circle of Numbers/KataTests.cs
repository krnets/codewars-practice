using NUnit.Framework;

[TestFixture]
public class myjinxin
{
    [Test]
    public void TestCase()
    {
        var kata = new Kata();

        Assert.AreEqual(7, kata.CircleOfNumbers(10, 2), "");

        Assert.AreEqual(2, kata.CircleOfNumbers(10, 7), "");

        Assert.AreEqual(3, kata.CircleOfNumbers(4, 1), "");

        Assert.AreEqual(0, kata.CircleOfNumbers(6, 3), "");
    }
}