using NUnit.Framework;

[TestFixture]
public class RoundUpTestCases
{
    [Test]
    public void OrderedIntegerList()
    {
        Assert.AreEqual(new int[] {8}, Kata.RoundUp(10, new int[] {1, 2, 4, 8, 16, 32}));
    }

    [Test]
    public void NegativeOrderedIntegerList()
    {
        Assert.AreEqual(new int[] {-80, -160}, Kata.RoundUp(-120, new int[] {-10, -20, -40, -80, -160, -320}));
    }

    [Test]
    public void MixedIntegerList()
    {
        Assert.AreEqual(new int[] {-2, 4}, Kata.RoundUp(1, new int[] {-32, 12, 8, -10, -2, 4}));
    }


    [Test]
    public void EmptyIntegerList()
    {
        Assert.AreEqual(new int[] { }, Kata.RoundUp(42, new int[] { }));
    }
}