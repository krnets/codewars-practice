using NUnit.Framework;

[TestFixture]
public class GroupingTest
{
    [Test]
    public void Test_1()
    {
        Assert.AreEqual("1", Kata.GenerateGroupings(new int[] {1}));
    }

    [Test]
    public void Test_1_3()
    {
        Assert.AreEqual("1, 3", Kata.GenerateGroupings(new int[] {1, 3}));
    }

    [Test]
    public void Test_1_2_3()
    {
        Assert.AreEqual("1-3", Kata.GenerateGroupings(new int[] {1, 2, 3}));
    }

    [Test]
    public void Test_5_3_4_1_2()
    {
        Assert.AreEqual("1-5", Kata.GenerateGroupings(new int[] {5, 3, 4, 1, 2}));
    }
}