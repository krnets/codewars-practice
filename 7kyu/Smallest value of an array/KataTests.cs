using NUnit.Framework;

[TestFixture]
public class FindSmallest
{
    [Test]
    public void Test_54321_value()
    {
        Assert.AreEqual(1, Kata.FindSmallest(new int[] { 5, 4, 3, 2, 1 }, "value"));
    }

    [Test]
    public void Test_54321_index()
    {
        Assert.AreEqual(4, Kata.FindSmallest(new int[] { 5, 4, 3, 2, 1 }, "index"));
    }
}